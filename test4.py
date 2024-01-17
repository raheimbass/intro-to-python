
def about_me():
    # dictionary
    me = {
        "first": "Sergion",
        "last": "Inzunza",
        "age": 37
    }

    print(me)




    # read values
    print(me["first"])
    print(me["age"])

    # add new elements
    me["email"] = "sinzunza@sdgku.edu"
    print(me)

    #update existing 
    me["age"] = 98

    # check if key exists, before reading
    if "preferred_color" in me:
        me["preferred_color"] 

def test_address():
    location = {
        "street": "Evergreen",
        "number": 27,
        "city": "Springfield",
        "state": "CA",
        "zip": "92101"
    }

    # A) print: street #, city
    print(location["street"])
    print(location["number"])
    print(location["city"])

    print(f'{location["street"]} #{location["number"]}, {location["city"]}')


about_me()
test_address()