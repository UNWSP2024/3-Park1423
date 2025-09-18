##
# Code by Parker Jolly
# Made with VS Code
# 9/18/2025
##

def categorize_age(age):
    
    #check what age we are and then set ageCatagory to the correct string.
    if age < 0:
        ageCategory = "nonexistant"
    elif age <= 1:
        ageCategory = "infant"
    elif age < 13:
        ageCategory = "child"
    elif age >= 13 and age < 20:
        ageCategory = "teenager"
    elif age >= 20 and age <= 120:
        ageCategory = "adult"
    elif age > 120:
        ageCategory = "dinosaur"
    else:
        ageCategory = "That's not an age"

    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)
