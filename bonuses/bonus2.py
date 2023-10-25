
password = input("enter the new password:")

result = []

if len(password) >= 8:
  result.append(True)
else:
  result.append(False)
      
  digit = False
for i in password:
 if i.isdigit():
   digit = True

result.append(digit)

upper = False 
      
for i in password:
 if i.isupper():
     upper = True
     
result.append(upper)



if all(result) == True:
     print(all(result))
     print(result)
     print("Strong password")
 
else:
    print(result)
    print('weak ahh password')