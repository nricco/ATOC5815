"""
ATOC-5815 homework 2 Due 9/9/2022

Practice python flow control and functions following the
discussions at https://www.pythoncheatsheet.org/
"""

print("\nProblem 1")
print("---------")
print("Twinkle, twinkle, little star \n \t How I wonder what you are! \n" \
      "\t\t Up above the world so high, \n \t\t Like a diamond in the sky. \n" \
      "Twinkle, twinkle little star \n \t How I wonder what you are")
    
print("\nProblem 2")
print("---------")
def getListAndTuples(*argv):
    myList = []
    for arg in argv:
        myList.append(arg)
    
    myTuple = tuple(myList)
    print("My List:",myList)
    print("My Tuple:",myTuple)

getListAndTuples(3,5,7,23)
print("\nProblem 3")
print("---------")
def getFileExtension(a_filename):
     fileExt = a_filename.split('.',1)[1]
     print(fileExt)
     
getFileExtension('abc.java')

print("\nProblem 4")
print("---------")
def findValue(a_val, a_list):
    result = ''
    for i in a_list:
        if i==a_val:
            result = True
            break
        else: 
            result = False
    return result

A,B=3,[1,5,8,3] 
print(A, '->', B, ':', findValue(A,B))
C,D=-1,[1,5,8,3]
print(C, '->', D, ':', findValue(C,D))

print("\nProblem 5")
print("---------")
def concatenateDict(*argv):
    bigDict = {}
    for arg in argv:
        bigDict.update(arg)
    print("Expected Results:",bigDict)
dic1 ={1:10,2:20}
dic2 ={3:30,4:40}
dic3 ={5:50,6:60}

concatenateDict(dic1,dic2,dic3)

print("\nProblem 6")
print("---------")
def addDict(a_dict1, a_dict2):
    for k,v in a_dict2.items():
        if(findValue(k,list(a_dict1.keys()))):
            a_dict1.update({k:v+a_dict1[k]})
        else:
            a_dict1.update({k:v})
    
    print(a_dict1)

d1 ={'a':100,'b':200,'c':300}
d2 ={'a':300,'b':200,'d':400}
addDict(d1,d2)

print("\nProblem 7")
print("---------")
def myStats(a_list):
    nX = len(a_list)
    X = sorted(a_list)
    
    # median = middle value (check in odd or even)
    if nX % 2 != 0:
        medX = X[int(nX/2)+1]
    else: 
        medX = (X[int(nX/2)] + X[int(nX/2)-1])/2
    
    sumX = 0.0
    maxX = 0.0 
    minX = 0.0 
    stdX = 0.0 
    
    for x in X:
        xprev = x
        if x > xprev: maxX = x
        if x < xprev: minX = x
        
        sumX+=x 
        
    meanX = sumX / nX
        
    # standard dev = sqrt(sum(x-mean)/n)
    for y in X: 
        stdX = ((y-meanX/nX))**(1/2)
        
    return maxX, minX, meanX, medX, stdX
X = [1,5,3,2,1,6]

print('Array:', X)
print('(Max, Min, Mean, Median, Stdev)')
print(myStats(X))

print("\nProblem 8")
print("---------")
import os
from src.text_read import textRead

def countWords(a_list):
    wordsDict={}
    sorted_dict_rev = {}
    # Find words from the list in the new dictionary and update the key and values
    for w in a_list:
        if(findValue(w,list(wordsDict.keys()))):
            wordsDict.update({w:wordsDict[w]+1})
        else:
            wordsDict.update({w:1})
    
    # Sort the dictionary's values and reverse the order
    sorted_values_rev = sorted(wordsDict.values(), reverse=True)
    
    # Populate a sorted dictionary by matching the sorted values to keys 
    for i in sorted_values_rev:
        for j in wordsDict.keys():
            if wordsDict[j] == i:
                sorted_dict_rev[j] = wordsDict[j]
    
    # Print the 10 most occuring words 
    for n in range(10):
        print('The word,', "\"",list(sorted_dict_rev.keys())[n], "\"", \
              ' occurred ', list(sorted_dict_rev.values())[n], ' times.')
        
dirtop = os.getcwd()
print(dirtop)
dirdat = os.path.join(dirtop,'\data')
listOfWords = textRead(dirtop + "\data\climate.txt")
countWords(listOfWords)
