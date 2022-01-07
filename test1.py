
# venv/Scripts/activate to activate virtual enviroment in Windows
#attach framework to python so dont need to repeat common steps required, Flask
# create and call function that prints your name
# execute the script
#js array = py list

def print_name():
    print("Mark Courtright")

def list1():
    print("Working with lists (not arrays)")

    names=['John', 'Juan']
    #add values to the list instead of push as in js, append
    names.append("Smokey")
    names.append("Joe")

    #get values print at index 0, 3
    print(names[0])
    print(names[3])
    # prints list ["",""]
    print(names)

    #loops for dont need to assign to let variable, and then execute for(let i= 0; )
    for name in names:
        print(name)

def list2():
    #print 30 times
    print("-" * 30)
    nums = [123,456,123,3456,6,689,23,6,8,7887,123,46,3,89,12,9,9,565,8,33,1,-200,23]

    #1 print sum of all nums with for loop
    sum = 0
    count=0
    smallest = nums[0]

    for num in nums:
        sum += num
        if (num<50):
            print(num)
            count += 1
        if (smallest > num):
            smallest = num
    print(sum)
    # f or F to format string, otherwise "there" + str(count) + "here"
    # python strings formating
    print(f"there are: {count} nums lower than 50")
    print(f"the smallest number: {smallest}")

    

def dict1():
    print("Dictionary tests 1...")

    me = {
        "name": "Mark",
        "last": "Courtright",
        "age": 56,
        "hobbies": [],
        "address": {
            "street": "Jimray",
            "number": 123,
            "city": "Mishawaka"
        }
    }

    print(me["name"])
    print(me["name"] + " " + me["last"])
    #print(me["iq"]) gives "KeyError: 'iq' ", with specifics on what to correct, DNE

    me["age"] = 99

    me["email"] = "smoke@gmail.com"

    print(me)

    address = me["address"]
    print(f"{address['number']} {address['steet']} {address['city']}") #use single quote inside



print_name()

list1()
list2()

dict1()

#api's from google or yahoo (sports and food)