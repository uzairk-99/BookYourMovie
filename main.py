from seats import database
from seats import functions
print("Welcome to Bookmymovie.com")
rows = int(input("\n Enter number of rows:"))
columns = int(input("\n Enter the number of seats in each row:"))
functions.set_seating(rows,columns)


n=0
while n!=5:
    print('\n Please enter the respective number \n 1. Show the Seating \n 2. Book a ticket \n 3. Show Statistics \n 4. Show booked ticket info \n 5. Exit \n')
    n=int(input())
    if n==1:
        functions.Seat_map(rows,columns)
    elif n==2:
        functions.book_ticket(rows,columns)
        
        
    elif n==3:
        print("Number of ticket's purchased: "+str(database.tickets_booked))
        print("Percentage of ticket's booked: "+str(round(((database.tickets_booked)/(rows*columns))*100 , 2))+" %")
        print("Current Income: "+"$ "+str(database.current_income))
        print("Total Income : "+"$ "+str(database.Total_Income))

    elif n==4:
        try:
            i=int(input('Enter row: '))
            j=int(input('Enter column: '))
        except:
            print('Please enter a valid number')

        functions.info(i,j)

        