name = "Alex"
destination = "Newyork"
Ticket_price = 5667.34
number_of_ticket = 4
ticket_available = True

print("passenger name:",name)
print("His destination:",destination)
print("price of each ticket:",Ticket_price)
print("Number of ticket:",number_of_ticket)
print("Ticket available:",ticket_available)

print(type(name))
print(type(destination))
print(type(Ticket_price))
print(type(number_of_ticket))
print(type(ticket_available))

Total_cost = Ticket_price * number_of_ticket
discount = 100
final_cost = Total_cost - discount

print("total cost:",Total_cost)
print("discount:",discount)
print("final cost:",final_cost)

print("double ticket cost:",Ticket_price * 2)
print("ticket cost after 20$ increases:",Ticket_price + 20)
print("half ticket cost:",Ticket_price / 2)

print("Is ticket cost under 1000?",Ticket_price < 1000)
print("Are more than 2 tickets booked?",number_of_ticket > 2)
print("Is destination Newyork?",destination == "Newyork")
print("Is final cost more than 2000?",final_cost > 2000)

travel_message = name + " is travelling to " + destination + "."
print("travel message:",travel_message)
print("destination in uppercase:",destination.upper())
print("passenger name in lowercasr:",name.lower())
print("First letter of destination:",destination[0])
print("Lenght of passenger name:",len(name))

morning_ticket_price = 9899
evening_ticket_price = 6587

print("before swapping:")
print("Morning ticket cost:",morning_ticket_price)
print("Evening ticket cost:",evening_ticket_price)

morning_ticket_price,evening_ticket_price = evening_ticket_price,morning_ticket_price

print("After swapping:")
print("Morning ticket cost:",morning_ticket_price)
print("Evening ticket_price:",evening_ticket_price)

print("Travel Ticket Summary")
print("passenger:",name)
print("Destination:",destination)
print("Ticket booked:",number_of_ticket)
print("Final Amount to pay:",final_cost)
print("Booking Confirmed?",ticket_available)
