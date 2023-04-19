#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# Formula used is: BMI = (weight in pounds x 703) / height in inches x height in inches)

# In[12]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name + ", you are underweight.")
    if(BMI <= 24.9):
        print(name + ", you are normal weight.")
    elif(BMI <= 29.9):
        print(name + ", you are overweight.")
    elif(BMI <= 34.9):
        print(name + ", you are obsese.")
    elif(BMI <= 39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Enter Valid Input")

