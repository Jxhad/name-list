mylist =[]

while True:
    userinput = input('please enter a new member: ') + '\n'
    file = open('members.txt', 'r')
    file.readlines()
    file.close()
    mylist.append(userinput)
    file = open('members.txt' , 'a')
    file.writelines(userinput)
    file.close()
    
    
