"""
Structured English- switch to structured english branch 
"""



"""
Pseudo Code: 
Check current parking lot? Or Find a new lot?

Check current parking lot:
Enter time: 2pm 
Enter Lot #: 6
Number of parking spots: or Percentage of spots:
Number of parking spots: There are 20 spots available at 2pm in parking lot 6.
Percentage of parking spots: There is a 10% chance of finding a parking spot at 2pm in parking lot 6.

Find a new lot?
Enter lot #: 4
Enter time: 6pm
Number of parking spots: or Percentage of spots:
Number of parking spots: There are 45 spots available at 6pm in parking lot 4.
Percentage of parking spots: There is a 60% chance of finding a parking spot at 6pm in parking lot 4. 

Want to check another lot? 
Yes? Or No?
Yes: Enters loop
No: End loop 

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
