# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:41:17 2019

@author: amjuli
"""

def df2sqlite(dataframe, db_name = "import.sqlite", tbl_name = "import"):
 
  import sqlite3
  conn=sqlite3.connect(db_name)
  cur = conn.cursor()                                 
 
  wildcards = ','.join(['?'] * len(dataframe.columns))              
  data = [tuple(x) for x in dataframe.values]
 
  cur.execute("drop table if exists %s" % tbl_name)
  col_str = '"' + '","'.join(dataframe.columns) + '"'
  cur.execute("create table %s (%s)" % (tbl_name, col_str))
  cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)
 
  conn.commit()
  conn.close()
  
def listTables(db_name):
    import sqlite3
    con = sqlite3.connect(db_name)
    mycur = con.cursor() 
    mycur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    available_table=(mycur.fetchall())
    return available_table

def dbConnect(filePath,query):
    import sqlite3
    import pandas as pd

    con = sqlite3.connect(filePath)
    data = pd.read_sql_query(query, con)
    con.close()
    return data