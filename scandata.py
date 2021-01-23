from getpath import *
import shutil
import sqlite3
import pandas as pd
import datetime
from time import strftime

def date_from_epoch(x):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(x))
    return (epoch_start + delta)


def genfiles():
    history = sqlite3.connect(data_path+'/History')
    df1 = pd.read_sql_query('select url, title, visit_count, last_visit_time from urls',history)
    df1['last_visit_time'] = df1['last_visit_time'].apply(lambda x: date_from_epoch(x))
    df1.to_csv("/tmp/fhistory",encoding='utf-8',index=False)

    keywords = sqlite3.connect(data_path+'/History')
    df2 = pd.read_sql_query('select term from keyword_search_terms',keywords)
    df2.to_csv("/tmp/fkeywords",encoding='utf-8',index=False)

    downloads = sqlite3.connect(data_path+'/History')
    df3 = pd.read_sql_query('select target_path from downloads',downloads)
    df3.to_csv("/tmp/fdownloads",encoding='utf-8',index=False)


    logins=sqlite3.connect(data_path+'/Login Data')
    df3 = pd.read_sql_query('select origin_url,username_element,username_value from logins',logins)
    df3.to_csv("/tmp/flogins",encoding='utf-8',index=False)

    topsites=sqlite3.connect(data_path+'/Top Sites')
    df4 = pd.read_sql_query('select url from top_sites',topsites)
    df4.to_csv("/tmp/ftopsites",encoding='utf-8',index=False)

    autofill=sqlite3.connect(data_path+'/Web Data')
    df4 = pd.read_sql_query('select name,value from autofill',autofill)
    df4.to_csv("/tmp/fautofill",encoding='utf-8',index=False)

    shutil.copytree('Accounts/Avatar Images', '/tmp/user-profile-images',dirs_exist_ok=True)


