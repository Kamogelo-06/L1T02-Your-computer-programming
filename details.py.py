# Get user information.

name = input("Enter your name:").strip()
age = input("Enter your age:").strip()
house_number = input("Enter your house number:").strip()
street_name = input ("Enter your street name:").strip()

# Format the information into a single sentence.
user_info = f"This is {name}. She is {age} years old and lives at house number {house_number} on {street_name}." 

# Print the formatted sentence.
print(user_info)