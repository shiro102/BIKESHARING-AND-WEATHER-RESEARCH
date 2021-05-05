import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns = {"instant":"Index", "dteday":"Date","season":"Season","yr":"Year","mnth":"Month","hr":"Hour","holiday":"Holiday","weekday":"Week_day","workingday":"Working_day",
                            "weathersit":"Weather","temp":"Temperature","atemp":"FeelTemp","hum":"Humidity","windspeed":"Wind_speed","casual":"Casual_users","registered":"Registered_users",
                            "cnt": "Total_users"}, errors = "ignore")
        .dropna(axis = 0, how = "any")
        .drop(columns = "Index", errors = "ignore")
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .assign(Casual_ratio = lambda x : x['Casual_users'] / x['Total_users'])
        .assign(Registered_ratio = lambda x : x['Registered_users'] / x['Total_users'])
      )
    # Replace weather conditions in column weather
    df2['Weather'] = df2['Weather'].replace([1,2,3,4],["Good(clear or cloudy)","Normal(mist or/and cloudy)","Lightly bad(light snow, rain, thunderstorm)","Severe(heavy Rain, ice pallets,fog)"])
    # Replace season in column season
    df2['Season'] = df2['Season'].replace([1,2,3,4],["Spring","Summer","Fall","Winter"])
    # Replace weekday in column week_day
    df2['Week_day'] = df2['Week_day'].replace([0,1,2,3,4,5,6],["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])


    
    
    # Make sure to return the latest dataframe

    return df2

def box_plot_one(df,var1,var2):
    #Make box plot that only has one figure
    sns.set(rc={'figure.figsize':(15,10)})
    ax = sns.boxplot(x = var1, y = var2, data = df, width = 0.9)
    ax.set(ylabel = " ")
    ax.set_title("Box plot of " + var1 + " by " + var2)

def box_plot_two(df,var1,var2,var3,var4):
    #Make box plot that contains two figures
    fig, axs = plt.subplots(ncols=2)
    sns.set(rc={'figure.figsize':(20,10)})
    ax = sns.boxplot(x = var1, y = var2, data = df, width = 0.9, ax = axs[0])
    ax.set(ylabel = " ")
    ax.set_title("Box plot of " + var1 + " by " + var2)
    ax1 = sns.boxplot(x = var3, y = var4, data = df, width = 0.9, ax = axs[1])
    ax1.set(ylabel = " ")
    ax1.set_title("Box plot of " + var3 + " by " + var4)
    plt.tight_layout()
