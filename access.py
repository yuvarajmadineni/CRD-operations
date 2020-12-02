import operations as x



x.create("Yuvi",42)



x.create("source",98,4200) 



x.read("Yuvi")



x.read("source")



x.create("Yuvi",50)



x.modify("Yuvi",55)


 
x.delete("Yuvi")


#we can access these using multiple threads like
'''t1=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()'''
