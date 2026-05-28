import pandas as pd
import os

data = {
    "Name" : ["Sandeep", "Vijay", "Harsha"],
    "Age" : [22, 21, 20],
    "City" : ["Wgl", "Hnk", "Wpt"],
    "backlogs" : [0, 1, 0]
}



df = pd.DataFrame(data)

# new_row_loc = {"Name" : "Sudhakar", "Age" : 21, "City" : "Wgl", "backlogs" : 0}
# df.loc[len(df.index)] = new_row_loc

data_dir = "data"
os.makedirs(data_dir, exist_ok = True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index = False)

print(f"The csv file is saved to {file_path}")