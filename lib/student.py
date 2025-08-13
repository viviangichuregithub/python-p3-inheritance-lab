#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Start with an empty list

    def learn(self, knowledge_string):
        # Add the given string to the student's knowledge list
        self.knowledge.append(knowledge_string)
