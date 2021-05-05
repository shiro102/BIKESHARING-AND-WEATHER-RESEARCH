import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):

    df1 =  (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns = {"instant":"Index", "dteday":"Date","season":"Season","yr":"Year","mnth":"Month","hr":"Hour","holiday":"Holiday","weekday":"Week_day","workingday":"Working_day",
                            "weathersit":"Weather","temp":"Temperature","atemp":"FeelTemp","hum":"Humidity","windspeed":"Wind_speed","casual":"Casual_users","registered":"Registered_users",
                            "cnt": "Total_users"}, errors = "ignore")
        .dropna(axis=0, how='any')
        .sort_values(["Index", "Date"])
        .sort_values('Date', ascending=True)
        .drop(columns = "Index", errors = "ignore")

      )

    df2 = (
        df1
        .assign(Average_Temp = lambda x : (x['FeelTemp'] + x['Temperature']) / 2)
        .assign(Casual_ratio = lambda x : x['Casual_users'] / x['Total_users'])
        .assign(Registered_ratio = lambda x : x['Registered_users'] / x['Total_users'])
      )
    
    # Replacing weekdays in column week_day
    df2['Week_day'] = df2['Week_day'].replace([0,1,2,3,4,5,6],["Sun","Mon","Tue","We","Thu","Fri","Sat"])
    # Replacing weather conditions in column weather
    df2['Weather'] = df2['Weather'].replace([1,2,3,4],["Sunny/Clear","Cloudy/Foggy","Rainy/Snowy","Severe Conditions"])
    # Replacing season in column season
    df2['Season'] = df2['Season'].replace([1,2,3,4],["Spring","Summer","Fall","Winter"])

    print(df2)
      
    return df2

def graph_type1(df, var1, var2):
   # graph= sns.displot(data=df, x='Temperature')
    sns.set(rc={'figure.figsize':(25,20)})
    graph= sns.displot( data=df, x= var1, y= var2, kind='kde', bw_adjust=0.01)
    plt.title("Displot of " + var1 + " by " + var2)
    
def graph_type2 (df, var1, var2, var3):
    
    graph= sns.relplot( data=df, x=var1, y=var2, hue= var3)
    plt.title("Relationship Plot of " + var1 + " by " + var2)
    
def graph_type3(df):
    graph4=sns.heatmap(df.corr(), annot=True)
    plt.title("Correlation matrix of " + df )
