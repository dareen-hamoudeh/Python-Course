
# coding: utf-8

# In[32]:


jordan=["karak", "irbid", "maan", "aqaba", "amman", "zarqa", "jerash", "ajloun", "balqa","tafileh","madaba", "mafraq"]

print("States of Jordan are:")
print(jordan)
print("--------------------------------")
print("States that start with A letter are:")
for jo in range(0,len(jordan)):
    if(jordan[jo][:1]=="a"):
        print(jordan[jo],end=",")
print("\n--------------------------------")    
print("States that contains 5 letters are:")http://localhost:8888/notebooks/Desktop/Python%20Course/week%202/Untitled2.ipynb?kernel_name=python3#
for jo in range(0,len(jordan)):
    if(len(jordan[jo])==5):
        print(jordan[jo],end=",")
        

