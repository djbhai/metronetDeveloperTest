# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:32:33 2019

@author: User
"""

import json
import re
records=[]
name_sorted_records=[]
names = []
digits= ['0','1','2','3','4','5','6','7','8','9']
with open("Web Developer Test","rb") as fp:
    data=json.load(fp)

for item in data:
    names.append(item['fullName'])
    records.append(item)

name_sorting = [i[0] for i in sorted(enumerate(names),key=lambda x:x[1])]
for item in name_sorting:
    name_sorted_records.append(records[item])


for item in name_sorted_records:
    email_invalid = True
    telephone_invalid = False
    both_invalid = True
    email=item['emailAddress']
    telephone = item['phoneNumber']
    name=item['fullName']
    emailparts= email.split('@')
    if(len(emailparts)==2):
        countAt =0
        for c in email:
            if(c=='@'):
                countAt+=1
        if(countAt==1):
            email_invalid=False
            both_invalid=False
    for d in telephone:
        if(d not in digits):
            if(d!='-'):
                if(d!=' '):
                    telephone_invalid=True
                    break
        
    print(name)
    if(both_invalid==True):
        print("Email and Telephone Number are invalid \n")
    elif(telephone_invalid==True):
        print("Telephone Number is invalid \n")
    elif(email_invalid==True):
        print("Email Address is invalid \n")
    else:
        print("Valid \n")
    
