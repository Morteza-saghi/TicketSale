class ticket:
    allavailableTickets = list()

    def dbConstructor(self):  # to Add the First imput of init function to the DataBase

        temp = dict()
        if self.howmany != 0:
            for i, j in self.availableTickets.items():
                temp.update({i: j})
        ticket.allavailableTickets.append(temp)

    def __init__(self, date, fromA, desA, howmany):
        self.date = date
        self.fromA = fromA
        self.desA = desA
        self.howmany = howmany
        self.availableTickets = {"date": self.date, "from": self.fromA,
                                 "to": self.desA, "howmany": self.howmany}
        ticket.dbConstructor(self)

    def showallticket(self):
        return ticket.allavailableTickets

    def addTikcet(self):  # after a instance of object is made they can use this function to add any other ticket they want
        temp = dict()
        for i in self.availableTickets.keys():
            a = input(f"Please Enter {i} :")
            temp[i] = a
            temp.update({i: a})
        temp["howmany"] = int(temp["howmany"])
        ticket.allavailableTickets.append(temp)


class user(ticket):
    allavailableTickets = ticket.allavailableTickets

    def __init__(self, name, username):
        self.username = username
        self.name = name

    def showallticket(self):
        return user.allavailableTickets

    def buyTicket(self):  # users can buy ticket with this fucntion
        print(user.showallticket(self))
        chosenTicket = int(input('Which ticket Do you want ?Enter int '))
        print(
            f"you chose this {ticket.allavailableTickets[chosenTicket]} ticket ")
        sureInput = input("Are You Sure?Enter y or n ")
        if sureInput == "y":
            ticket.allavailableTickets[chosenTicket]["howmany"] -= 1
            print("Done!")
            # after user is sure of hes purchase number of that ticket decrease by one
        else:
            print("You Have Aborted Your Purchas")


a = ticket(2022, "japan", "newyork", 2)
mori = user("mori", "mori_mcr")

# a.addTikcet()
# print(mori.buyTicket())
# # print(mori.showallticket())
# mori.buyTicket()
