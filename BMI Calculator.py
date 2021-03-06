# Practice
# BMI Calculator using Coditional Statements

print("Find out your Body Mass Index")
name = input("What's your name? ")
weight_kg = int(input("Weight(kg): "))
height_m = int(input("Height(m): "))

bmi = weight_kg / (height_m ** 2)


if bmi > 25:
  print(f"{name}, your body mass index is {bmi}, therefore you are overweight.")
else: 
  print(f"{name}, your body mass index is {bmi}, therefore you are normal")

#In making this BMI i use i named give the variables weight and height with a value of input that will ask the users weight and height, and it is is nested inside integer so that it would give a value of integer, and not string,

#Next, I created a variable 'bmi' where the height and weight will be calculated... it will calculated by division, where weight in kg will be divided into height in m squared.

#Lastly, if the calculation is done, there is an if and else conditions that will tell the user of what the results is. The first condition, is, if the users bmi is more than 25 then the user is OVERWEIGHT, and else or otherwise, the user is NORMAL.

#BMI Calculator using FUNCTIONS and CONDITIONS

name = "Cj"
weight_kg = 90
height_m = 3

def bmi_calculator(name, weight_kg, height_m):
  bmi = weight_kg / (height_m ** 2)
  print(bmi)
  if bmi > 25:
    return name + " is overweight"
  else: 
    return name + " is not overweight"

result = bmi_calculator(name, weight_kg, height_m)
print(result)


#The first thing I did here is I created a variable for name, weight in kg, and height in m.... 
#Next, I defined a function bmi_calculator where its values are names, weight_kg, and height_m... and nested the bmi formula in it, where weight_kg should be divided by height_m squared
#Next, I created a conditional statements if and else, where if the bmi is greater than 25 it should return the person is overweight, and else or otherwise the person is not overweight
#lastly, i created a variable -- result, that calls the function-- bmi_function,  to get the results and print it to the terminal.

