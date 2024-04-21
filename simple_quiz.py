# Quiz Game in Python

def run_quiz():
    # List of questions for the quiz
    # Each question is a dictionary with the question text and the correct answer
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the capital of Germany?", "answer": "Berlin"},
        {"question": "What is the capital of Italy?", "answer": "Rome"},
        {"question": "What is the capital of Spain?", "answer": "Madrid"}
    ]

    # Initialize score counter
    score = 0

    # Iterate through each question in the list
    for question in questions:
        # Print the question
        print(question["question"])
        # Get user input for the answer
        user_answer = input("Enter your answer: ")
        
        # Check if the user's answer is correct
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong! The correct answer is " + question["answer"])

    # Print the final score
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

# Run the quiz function if this script is executed
if __name__ == "__main__":
    run_quiz()
