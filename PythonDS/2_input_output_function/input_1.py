# Input Function - input()

# Taking input for the institution's name and location
company_name = input("Enter the Institute name: ")  # Input for the name
location = input("Enter the location of the Institute: ")  # Input for the location

# Printing the entered values
print("\nInstitution name is", company_name)  # Displaying the name
print("Institution is located at", location)  # Displaying the location

# A formatted output showing both details in a single sentence
print(f"\n{company_name} is an IT finishing school located at {location}")  # Using f-string for clean formatting
