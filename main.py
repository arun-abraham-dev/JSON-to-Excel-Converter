import sys
import json
import pandas as pd


def json_to_excel(json_file,excel_file):
    #Step 1 :Open JSON file
    try:
        with open(json_file,"r",encoding="utf-8") as f:
            data=json.load(f)      #now it's a Python dict/list
    except FileNotFoundError:
        sys.exit(f"[error]File not found:{json_file}")
    except json.JSONDecodeError as e:
        sys.exit(f"[error] Invalid JSON in {json_file} : {e}")
    if isinstance(data,dict) and "orders" in data and isinstance(data["orders"],list):
        df=pd.json_normalize(data,record_path="orders",meta=[["user","id"],["user","name"]],errors="ignore")   #columns from the parent object
    else:
        # Step 2 : Flatten JSON into a DataFrame
        df = pd.json_normalize(data)

    #Step 3 : Write DataFrame into Excel
    df.to_excel(excel_file,index=False)

if __name__=="__main__":        #To make sure this runs only when executed directly, not when imported
    json_to_excel("sample_flat.json", "output.xlsx")
    json_to_excel("sample_nested.json", "orders.xlsx")


