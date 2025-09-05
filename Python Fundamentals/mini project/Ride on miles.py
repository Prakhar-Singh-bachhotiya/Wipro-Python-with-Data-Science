# 1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination

def vehicle(miles):
    ride=''
    if miles<3:
        ride='Bicycle'
    elif miles<300:
        ride='Motor-cycle'
    else:
        ride='Super-Car'
    
    return f'I suggest {ride} to your destination'


dist=int(input('Enter Distance You want to Travel (Must be greater than 0):'))
print(vehicle(dist))



# 2.	Let's assume you are planning to use your python skills to build an App for Mobile.
# You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
# Write a python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How much days can I operate one server with $918?

cost_per_hour=0.51
cost_per_day=cost_per_hour*24
cost_per_week=cost_per_day*7
cost_per_month=cost_per_day*30
capital=918
days=918//cost_per_day
choice=int(input('''1.How much does it cost to operate one server per day?
2.How much does it cost to operate one server per week?
3.How much does it cost to operate one server per month?
4.How much days can I operate one server with $918?
Enter your Choice(1-4):'''))

if choice==1:
    print(f'cost to operate one server per day = {cost_per_day}')
if choice==2:
    print(f'cost to operate one server per week = {cost_per_week}')
if choice==3:
    print(f'cost to operate one server per month = {cost_per_month}')
if choice==4:
    print(f'days I can operate one server with $918 = {days}')
