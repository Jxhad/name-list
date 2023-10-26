<<<<<<< HEAD

from functions import getNames, storeNames, forLoop
        

while True:  
  userAction = input('enter add, show, edit, delete or exit: ')
  
  if userAction.startswith('add'):
    todos = userAction[4:]
    mylist = getNames()
    mylist.append(todos + '\n')
    storeNames(mylist)
     
  elif 'show' in userAction:
     mylist = getNames()
     forLoop(mylist) 
      
  elif 'edit' in userAction:
    try:
      mylist = getNames()
      forLoop(mylist)
      number = int(input('please enter the number in the list: ')) 
      number-=1
      print(mylist[number])
      editname = input('please enter the username change:')
      mylist[number] = editname + '\n'
      storeNames(mylist)
      print(mylist)
    except IndexError:
      print('the number doesnt exist') 
  elif 'delete' in userAction:
    try:
     number= input('please enter what number you want to delete:')
     mylist = getNames()
     number = int(number)
     number-=1
     mylist.pop(number)
     storeNames(mylist)
    except IndexError:
      print('the number you entered doesnt exist')
       
  elif   'exit' in userAction:
    break
  
  else:
    print("please write the right function!")
  
       

print("bye")
    
      
=======

while True:  
  userAction = input('enter add, show, edit, delete or exit: ')
  
  if 'add' in userAction:
    name = userAction[4:]
    with open('info.txt', 'r') as file:
     mylist = file.readlines()
    mylist.append(name)
    with open('info.txt', 'a') as file:
     file.writelines(mylist)
     break
     
  if 'show' in userAction:
     with open('info.txt' , 'r') as file:
      mylist = file.readlines()
     for index, item in enumerate(mylist):
      item = item.strip('\n')
      index+=1
      row = f"{index}-{item}"
      print(row)
      
  if 'edit' in userAction:
     number = input('please enter the number in the list: ') 
     number = int(number)
     number-=1
     print(mylist[number])
     with open('info.txt', 'r') as file:
      file.readlines()
     editname = input('please enter the username change:')
     mylist[number] = editname
     with open('info.txt', 'a') as file:
      file.writelines(mylist)
     print(mylist)
     
  if 'delete' in userAction:
     number= input('please enter what number you want to delete:')
     with open('info.txt', 'r') as file:
      mylist = file.readlines()
     number = int(number)
     number-=1
     mylist.pop(number)
     with open('info.txt', 'w') as file:
      file.writelines(mylist)
     
  if 'exit' in userAction:
    break
  
  else:
    print("please write the right function!")
  
       

print("bye")
    
      
>>>>>>> a4bb3ad703a92aec6d1a290082ce87f39f671489
