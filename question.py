# -------------------------------------------------------------------------------
# Name:        question.py
# Purpose:
#
# Author:      OnlyChads
#
# Created:     16/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

import random

class Question:
    """object holds the question text and 4 answers, 
        Remember to put the correct answers FIRST
    """

    def __init__(self, q_text, a1_text, a2_text, a3_text, a4_text, img_parameter):
        self.q_text = q_text
        self.a1_text = a1_text
        self.a2_text = a2_text
        self.a3_text = a3_text
        self.a4_text = a4_text
        self.img_parameter = img_parameter
      

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

    def get_img_parameter(self):
        return self.img_parameter

    def get_randomize_answers(self):
        """
        Returns:
            array[4]: question in random order
        """
        answers_list = [self.a1_text, self.a2_text, self.a3_text, self.a4_text]
        random.shuffle(answers_list)
        return answers_list

    def is_answer_correct(self, answer):
        """function checks if the answer is correct

        Args:
            answer (text): the text from the answer button

        Returns:
            boolean: True if the answer is correct, False if not
        """
        if answer == self.a1_text:
            return True
        else:
            return False
