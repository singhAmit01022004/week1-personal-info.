# Name: Amit Kumar Singh
# Project: Personal Information Storage & Display
# Description: A program to store static data and collect user input to display a profile.

def main():
    # --- Welcome Message ---
    print("========================================")
    print("   Welcome to the Profile Builder!   ")
    print("========================================\n")

    # --- Store Static Information ---
    # Storing basic details in appropriate data types
    name = "Aman Kumar"          # String
    age = 21                     # Integer
    city = "Ramgarh"             # String
    hobby = "Cooking"            # String

    # --- Get User Input & Validation ---
    # We use a simple while loop to make sure the user doesn't leave it blank
    
    favorite_food = ""
    while not favorite_food.strip():
        favorite_food = input("What is your favorite food? ")
        if not favorite_food.strip():
            print("Oops! Food cannot be empty. Please try again.")

    favorite_color = ""
    while not favorite_color.strip():
        favorite_color = input("What is your favorite color? ")
        if not favorite_color.strip():
            print("Please enter a color to proceed.")

    # --- Calculations ---
    # Converting age from years to months
    age_in_months = age * 12

    # --- Display Information with String Formatting ---
    print("\n" + "-"*30)
    print("      USER PROFILE SUMMARY      ")
    print("-"*30)

    # Using f-strings for clean output and string methods like .title() and .upper()
    print(f"Name:           {name.upper()}")
    print(f"Age:            {age} years old ({age_in_months} months)")
    print(f"Location:       {city.title()}")
    print(f"Main Hobby:     {hobby}")
    print(f"Favorite Food:  {favorite_food.capitalize()}")
    print(f"Favorite Color: {favorite_color.lower()}")
    
    print("-"*30)

    # --- Goodbye Message ---
    print("\nThank you for using the Profile Builder. Have a great day!")

if __name__ == "__main__":
    main()