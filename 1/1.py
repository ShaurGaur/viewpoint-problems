import pandas as pd

# Student IDs. I'll use them as indexes for the DataFrames.
studentids = ["V001", "V002", "V003", "V004"]

# Tables (provided data).
name_table = pd.DataFrame({
    "Name": ["Abe", "Abhay", "Acelin", "Adelphos"]
}, index=studentids)

mark_table = pd.DataFrame({
    "Total_marks": [95, 80, 74, 81]   
}, index=studentids)

# Function for question 1b. 
def partOneB(df):
    for k in df.index.values:
        s = df.loc[k]["Name"]
        uppercase_e = s.find("E")
        lowercase_e = s.find("e")

        if uppercase_e != -1 or lowercase_e != -1:
            df.loc[k]["Name"] = s.upper()
        else:
            df.loc[k]["Name"] = s.lower()

# Function for question 1c.
def partOneC(names, marks):
    sum_upper, sum_lower, cnt_upper, cnt_lower = 0, 0, 0, 0
    
    for k in names.index.values:
        if names.loc[k]["Name"].isupper():
            cnt_upper += 1
            sum_upper += marks.loc[k]["Total_marks"]
        elif names.loc[k]["Name"].islower():
            cnt_lower += 1
            sum_lower += marks.loc[k]["Total_marks"]

    avg_upper = sum_upper / cnt_upper
    avg_lower = sum_lower / cnt_lower

    result = pd.DataFrame({
        "avg_grade": [avg_upper, avg_lower]
    }, index=["uppercase", "lowercase"])
    
    return result

partOneB(name_table)
print(name_table)
print(partOneC(name_table, mark_table))