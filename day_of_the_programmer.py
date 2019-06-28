#  -*- coding: utf-8 -*-
""" 
Created on Friday 28 Jun 2019 16:25:12
 
@author: HardcodeCoder
"""

# About Day of the programmer: https://en.wikipedia.org/wiki/Day_of_the_Programmer
# From 1700 to 1917, Russia's official calendar was the julian calendar;
# since 1919 they used the Gregorian calendar system.The transition from 
# the Julian to Gregorian calendar system occurred in 1918 when the next 
# day after 31st January was 14th February . This means that in 1918, February  
# 14th was the  32nd day of the year in Russia.
# Find the date of 256th day of that year
# 1700 <= year <= 2700
# Output format : dd.mm.yyyy

def is_leap_year(year, julian_calendar):
    if julian_calendar:
        return year % 4 == 0
    else:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_date(year):
    feb = 28
    jul_cal = False
    if year <= 1917 : 
        jul_cal = True
    if is_leap_year(year, jul_cal):
        feb = 29
    if year == 1918:
        feb = feb - 13
    #It is sure that 256th day will lie in the month of september
    # Sum the total days in that year till august    
    days_till_august = 31 + feb + 31 + 30 + 31 + 30 + 31 + 31
    # Subtract the total days till august from 256 to get the day in september
    day_in_sep = 256 - days_till_august
    print("{}.{}.{}".format(day_in_sep, '09', year))

#call the method
get_date(2019)