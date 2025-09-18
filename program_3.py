##
# Code by Parker Jolly
# Made with VS Code
# 9/18/2025
##

def weight_conversion(weight):
    # Calculate the shipping charge.
    
    if weight <= 2:
        shippingCost = 1.50
    elif weight <= 6:
        shippingCost = 3.00
    elif weight <= 10:
        shippingCost = 4.00
    elif weight > 10:
        shippingCost = 4.75
    else:
        shippingCost = "That's not a weight"

    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
