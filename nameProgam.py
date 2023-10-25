
def getNames():
 with open('info.txt', 'r') as file_local:
     mylist_local = file_local.readlines()
 return mylist_local


def storeNames():
 with open('info.txt', 'w') as file_local:
     file_local.writelines(mylist) 
     return mylist



def forLoop():
  for index, item in enumerate(mylist):
        item = item.strip('\n')
        index+=1
        row = f"{index}-{item}"
        print(row)
  return 
        
     
while True:  
  userAction = input('enter add, show, edit, delete or exit: ')
  
  if userAction.startswith('add'):
    todos = userAction[4:]
    mylist = getNames()
    mylist.append(todos + '\n')
    storeNames()
     
  elif 'show' in userAction:
     mylist = getNames()
     forLoop()
      
  elif 'edit' in userAction:
    try:
      mylist = getNames()
      forLoop()
      number = int(input('please enter the number in the list: ')) 
      number-=1
      print(mylist[number])
      editname = input('please enter the username change:')
      mylist[number] = editname + '\n'
      storeNames()
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
     storeNames()
    except IndexError:
      print('the number you entered doesnt exist')
       
  elif   'exit' in userAction:
    break
  
  else:
    print("please write the right function!")
  
       

print("bye")
    
      
