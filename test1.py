
# comment
name = "Raheim"
last_name = "Bass"
age = 21
price = 12.99
found = True

print(name)
print(last_name)

#math
total = 21 / 21
print(total)


# if 
if age < 100:
    print("Dont worry you are young!")
    print("Inside the if")
    print("me too")

    
print("I'm outside")


# exc 1:
# create an if, if the age is lower than 21,
# show a message like "You can not drink alcohol"

if age < 21:
    print("You can not drink alcohol")

# exc 2:
# if you are 21 and up, print "Fancy a beer?"
    
if age >= 21:
    print("Have a beer on me")



def say_hello():
    print("Hello there!")


#call function
say_hello()
say_hello()
say_hello()


def salute(name):
    print("Hi " + name)

salute("John")
salute("Jane")
salute(name)

def sum(num1, num2):
    result = num1 + num2
    print("The result is " + str(result))




sum(21, 21)
sum(9234, 18393)