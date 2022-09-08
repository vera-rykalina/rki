# Import libraries
import pandas as pd
import sys


infilename = sys.argv[1]
outfilename = sys.argv[2]


for infilename in sys.argv[1:]:
    name1 = infilename.rsplit("/")[-1] # gives a file name.csv
    name2 = name1.split("_")[-2] # gives a middle part after splitting by "_"
    name3 = name1.split("joint_")[-1].split(".")[-2] # cuts .csv
    list_of_substrings = name1.split("_")
    df = pd.read_csv(infilename, sep = ",")
    
    # Change data type string -> float
    df["Comet_" + name2 + "_Comment"] = pd.to_numeric(df["Comet_" + name2 + "_Comment"], downcast="float")   
    
    if "PRRT" in list_of_substrings or "INT" in list_of_substrings:
        for i, row in df.iterrows():
            if row["Stanford_" + name2 + "_Subtype"] == row["Comet_" + name2 + "_Subtype"] and row["Comet_" + name2 + "_Comment"] >= 50:
                df.at[i, [name2 + "_Subtype"]] = row["Stanford_" + name2 + "_Subtype"]
            else:
                df.at[i, [name2 + "_Subtype"]] = "Manual" 

        # Prepare .csv file
        df.to_csv("decision_" + name3 + ".csv", sep=",", index=False, encoding="utf-8") 

    if "ENV" in list_of_substrings:
        for i, row in df.iterrows():
            if row["Rega_" + name2 + "_Subtype"][0] == row["Comet_" + name2 + "_Subtype"] and len(row["Rega_" + name2 + "_Subtype"]) < 3 and row["Comet_" + name2 + "_Comment"] >= 50:
                df.at[i, [name2 + "_Subtype"]] = row["Comet_" + name2 + "_Subtype"]

            elif row["Rega_" + name2 + "_Subtype"] != row["Comet_" + name2 + "_Subtype"] and row["Comet_" + name2 + "_Comment"] >= 70:
                df.at[i, [name2 + "_Subtype"]] = row["Comet_" + name2 + "_Subtype"]

            else:
                df.at[i, [name2 + "_Subtype"]] = "Manual"
    
        df.to_csv("decision_" + name3 + ".csv", sep=",", index=False, encoding="utf-8")
