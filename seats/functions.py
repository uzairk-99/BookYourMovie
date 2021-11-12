
from seats import database



def set_seating(r,c):
    '''r is the number of rows \n c is the number of columns'''
    for i in range(r):
        seats = []
        for j in range(c):
            seats.append('S')
        database.seating.append(seats)

    if r*c<=60:
        database.Total_Income=r*c*10
    else:
        uh=r//2
        lh=r-uh
        database.Total_Income=(uh*c*10)+(lh*c*8)



def calculate_price(r,c,br):
    '''r is the number of rows \n c is the number of columns \n br is the row of the ticket to be booked'''
    if r*c <= 60:
        return int(10)
    else:
        if br <= (r//2):
            return int(10)
        else:
            return int(8)


def book_ticket(r,c):
    '''r is the number of rows \n c is the number of columns'''
    try:
        a_temp=int(input('Enter the Row: '))
        if a_temp<r:
            ro=a_temp
        else:
            print('please enter a valid row')
            book_ticket(r,c)
    except:
        print('please enter a valid number')
        book_ticket(r,c)

    try:
        a_temp=int(input('Enter the Column: '))
        if a_temp<c:
            co=a_temp
        else:
            print('please enter a valid column')
            book_ticket(r,c)
    except:
        print('please enter a valid number')
        book_ticket(r,c)

    if database.seating[ro-1][co-1]=='B':
        print('\n That seat is already booked,\nPlease choose another seat. \n ')
        book_ticket(r,c)
    else:
        ticket_price=calculate_price(r,c,ro)
        ans=input('Price of your ticket is '+'$ '+str(ticket_price)+' type yes to continue booking.')
        if ans.lower()=='yes':
            name=input('Enter Your Name : ')
            gender=input('Enter Your Gender : ')
            age=input('Enter Your Age : ')
            phone=input('Enter Your Phone no. : ')
            booked_temp=database.Seats(name,gender,age,phone,ticket_price)
            database.booked[(ro,co)]=booked_temp
            database.seating[ro-1][co-1]='B'
            database.current_income+=ticket_price
            database.tickets_booked+=1
            print('\n \n \n Booked Successfully.\n \n \n')
        else:
            return

def Seat_map(r,c):
    for x in range(r+1):
        for y in range(c+1):
            if x==0:
                print(y, " ", end="")
            else:
                if y==0:
                    print(x, " ", end="")
                else:
                    print(database.seating[x-1][y-1], " ", end="")
        print("\n")


def info(row,column):
    try:
        check=database.booked[(row,column)]
        print('Name: '+check.name)
        print('Gender: '+check.gender)
        print('Age: '+check.age)
        print('Ticket Phone no. : '+check.phone)
        print('Ticket Price: '+str(check.price)+'\n \n')

    except:
        print('\n Either the entered seat is not valid or not booked \n')
