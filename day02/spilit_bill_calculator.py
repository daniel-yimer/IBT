# bill spiliter with tip
# number of people 
# total bill price
# tip in %

#  make the names loop
#

namesOfCustomers =[]


totalPrice = float(input ("enter the toal price of the bill: "))
numberOfPeople = int(input("the number of bill to be spilit by: "))
for i in range(numberOfPeople):
    customerName=input("Enter the customer name: ")
    namesOfCustomers.append(customerName)

tip =  int(input("enter the amount of tip you want to give in percent: "))

def spilit_bill_calculator(totalPrice , numberOfPeople, tip):
    eachPrice = (totalPrice + (totalPrice * (tip * 1/100)))/numberOfPeople
    return eachPrice

price = spilit_bill_calculator(totalPrice , numberOfPeople, tip)

print("The Total bill spilited between customers")

for i in namesOfCustomers:
    print (f"\n {i} Your total bill is {price} ETB")
