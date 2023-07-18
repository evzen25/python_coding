quiz = {
    "question1": { 
    "question": "What is the capital of France?",
    "answer": "Paris"
},
"question2": { 
    "question": "What is the capital of Czech Republic?",
    "answer": "Prague"
},
"question3": { 
    "question": "What is the capital of The US?",
    "answer": "Washington D.C."
},
"question4": { 
    "question": "What is the capital of Italy?",
    "answer": "Rome"
},
"question5": { 
    "question": "What is the capital of Germany?",
    "answer": "Berlin"
},
"question6": { 
    "question": "What is the capital of France?",
    "answer": "Paris"
},
"question7": { 
    "question": "What is the capital of Poland?",
    "answer": "Warsaw"
},
"question8": { 
    "question": "What is the capital of Portugal?",
    "answer": "Lisbon"
},
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? " ) 

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))

    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/8 * 100)) + "%")










