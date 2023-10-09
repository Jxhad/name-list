
while True:  
  userAction = input('enter add, show, edit, delete or exit: ')
  
  if 'add' in userAction:
    todos = userAction[4:]
    with open('info.txt', 'r') as file:
     mylist = file.readlines()
    mylist.append(todos)
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
    
      
