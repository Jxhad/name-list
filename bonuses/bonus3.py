try:  
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(name + ' is not in the list')    