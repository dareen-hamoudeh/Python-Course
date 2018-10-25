
# coding: utf-8

# In[7]:


def print_prime_numbers(n):
    #  max=int(input("Enter the maximum number: "))
    for num in range(1,n):
        count = 0;
        for i in range(2,num):
            if (num%i==0):
                count=count+1;
                break;
                
        if (count==0 and num!= 1):
            print(num," ")
            

max=int(input("Enter the maximum number: "))
print_prime_numbers(max)

