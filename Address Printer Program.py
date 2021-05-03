print ("Address Printer Program")

def printAddress(name, streetAdd, town, state, postCode, country):
    print(name)
    print(streetAdd)
    print(town)
    print(state)
    print(postCode)
    print(country)

# To variables
ToPost = print("_______To:_______")
ToName = input("Name: ")
ToStreetAdd = input("Street Address: ")
ToTown = input("Town/Suburb: ")
ToState = input("State: ")
ToPostCode = int(input("PostCode: "))
ToCountry = input("Country: ")
print("")

# From variables
FromPost = print("______From:______")
FromName = input("Name: ")
FromStreetAdd = input("Street Address: ")
FromTown = input("Town/Suburb: ")
FromState = input("State: ")
FromPostCode = int(input("PostCode: "))
FromCountry = input("Country: ")
print("")

print ("Your Shipping Labels: ","\n")
print ("To: ","\n", ToName,"\n" , ToStreetAdd,"\n" , ToTown,"\n" , ToPostCode,"\n" , ToState,"\n" , ToCountry, "\n")

print ("From: ","\n", FromName,"\n" , FromStreetAdd,"\n" , FromTown,"\n" , FromPostCode,"\n" , FromState,"\n" , FromCountry, "\n")
                    
