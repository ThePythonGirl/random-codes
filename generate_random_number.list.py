#set range
import random

# function to search a number in the llist
def search(num, l):
  if num in li:
    return True
  else:
    return False

# function to generate a random list
def generate_list(start, stop, quantity):
  return [random.randrange(start, stop, 1) for i in range(quantity)]


start = int(input("Enter the limit start: "))
stop = int(input("Enter the limit stop: "))
quantity = int(input("Enter the quantity: "))


li = generate_list(start, stop, quantity)

print(li)

# write a program to search a number from the list

num = int(input("Enter a number to search: "))

if search(num, li):
  print('Number Found')
else:
  print('Number not found')