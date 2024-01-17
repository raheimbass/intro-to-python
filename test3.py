


def say_hello(name, age):
    print("Hi " + name + ", so you are " + str(age) + " years old")
    # F string
    print(f"Hi {name}, so you are {age} years old")


def format_address(street, number, city, zip):
    print(f"Please return to street: {street} #{number}; city: {city}, zip: {zip}")


def list_1():
    names = ["Tyrell", "Gerardo", "Raheim", "Morris",]
    print(names)

    # count the elements
    print(len(names)) # len = length of the list or string 

    # add elements to list
    names.append("Sergio")
    print(names)


    names.remove("Sergio")
    print(names)


    # four loop
    for name in names:
        print(name)

def get_total():
    prices = [123, 234, 45, 12, 84, 123, 672, 787, 173, 51, 687, 146, 613, 6, 135]

    for price in prices:
        print(price)

    # A) print each price on a line
    # B) sum all the prices 
    total = 0
    for price in prices:
        print(price)
        total = total + price

    print(f"The total is: {total}")

def test_list_3():
    student_ages = [20, 29, 53, 65, 27, 35, 51, 45, 74, 46, 27, 20, 32, 47, 33, 27]

    # A): how many students are there?
    # B): print ages greater than 30 years old
    print(len(student_ages))
    for age in student_ages:
        if age > 30:
            print(age)




# solve this:
say_hello("John", 25) # Hi John, so you are 25 years old
say_hello("Jane", 31) # Hi Jane, so you are 31 years old


# hw is investigate python string formatting 


print("--------------")

# solve this:
format_address("evergreen", 25, "Springfield", 92384)
# Please return to street: evergreen #25; city: Springfield, zip: 92384

list_1()

print("-----------")
get_total()

print("-----------")
test_list_3()

