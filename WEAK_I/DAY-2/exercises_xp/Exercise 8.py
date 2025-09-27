data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def run_quiz():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ").strip()

        if user_answer.lower() == item["answer"].lower():
            print("✅ Correct!")
            correct += 1
        else:
            print("❌ Wrong!")
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })

    show_results(correct, incorrect, wrong_answers)


def show_results(correct, incorrect, wrong_answers):
    print("\n--- QUIZ RESULTS ---")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

    if wrong_answers:
        print("\nHere are the questions you missed:")
        for w in wrong_answers:
            print(f"- {w['question']}")
            print(f"  Your answer: {w['your_answer']}")
            print(f"  Correct answer: {w['correct_answer']}\n")


    if incorrect > 3:
        play_again = input("You had more than 3 wrong answers 😬. Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            run_quiz()
        else:
            print("Thanks for playing!")
    else:
        print("Great job, you did well! 🌟")



run_quiz()
