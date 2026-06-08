# BMI Calculator
print("Ready to check your Body Mass Index :)")

try:
    weight_kg = float(input("Enter weight in kilograms: \n"))
    height_m = float(input("Enter height in meters: \n"))
    bmi = weight_kg / height_m**2
    print(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        print("Condition: Underweight")
    elif bmi <= 24.9:
        print("Condition: Normal weight")
    elif bmi <= 29.9:
        print("Condition: Overweight")
    else:
        print("Condition: Obese")
except ValueError:
    print("Error! Please input valid numbers.")
except ZeroDivisionError:
    print("Error! Height must be greater than zero.")