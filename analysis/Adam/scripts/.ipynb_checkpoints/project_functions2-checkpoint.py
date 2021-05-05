import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

day_table = "../../data/raw/day.csv"

def load_and_process(url_or_path_to_csv_file):

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns = {"instant":"Index", "dteday":"Date","season":"Season","yr":"Year","mnth":"Month","hr":"Hour","holiday":"Holiday","weekday":"Week_day","workingday":"Working_day",
                            "weathersit":"Weather","temp":"Temperature","atemp":"FeelTemp","hum":"Humidity","windspeed":"Wind_speed","casual":"Casual_users","registered":"Registered_users",
                            "cnt": "Total_users"}, errors = "ignore")
        .sort_values(["Index", "Date"])
        .fillna("Data Unavailable")
      )

    df2 = (
        df1
        .assign(AverageTemp = lambda x : (x['FeelTemp'] + x['Temperature']) / 2)
      )

    df2.groupby(['AverageTemp']).mean()
    df2.filter(items=['Index', 'Date', 'AverageTemp'])
      
    return df2

load_and_process(day_table)
