from Dictonary import Dict

while True:
    search = raw_input("Enter the first name to get the last name.   ")


    keys = Dict.keys()

    if search in keys:
    
        last_name =Dict[search]

        full_name = search + " " + last_name

        print("First name: " + search + "\n" + "Last name: " + last_name + "\n" +
              "Full name: " + full_name +"\n")

