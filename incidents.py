# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 7:30:16 2021

@author: clara
"""
import pandas as pd

while True:
    try:
        inputfile=input('Name of the file: ')
        file=open(inputfile)
    except FileNotFoundError:
        print('Please enter the name of the file you wish to transform.')
        
        continue
    else:
        print('Processing file ',inputfile)
        break          


while True:
    outputfile=input('Name of the outputfile: ')
    
    if (outputfile==""):
        print('Please enter the name of the output file.\nNote that if it does not exist, we will create a new one with that name.')
    else:
        break


file=open(inputfile)

#file=open("incidentesRaw.csv")
lst=file.read()
lst=lst.splitlines()


nlst=[]
for i in lst:
    k=len(i)
    if(k>1 and k<7):
        k=k/2
        nlst.append(i[int(k):]) 
print("Please find below the list of incidents per day, you may want to review if the following data makes sense to you:\n",nlst, "\nProcessing the list into a column... Please wait.")      

#file=open("NEWincidentesRaw.csv", "w") 
file=open(outputfile, "a")    
for i in nlst:
    #row=i.split(", ")
    file.write(i)
    file.write("\n")
    #print(i)


file.close()   
print("Dear Lady, your file has been generated with name <<",outputfile, ">> successfully.")
