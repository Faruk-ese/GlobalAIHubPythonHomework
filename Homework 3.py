#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
list = ["elma","armut","ayva","mandalina","portakal","muz"]
choosen_data = random.choice(list)
guess_chance = 10
true_list = []
false_list = []

while True:
    index = input("Enter a letter:")
    if (index not in choosen_data):
        if (index in false_list):
            print("Do not use the same letter again.")
        false_list.append(index)
        print("Sorryy.There is no letter like that.")
        guess_chance -= 1
        if (guess_chance == 0):
            print("Your guess chance is over..")
            break
        continue
    elif (index in choosen_data):
        if (index in true_list):
            print("Do not use the same letter again.")
        true_list.append(index)
        if (len(choosen_data) == len(true_list)):
            print("Congratulations,you win the game...")
            print("Choosen data is {}".format(choosen_data))
            break
        else:
            continue

