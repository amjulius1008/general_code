# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:15:35 2019

@author: amjuli
"""
# Install business-duration and holidays packages from command prompt
# pip install business-duration
# pip install holidays


from business_duration import businessDuration
import pandas as pd
from datetime import time,datetime
import holidays as pyholidays

time_elapsed = businessDuration(startdate = pd.to_datetime('2019-06-13 14:23:42'),
                                enddate = pd.to_datetime('2019-06-20 14:23:42'),
                                starttime = time(9,0,0),
                                endtime = time(17,0,0),
                                weekendlist = [5,6],
                                holidaylist = pyholidays.UnitedStates(),
                                unit = 'hour')
print(time_elapsed)
