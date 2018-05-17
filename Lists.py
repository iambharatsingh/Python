#LISTS

from __future__ import print_function 

grocery_list = ["Juice", "Onions", "Potatoes", "Bananas", "Pickels"]

print("First Item is", grocery_list[0])

print("grocery_list[1:3]", grocery_list[1:3])

print("grocery_list[3:]", grocery_list[3:])

print("grocery_list[3:]", grocery_list[:3])

print("grocery_list[-1]", grocery_list[-1])

print("grocery_list[-1:3]", grocery_list[1:-2])

print("grocery_list[-4:4]", grocery_list[-4:4])

#CHANGING VALUES

grocery_list[0] = "GREEN JUICE"

other_events = ["WASH CAR", "PICK UP KIDS", "CASH CHECK"]

to_do_list = [other_events, grocery_list]

# print(to_do_list)

print(to_do_list[0][2])

#APPEND ITEM TO END

grocery_list.append("Tomatoes")

#Inserting at Specific Index

grocery_list.insert(2, "Chicken")

#grocery_list.remove(grocery_list[0])

grocery_list.remove("GREEN JUICE")

grocery_list.sort()

grocery_list.reverse()

del grocery_list[0]

print(grocery_list)

# appending lists
 
to_do_list_2 = other_events + grocery_list

#PRINTING LENGTH

print(len(to_do_list_2))

#MAX AND MIN

print(max(to_do_list_2))

print(min(to_do_list_2))
