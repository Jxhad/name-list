
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
    
      
