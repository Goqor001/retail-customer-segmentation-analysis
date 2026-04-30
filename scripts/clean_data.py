import pandas as pd

def load_data():
    df = pd.read_csv("raw_customer_data.csv")
    return df

def clean_columns(df):
    clean_df = df.copy()
    clean_df.columns = clean_df.columns.str.strip()

    clean_df["order_id"] = pd.to_numeric(clean_df["order_id"],errors="coerce")
    clean_df["age"] = pd.to_numeric(clean_df["age"],errors="coerce")
    clean_df["income"] = pd.to_numeric(clean_df["income"],errors="coerce")
    clean_df["quantity"] = pd.to_numeric(clean_df["quantity"],errors="coerce")
    clean_df["price"] = pd.to_numeric(clean_df["price"],errors="coerce")
    clean_df["customer_name"] = clean_df["customer_name"].str.strip()
    clean_df["city"] = clean_df["city"].str.strip()
    clean_df["product_category"] = clean_df["product_category"].str.strip()
    clean_df["prodcut_name"] = clean_df["product_name"].str.strip()

    return clean_df

def fix_dates(clean_df):
    clean_df = clean_df.copy()

    clean_df["order_date"] = pd.to_datetime(
        clean_df["order_date"],
        errors="coerce",
        dayfirst=False
    )

    print("Bad dates:", clean_df["order_date"].isna().sum())

    return clean_df

def handle_missing_values(clean_df):

    clean_df["age"] = clean_df["age"].fillna(clean_df["age"].mean())
    clean_df["income"] = clean_df["income"].fillna(clean_df["income"].mean)
    clean_df["quantity"] = clean_df["quantity"].fillna(1)
    clean_df = clean_df.dropna(subset="order_date")

    print(clean_df.head(5))
    print(clean_df.isna().sum())

    return clean_df

def remove_duplicates(clean_df):
    clean_df = clean_df.copy()

    print("Duplicates:", clean_df.duplicated().sum())

    clean_df = clean_df.drop_duplicates()
    
    return clean_df    

def business_metrics(clean_df):
    clean_df["revenue"] = clean_df["quantity"] * clean_df["price"]
    clean_df["month"] = clean_df["order_date"].dt.to_period("M").astype(str) 

    return clean_df

def save_clean_data(clean_df):


    clean_df.to_csv("clean_customer_data.csv",index=False)
    print("Clean data are saved")

df = load_data()
clean_df = clean_columns(df)
clean_df = fix_dates(clean_df)
clean_df = handle_missing_values(clean_df)
clean_df = remove_duplicates(clean_df)
clean_df = business_metrics(clean_df)
save_clean_data(clean_df)
