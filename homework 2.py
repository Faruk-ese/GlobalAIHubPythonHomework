#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = input("Please enter your first name:")
b = input("Please enter your last name:")
c = int(input("Please enter your age:"))
d = int(input("Please enter your date of birth:"))
liste = [a,b,c,d]
for i in liste:
    print("""\nthe first element of list is {} \nthe second element of list is {} \nthe third element of list is {} \nthe fourth element of list is {}
    
    """.format(liste[0],liste[1],liste[2],liste[3]))
    
if (c > 18):
    print("You can go out to the street.")
else:
    print("You can't go out because it's too dangerous.")


# In[ ]:




