"""
This program will show users what percentage of parking spots are available in the selected parking lot at the time they enter. 
They will be asked if they want to see the information of the parking lot they are currently in or find a new parking lot. 
If they choose a current parking lot, they will be prompted to enter a time and parking lot number.
Then the user will be prompted to enter Number of percentage, If they choose Number then they will be given how many parking spots are left.
If they chose Percentage then it will print the sentence “There is a --% chance you will find a parking spot in the parking lot --” . 

If the user wants a new parking spot they will be prompted to enter a time and then display a list of the parking lots available. 
Then the user will be prompted to enter a parking lot number. 
This will give the user how many parking spots are available in that particular parking lot. 
If they want to know another parkinglot’s information then they can enter another parking lot number and it will display the information of that particular parking lot. 
This loop will repeat four times. 

"""



print("Check current parking lot or find new parkinglot?")
answer=raw_input()
if answer==("current parking lot"):
    print("Enter Parkinglot Number:")
    Parkinglot=input()
    print("Enter Time, Hour only:")
    Time=input()
    print("Which information do you want, number of parking spots avaible, precentage chance of finding a parking spot?")
    information=raw_input()
    if information == ("Number"):
        print("there are", Parkinglot*Time, "parking spots availbe in parkinglot", Parkinglot)
    if information == ("Percentage"):
     print("there is a", (Time*10/Parkinglot), "percent chance you will find parking" )
if answer==("find new parkinglot"):
    parkinglots=[1,2,3,4,5,6]
    print("Enter Time")
    Time= input()
    print("Parking lots avabile", parkinglots)
    print("enter Parking lot numbers")
    p= input()
    c= p*9/Time
    print ("In parkinglot",p,"there are", c, " spots avaible")
    for parkinglots in range(1,4):
        print("Want to check another parkinginglot? Enter another parkinglot number:")
        q= input()
        t= q*9/Time
        print ("In parkinglot",q,"there are", t, " spots avaible")
