
# coding: utf-8

# In[9]:


tem=int(input("please enter tempreture: "))
t=input("please enter c/f: ")
        
if t=='c':
    result=tem * 9/5 + 32
    print(tem,t," =", result,"F")
else:
    result=(tem - 32) * 5/9
    print(tem,t," =", result,"C")
        

