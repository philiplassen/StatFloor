#!/usr/bin/env python3
"""
Trains a prediction Model based on Players
previous 10 game logs as training data
"""
from datetime import date
import pandas as pd
path = "/Users/philiplassen/CS/StatFloor/data/player_data"
pid = "troutmi01"
year = "2017"
start_date = date(int(year), 3, 1)

def get_table(pid, year):
  df = pd.read_csv(path + "/" + pid + "/" + year + "/gameLogs.csv")
  del df['DFS(DK)']
  del df['DFS(FD)']
  del df['Pos']
  df.rename({"Unnamed: 5" : "Away"}, axis = 'columns')
  return df

def date_to_int(date1):
  res = date1.split()
  month = month_to_int(res[0])
  day = int(res[1])
  result_date = date(int(year), month, day)
  return (result_date - start_date).days




def month_to_int(month):
  month = month.lower()
  months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
  return months.index(month) + 1
result = get_table(pid, year)
result["Date"] = result["Date"].apply(date_to_int)
print(result["Unnamed: 5"])
print(result)
# (To Do) Clean DataFrame i.e Strings -> Numbers, NAN -> Numbers, Remove -> Columns

# (To Do) Chunk into Training and Test 10 i.e list of matrices of consecutive 10 Games

# (To Do) Train a model i.e Regression

# (To Do) Cross validation i.e Accuracy of the Model



