print("Welcome to BMI Calculator")
print("-------------------------")
mass = float(input("Enter your mass in kg: "))
height = float(input("Enter your height in m: "))

bmi = mass / height **2

print(f"Your BMI index is : {bmi:.2f}")
