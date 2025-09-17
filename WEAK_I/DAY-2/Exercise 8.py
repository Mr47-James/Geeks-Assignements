data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

WrongList = []
Correct_Answers = 0
Incorrect_Answers = 0   # fixed spelling (was Inorrect_Answers)
Global_Score = 0

def asker():
    global Correct_Answers, Incorrect_Answers, WrongList, Global_Score
    for Ques in data:
        x = input(Ques["question"] + " ").strip()
        if x == Ques["answer"].lower():
            Correct_Answers += 1
            print(f"\nCongratulations your answer is correct\n{Ques['answer']}")
        else:
            Incorrect_Answers += 1
            print(f"\nYour answer is not correct: {x}\n{Ques['answer']}")
            WrongList.append(x)

    Global_Score = Correct_Answers * 100 / len(data)
    informer()

def informer():
    global Correct_Answers, Incorrect_Answers, Global_Score, WrongList
    print(f"Correct_Answers: {Correct_Answers}")
    print(f"Incorrect_Answers: {Incorrect_Answers}")
    print(f"Global_Score: {Global_Score}\n")
          
    if Correct_Answers > Incorrect_Answers:
        for i in WrongList:
            print(f"\n{i}")   # fixed undefined Ques + strip misuse
        print("(+++++You WIN+++++)\n")
    elif Correct_Answers < Incorrect_Answers:
        for i in WrongList:
            print(f"\n{i}")
        print("(-----You LOOSE-----)\n")
    elif Correct_Answers == Incorrect_Answers:
        for i in WrongList:
            print(f"\n{i}")
        print("(-----Nicely Done-----)\n")
        Q = input("Do you want to play again (Y/N): ").strip().lower()
        if Q == "y":
            asker()
        elif Q == "n":
            return
    else:
        pass

asker()
