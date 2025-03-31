print ("Welcome to hotel management system")
print ("----------------------------------")

print ("01 - New booking")
print ("02 - View booking list")
print ("03 - Check-in guest")
print ("04 - Check-out guest")
print ("05 - Exit")
choice = int(input("Enter your choice: "))

if choice == 1:
    name = input("please enter guest name: ")
    contact = int(input("guest contact number: "))
    nic = input("enter NIC number: ")
    days = int(input ("enter nights: "))
    roomPrice = 2000

    roomType = int(input("enter room type (1 - A/C, 2 - non A/C : )"))
    if roomType == 1:
        roomPrice += 1500
    elif roomType == 2:
        roomPrice == roomPrice
    
    else:
        print("Please choose correct room type")

    foods = input("do you need foods service (1 - yes, 2 - no): ")
    if foods == 1:
        roomPrice += 3000
    elif foods == 2:
        roomPrice == roomPrice
    else:
        print("please choice correct option")

    finalPrice = roomPrice + days 
    print(f"{name} your final bill is {finalPrice}")