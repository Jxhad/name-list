import json

with open("questions.json", 'r') as file:
    content = file.read()
    
data = json.loads(content)

score = 0

for question in (data):
    print(question["questionsText"])
    for index, choice in enumerate(question["choices"]):
        print(index + 1, choice)
        
    userAnswer = input("enter the correct answer: ")
    userAnswer = int(userAnswer)
    
    if userAnswer == question["answer"]:
        print("correct answer!")
        score+=1
     
print("your score is ",score, "/" ,len(data))   