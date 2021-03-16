# -------------------------------------------------------------------------------
# Name:        question.py
# Purpose:
#
# Author:      OnlyChads
#
# Created:     16/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------


class Question:
    """object holds the question text and 4 answers, 
        Remember to put the correct answers FIRST
    """

    def __init__(self, q_text, a1_text, a2_text, a3_text, a4_text):
        self.q_text = q_text
        self.a1_text = a1_text
        self.a2_text = a2_text
        self.a3_text = a3_text
        self.a4_text = a4_text

    def get_q_text(self):
        return self.q_text

    def get_a1_text(self):
        return self.a1_text

    def get_a2_text(self):
        return self.a2_text

    def get_a3_text(self):
        return self.a3_text

    def get_a4_text(self):
        return self.a4_text
