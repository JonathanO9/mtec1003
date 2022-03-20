import sys
print("BMI: Body Mass Index Calculator");
userWeight = input("Enter your weight (in pounds): ")
userHeight = input("Enter your height (in inches): ")

# BMI Formula: (703 * float(userWeight)) / (pow(float(userWeight), 2))
myBMI = (703 * float(userWeight)) / (pow(float(userWeight), 2))
myBMI = round(myBMI, 2)
print("Your body mass index (BMI) is" + str(myBMI)+ "%")