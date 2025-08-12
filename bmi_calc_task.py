def calculate_bmi(weight_kg, height_cm):
    if height_cm <= 0:
        return None  # Avoid division by zero
    bmi = weight_kg / ((height_cm / 100) ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi is None:
        return "Invalid input for height."
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25<= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in centimeters (cm): "))

        bmi_value = calculate_bmi(weight, height)
        bmi_interpretation = interpret_bmi(bmi_value)

        if bmi_value is not None:
            print(f"\nYour BMI is: {bmi_value:.2f}")
        print(f"Interpretation: {bmi_interpretation}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")