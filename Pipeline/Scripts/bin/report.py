# Import libraries
import pandas as pd
import sys
import re

# Read .csv file
for infilename in sys.argv[1:]:
    filename = infilename.rsplit("/")[-1] # gives a file name.csv
    list_of_substrings = filename.split("_")
    if "PRRT" in list_of_substrings:
        df_full_prrt = pd.read_excel(infilename)
    if "ENV" in list_of_substrings:
        df_full_env = pd.read_excel(infilename)
    if "INT" in list_of_substrings:
        df_full_int = pd.read_excel(infilename)


outfilename = sys.argv[2]


# Select only what is needed
df_full_prrt = df_full_prrt.loc[:,["Scount", "PRRT_Subsubtype"]]
df_full_int = df_full_int.loc[:,["Scount", "INT_Subsubtype"]]
df_full_env = df_full_env.loc[:,["Scount", "ENV_Subsubtype"]]


# Merge tables
final_report = df_full_prrt.merge(df_full_int, on = "Scount", how = "outer").merge(df_full_env, on = "Scount", how = "outer")

# Rename two first columns 
final_report.rename(columns = {"Scount":"SCount", "PRRT_Subsubtype": "Subtype_PRRT","INT_Subsubtype": "Subtype_INT", "ENV_Subsubtype": "Subtype_ENV"}, inplace = True)

# Initiate empty column
final_report["Subtype"] = None

# Initiate special cases
special_cases = ["noClassified",  "Manual", "notSequenced"]


# Make a decision
for i, row in final_report.iterrows():
    if row["Subtype_PRRT"] == row["Subtype_INT"] and row["Subtype_PRRT"] == row["Subtype_ENV"]:
        final_report.at[i, ["Subtype"]] = row["Subtype_PRRT"]
    
    elif row["Subtype_PRRT"] == row["Subtype_INT"] and len(row["Subtype_PRRT"]) <=2 and len(row["Subtype_ENV"]) > 2 and row["Subtype_ENV"] not in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_ENV"]
    
    elif row["Subtype_PRRT"] == row["Subtype_ENV"] and len(row["Subtype_PRRT"]) <=2 and len(row["Subtype_INT"]) > 2 and row["Subtype_INT"] not in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_INT"]
    
    elif row["Subtype_INT"] == row["Subtype_ENV"] and len(row["Subtype_INT"]) <=2 and len(row["Subtype_PRRT"]) > 2 and row["Subtype_PRRT"] not in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_PRRT"]
    
    elif row["Subtype_PRRT"] == row["Subtype_INT"] and row["Subtype_ENV"] in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_PRRT"]
    
    elif row["Subtype_INT"] == row["Subtype_ENV"] and row["Subtype_PRRT"] in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_INT"]
    
    elif row["Subtype_PRRT"] == row["Subtype_ENV"] and row["Subtype_INT"] in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_PRRT"]

    elif row["Subtype_INT"] in special_cases and row["Subtype_ENV"] in special_cases and row["Subtype_PRRT"] not in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_PRRT"]
    
    elif row["Subtype_PRRT"] in special_cases and row["Subtype_ENV"] in special_cases and row["Subtype_INT"] not in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_INT"]
    
    elif row["Subtype_PRRT"] in special_cases and row["Subtype_INT"] in special_cases and row["Subtype_ENV"] not in special_cases:
        final_report.at[i, ["Subtype"]] = row["Subtype_ENV"]
    
    else:
        final_report.at[i, ["Subtype"]] = "Manual"


# Sort df by SequenceName
final_report.sort_values(by=["SCount"], inplace=True)

# Create output file
datasetname = filename.split("_")[1]
final_report.to_excel(datasetname +"_report.xlsx", index=False, encoding="utf-8")