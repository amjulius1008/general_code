# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:19:18 2019

@author: amjuli
"""

import pandas as pd
import pandasql as pdsql
from pandasql import sqldf
import sys
import sqlite3
import datetime
import time


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
  
df2sqlite(data, db_name = "googleAnalytics.sqlite", tbl_name = "data_2019")