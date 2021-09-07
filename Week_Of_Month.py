#!/usr/bin/env python
# coding: utf-8

# In[3]:


import calendar
import numpy as np
calendar.setfirstweekday(6)

def get_week_of_month(day, month, year):
   try:
            
            x = np.array(calendar.monthcalendar(year, month))
            week_of_month = np.where(x==day)[0][0] + 1
   except:
            return(0)
   return(week_of_month)
get_week_of_month(31,5,2021)

