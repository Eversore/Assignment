#!/usr/bin/env python
# coding: utf-8
1.
# In[1]:


msg="Regret requires age and wisdom"
print(msg)


# 2.

# In[18]:


print('\033[1m' + 'Leonardo da Vinci Once Said:"Learning never exhausts mind"' + '\033[1m')

3.
# In[20]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

4.
# In[29]:


num=True
while bool(num):
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")  

5.
# In[28]:


ch = True
while bool(ch):
    ch = input("Enter a character: ")

    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
     or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")

6.
# In[16]:


height = float(input("Input your height in cm: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round((weight / (height * height))*10000, 2))


# In[10]:


friends=['Wahaj','Usman','Yousf','Abdullah']
print(friends[1])


# In[13]:


friends=['Wahaj','Usman','Yousf','Abdullah']
print(friends[0])

7.
# In[1]:


guests = ['Omama', 'Zaki', 'Anas']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

8.
# In[5]:


Dishes=["Biryani","Qurma","Kunna","Mutton Shahi Raan","Mutton Ribs","Behari Bottti","Dahaga Kabab","Ice Cream Ckae","Gulab Jaman"]

print(Dishes[0:3])
print(Dishes[3:6])
print(Dishes[6:])


# In[25]:


food=["Biryani","Qurma","Kunna","Mutton Shahi Raan","Mutton Ribs","Behari Bottti","Dahaga Kabab","Ice Cream Ckae","Gulab Jaman"]
favorite_food=["Pizza","Burger","Pasta","Namkeen boti","full Motton Rost","Qeema","Karhai","Ice cream","labe sheereen"]

food.append("Pomegranate Juice")
print(food)

print("\n")

favorite_food.append("Orange juice")
print(favorite_food)

favorite_food=["Pizza"]

for pizza in favorite_food:
    print("Pizza")
    
print("\n")

for pizza in favorite_food:
    print("I really love " + pizza + " megretta!")


print("\n")

food=["Pomegranate Juice"]

for pizza in food:
    print("")
    


for pizza in food:
    print("I really love " + "Pomegranate" + " Juice!")




# In[ ]:




