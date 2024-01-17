# imports

# global variables
name = "Raheim"

# functions
def print_header():
    print("-----------")
    print("   Test 2   ")
    print("-----------")
    print("- by: " + name)
    print ("-----------")


def multiply(num1, num2):
    result = num1 * num2
    print("The total is " + str(result))


# plain instructions
#function calls 

print_header()

# exc 3:
# create a multiple function, that receives 2 params
# it does the multiplication and print the result like:
# The total is: XYZ
multiply(8, 78)
multiply(873, 7224548)





# exc 4:
# create a divide function, that receives 2 params

# if the second number is 0, then show an error "Error: Zero division not allowed"

# otherwise, do the division and show the result, like: 

# The total is: XYZ

def divide(num1, num2):
   

    if num2 == 0:
        print("Error: Zero division not allowed")

    else:
         result = num1 / num2
         print("The total is " + str(result))



divide(10, 2) # 5
divide(2, 2) # 1
divide(2, 0) # show an error 



