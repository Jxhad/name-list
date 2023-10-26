

def getNames():
 with open('info.txt', 'r') as file_local:
     mylist_local = file_local.readlines()
 return mylist_local


def storeNames(mylist_arg):
 with open('info.txt', 'w') as file_local:
     file_local.writelines(mylist_arg) 
     



def forLoop(mylist_arg):
  for index, item in enumerate(mylist_arg):
        item = item.strip('\n')
        index+=1
        row = f"{index}-{item}"
        print(row)
  return 