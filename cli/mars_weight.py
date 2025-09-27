def calculate_weight(earth_weight, factor):
    return earth_weight * factor

def main():
    print("Mars Weight Calculator (CLI)")
    earth = input("Enter your weight on Earth in kilograms (e.g., 72.5): ")

    try:
        earth_weight = float(earth)
        if earth_weight <= 0:
            raise ValueError("Weight must be positive.")
    except ValueError:
        print("Invalid input. Please enter a positive number like 72.5")
        return

    factors = {
        "Moon": 0.165,
        "Mars": 0.38,
        "ISS": 0.90
    }

    for body, f in factors.items():
        print(f"Your weight on {body}: {earth_weight * f:.2f} kg")

if __name__ == "__main__":
    main()
