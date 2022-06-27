###########################################################
# By: Feng Zhang &  Alim Chen
#
# Project: Date Calculator - Python
# Description: Replace a date below and set your     
#              prefered date! Includes a wide variety. 	
#							 Main purpose is to find days between two 
#  					   dates.
# 						 
# NOTE: --------------------
#				
###########################################################

#Import our library
from calendarTools import *

#Set your dates, testcases below
date1 = "Aug 04, 2017"
date2 = "Aug 25, 2017"
date3 = "Sep 10, 2017"
date4 = "Dec 10, 2017"
date5 = "Jan 03, 2018"
date6 = "Mar 03, 2020"
date7 = "Mar 03, 2120"

#Calling function
print(calculateDaysBetween(date1, date2))