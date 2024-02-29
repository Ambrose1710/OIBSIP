#BMI Calculator

weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in meters: '))
BMI = weight/(height**2)
BMI = round(BMI,2)


def BMI_range():
    if BMI >= 25.0:
        return f'Your BMI is {BMI}, you are overweight'
    elif BMI > 18.49 and BMI < 25.0:
        return f" Your BMI is {BMI}, you are within normal range"
    elif BMI < 18.5:
        return f"Your BMI is {BMI}, you are underweight"
    else:
        return f"Your BMI is {BMI}, you are obese"
BMI_Range = BMI_range()

print(BMI_Range)