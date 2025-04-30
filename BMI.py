print("---BODY MASS INDEX----")
print("Maintain Weight Stay Healthy")
num1=float(input("Enter Your Weight in KG: "))
num2=float(input("Enter your Height in Meters: "))
BMI=num1/(num2**2)
print(f"Your BMI is:{round(BMI, 2)}")
if BMI<=20:
    print("You are under weight please take healthy diet")
elif BMI<=23:
    print("You have an average BMI")
elif BMI<=25:
    print("You have an ideal weight")
elif BMI>26:
    print("You are over weight please do exercise")



