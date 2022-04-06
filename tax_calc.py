# The app will:
#Ask the user to input a subtotal.
#Calculate the tax owed using some (hard-coded) tax rate. This can be whatever you want, like 0.25.
#Print out a message with the amount of tax owed.
#Print out another message with the total owed including tax.


subtotal = input("What is the total?")
taxRate = 0.25
taxAmount = subtotal * taxRate
total = subtotal + taxAmount

print("Tax owing is $" + str(taxAmount))

print("Total including tax is $" + str(total))
