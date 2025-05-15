print("age calculator")

from datetime import datetime

def calculate_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    age = calculate_age(dob_input)

    if age is not None:
        if age < 18:
            print("Under age")
        else:
            print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
