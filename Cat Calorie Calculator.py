#!/usr/bin/env python
# coding: utf-8

# In[ ]:


source: https://www.petplace.com/article/cats/pet-health/how-to-calculate-your-cats-daily-calorie-intake/


# In[19]:


weight = int(input("Enter your cat's weight in pounds: "))

# Library keys are the cat's weight
# Library values are the calories per day burned based on weight
cal_per_day = {1:39, 2:65, 3:88, 4:110, 5:130, 6:149, 7:167, 8:184, 9:200, 10:218, 11:234, 
              12:250, 13:265, 14:280, 15:295, 16:310, 17:324, 18:339, 19:353, 20:366, 25:433}

neutered = input("Is your cat neutered/spayed? ")

if neutered == "Yes":
    neut_factor = 1.2
elif neutered == "No":
    neut_factor = 1.4
else:
    print("{Please input Yes or No.")

weight_loss = input("Are you trying to have your cat lose weight? ")

if weight_loss == "Yes":
    loss_factor = 0.8
elif weight_loss == "No":
    loss_factor = 1
    weight_gain = input("Are you trying to have your cat gain weight? ")
    if weight_gain == "Yes":
        gain_factor = 1.8
    elif weight_gain == "No":
        gain_factor = 1
    else:
        print("{Please input Yes or No.")
else:
    print("{Please input Yes or No.")
    
young_kitten = input("Is you cat between 0-4 months old? ")

if young_kitten == "Yes":
    young_kitten_factor = 2.5
elif young_kitten == "No":
    young_kitten_factor = 1
    older_kitten = input("Is you cat between 4 months old and 1 year old? ")
    if older_kitten == "Yes":
        older_kitten_factor = 2
    elif older_kitten == "No":
        older_kitten_factor = 1
    else:
        print("{Please input Yes or No.")
else:
    print("{Please input Yes or No.")
    
for key, value in cal_per_day.items():
    if key == weight:
        print("Your cat should intake around " + 
              str(round(value*neut_factor*loss_factor*gain_factor*young_kitten_factor*older_kitten_factor))
             + " calories per day.")

