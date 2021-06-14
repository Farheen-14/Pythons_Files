#class train - method to book ticket, get status- no. of seats, get fare information of trains running under inidan railway.
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print("**********")
        print(f"The Train name is {self.name}")
        print(f"The availablity of seats are {self.seats}")
        print("**********")
    def fareInfo(self):
        print(f"The charges of the ticket is : Rs.{self.fare}")
    def bookTickets(self):
        if(self.seats>0):
            print(f"Your ticket is booked now ! Your sear number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry! Seats are full now... Please try in Tatkal!!!")
intercity = Train("Rajdhani Express : 14058", 100, 2)
intercity.fareInfo()
intercity.getStatus()
intercity.bookTickets()
intercity.getStatus()
intercity.bookTickets()
intercity.getStatus()
intercity.bookTickets()

