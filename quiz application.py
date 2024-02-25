# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:52:20 2024

@author: Rakesh
"""

import random

# Define questions and answers
questions = {
    "What is the capital of France?": ["Berlin", "Paris", "Madrid", "Rome"],
    "Which planet is known as the Red Planet?": ["Mars", "Venus", "Jupiter", "Saturn"],
    "What is the largest mammal in the world?": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"]
}

# Shuffle the order of questions
question_keys = list(questions.keys())
random.shuffle(question_keys)

# Initialize score
score = 0

# Ask questions
for question_key in question_keys:
    # Shuffle answer choices
    choices = questions[question_key]
    random.shuffle(choices)

    # Present the question
    print(question_key)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    # Get user's answer
    user_answer = input("Enter your answer (1-4): ")

    # Check if the answer is correct
    correct_answer = choices.index(questions[question_key][0]) + 1
    if int(user_answer) == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

# Display final score
print(f"Your final score is {score}/{len(questions)}")
