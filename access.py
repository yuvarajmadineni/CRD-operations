import operations as x

#importing the main file("code" is the name of the file I have used) as a library 


x.create("Yuvi",42)
#to create a key with key_name,value given and with no time-to-live property


x.create("source",98,4200) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("Yuvi")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("source")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("Yuvi",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("Yuvi",55)
#it replaces the initial value of the respective key with new value 

 
x.delete("Yuvi")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
