import threading

import time
d={} #creating dictionary for storing data
def read(key):
    if key in d:
        val=d[key]
        if val[1]!=0:
            if time.time()<val[1]: #comparing the present time with expiry time
                si=str(key)+':'+str(val[0]) #to return value in form of json object
                return si
            else:
                print('error:time-to-live of',key,'has expired')
        else:
            si=str(key)+':'+str(val[0])
            return si
    else:
        print('error: The given key does not exist in database')
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")

#I have an additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
