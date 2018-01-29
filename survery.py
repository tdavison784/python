#!/usr/bin/python
class AnonymousServery():
    """Collect anonymous answers to a survery question"""

    def __init__(self, question):
        """Store a question, and prepare a response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the end user the survey question"""
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        """Show the answers from the survey"""
        print("Survey results:")
        for response in self.responses:
            print("-", response)