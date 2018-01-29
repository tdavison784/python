#!/usr/bin/python
from survery import AnonymousServery

# Define a question, and make a survey
question = "What language did you first learn to speak?"

my_survey = AnonymousServery(question)

#Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' to quit at any time.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Show the survey results
print("\nThank you to all that participated. Here are the results:")
my_survey.show_results()