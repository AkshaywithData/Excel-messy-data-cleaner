import pandas as pd
import os
import glob
import shutil

files = glob.glob("Data/Source/*.xlsx")

def read_data():

    os.makedirs("Data/Archive", exist_ok = True)

    dfs = []

    for file in files:

        d = pd.read_excel(file)

        dfs.append(d)

        shutil.move(file, os.path.join("Data/Archive",os.path.basename(file)))

    return dfs

def data_clean(dfs):

    df = pd.concat(dfs, ignore_index=True)

    df.drop_duplicates(inplace = True)

    df.dropna(how = "all", inplace =True)

    df.columns = (df.columns.str.strip().str.replace(" ", "_"))

    df["Customer_Name"] = df["Customer_Name"].astype("string").str.strip().str.title()

    df["Product"] = df["Product"].astype("string").str.strip().str.title()

    df["Category"] = df["Category"].astype("string").str.strip().str.title()

    df["City"] = df["City"].astype("string").str.strip().str.title()

    df["Order_Status"] = df["Order_Status"].astype("string").str.strip().str.title()

    df["Payment_Method"] = df["Payment_Method"].astype("string").str.strip().str.title()

    #fiiling values

    df["Customer_ID"] = df["Customer_ID"].fillna("Unknown")

    df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")

    df.loc[~df["Customer_Name"].str.match(r"^[A-Za-z\s]+$", na=False), "Customer_Name"] = "Unknown"

    df["City"] = df["City"].fillna("Unknown")

    df.loc[~df["City"].str.match(r"^[A-Za-z\s]+$", na=False), "City"] = "Unknown"

    df["Quantity"] = (df["Quantity"].astype(str).str.extract(r"(\d+\.?\d*)")[0])
      
    df["Quantity"] = pd.to_numeric(df["Quantity"],errors="coerce")

    df["Quantity"] = df["Quantity"].fillna(df.groupby("Category")["Quantity"].transform("median"))

    df["Quantity"] = df["Quantity"].round().astype(int)

    df["Unit_Price"] = (df["Unit_Price"].astype(str).str.extract(r"(\d+\.?\d*)")[0])

    df["Unit_Price"] = pd.to_numeric(df["Unit_Price"],errors="coerce")

    df["Unit_Price"] = df["Unit_Price"].fillna(df.groupby("Category")["Unit_Price"].transform("median"))

    df["Order_Date"] = pd.to_datetime(df["Order_Date"],errors="coerce")

    df.dropna(subset=["Order_Date"], inplace=True)

    df["Order_Status"] = df["Order_Status"].fillna(df["Order_Status"].mode()[0])

    return df

def save_data(df):

    os.makedirs("Output", exist_ok=True)

    df.to_excel(os.path.join("Output", "cleaned_data.xlsx"),index=False)


def main():

    dfs = read_data()

    df = data_clean(dfs)

    save_data(df)

if __name__ == "__main__":
    main()










