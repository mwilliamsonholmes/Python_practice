#Your task is to build an app that takes a bill total, tip amount, and number of people as input; and outputs how much each person should pay. 

#The app will:

#Ask for a total dollar amount
#Ask for the percentage tip
#Ask for the number of people splitting the bill
#Use those numbers to calculate the amount that each person owes, printing it out to the terminal, along with the overall total

subtotal = input("What is the total? ")

tip = float(input("What percent would you like to tip? "))

percent = float(tip / 100)

groupSize = input("How many people are splitting this bill? ")
total = (percent * subtotal) + subtotal

perPerson = total / groupSize
print("Each person should pay $" + str(perPerson))
