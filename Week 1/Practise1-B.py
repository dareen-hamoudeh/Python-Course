
# coding: utf-8

# In[7]:


x=int(input("please enter the value of x:"))
pi=3.14
if x>0:
    if x<100:
        f=pi/2 * x + 3** x
    else:
        f=x
else:
    if x>-25:
        f= 3 * x ** 2 - 1
    elif x>-100:
        f= x ** 4
    else:
        f= -1 * x
        
print("****************")
print("x= ",x,",f(x)=",f)
    
# Answer Of question D:
# the best data type of F(x) is to be float, because the function contains division operation that may result fractions.

