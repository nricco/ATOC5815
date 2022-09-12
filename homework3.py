# -*- coding: utf-8 -*-
"""
ATOC-5815 homework 3 Due 9/16/2022

HW3 document 
"""
import numpy as np 

print("\nProblem 1")
print("---------")
def fiveIntArray(a_1,a_2,a_3,a_4,a_5):
    return np.array([a_1,a_2,a_3,a_4,a_5],dtype=int)    

x = fiveIntArray(1,2,3.6,4,5.1)
print(x)
X = np.append(x,int(7.8))
print("Appdended:", X)
X_rev = np.flip(X)
print("Reversed:",X_rev)

print("\nProblem 2")
print("---------")
import os

def appendTextFile(a_filepath, a_string):
    print("File:",a_filepath)
    file = open(a_filepath,'a')
    file.write(a_string + "\n")
    file.close()
    with open(a_filepath) as file: 
        print(file.read())
    
dirdat = os.path.abspath(os.path.dirname(__file__) +"\data")
filename = dirdat + "\hw3_prob2.txt"
myString = "Homework#3 problem 2: \nWrite a Python Program to append text to a most wondiferously-beautiful file and display the text."
appendTextFile(filename,myString)

print("\nProblem 3")
print("---------")
def findLongestWord(a_filepath):
    with open(a_filepath) as file:
        filetext = file.read()
        word_list = filetext.split()
        longword = word_list[0]
        
        for word in word_list:    
            #print(word)
            #print(len(word))
            if len(word) > len(longword): longword = word
        
        print(longword, " is the longest word in {}".format(a_filepath))
        
findLongestWord(filename)

print("\nProblem 4")
print("---------")
def generateAZTextFiles(a_path):
    azrange = range(ord('A'),ord('Z')+1)
    
    for letter in azrange:
        file = open(a_path + chr(letter) +".txt",'w')
        file.write("Filename:" + chr(letter) + ".txt \n")
        file.close()
    print("See directory {} for the {} generated files".format(a_path,len(azrange)))

generateAZTextFiles(dirdat + "/prob4/")

print("\nProblem 5")
print("---------")
import datetime as dt 

def parkingFeeCalculator(a_enter, lostTicket='False'):
    fmt = "%m-%d-%Y:%H:%M"
    entry_date = dt.datetime.strptime(a_enter, fmt)
    today_date = dt.datetime.now()
    today_date.strftime("%Y-%m-%d %H:%M")
    date_diff = today_date - entry_date
    days,hours = date_diff.days, int(date_diff.seconds/3600)
    
    if lostTicket==True:
        lost_ticket = 17
    else: 
        lost_ticket = 0
    
    hour_rate = 3
    
    if days < 3:
        day_rate = 24
    else:
        day_rate = 18
    
    if days > 14:
        day_bonus = 0.9
    else:
        day_bonus = 1.0 
        
    total = lost_ticket + hour_rate * hours + day_rate * days * day_bonus
    
    print("Denver Airport Parking Ticket:")
    print("***DO NOT LOSE THIS TICKET***")
    print("-----------------------------")
    print("Entry Date:", entry_date)
    print("Today's Date:",today_date)
    print("Total Time Parked: {} days and {} hours".format(days,hours))
    print("Lost Ticket?:", lostTicket)
    print("------------------------------------------")
    print("Parking Rates:")
    print("Hourly $3 per hour")
    print("Daily* $24 under 3 days")
    print("Daily* $18 more than 3 days")
    print("*10% discount parking longer than 14 days")
    print("Lost ticket fee, $17")
    print("-----------------------------------------")
    print("Total Cost: ${}\n\n".format(total))

# Date String format: M-D-YYYY:HH:MM
parkingFeeCalculator('7-8-2022:14:00')
parkingFeeCalculator('9-3-2022:8:25')
parkingFeeCalculator('9-9-2022:8:25',True)