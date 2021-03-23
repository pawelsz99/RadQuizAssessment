# -------------------------------------------------------------------------------
# Name:        chemistry.py
# Purpose:     responsible for chemistry quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window, Picture

from question import Question
import random

img_dict = {0:"imgs/img_blank.PNG", 7: "imgs/chem_q7.PNG", 9:"imgs/chem_q9.PNG", 10:"imgs/chem_q10.PNG"}

list_questions = {
    1: Question("The term ‘renal’ refers to which organs?", "Kidney", "Liver", "Stomach", "Appendix", ""),
    2: Question("Botany is the study of what life form?", "Plants", "Animals", "Insects ", "Humans", ""),
    3: Question("What is the human body’s largest organ?", "Skin", "Liver", "Brain", "Spleen", ""),
    4: Question("How many bones does an adult human have?", "206", "198", "176", "234", ""),
    5: Question("What year was the first animal cloned?", "1640", "2015", "1996", "Has not happened yet", ""),
    6: Question("Which food substance helps move waste through the body?", "Fibre", "Protein", "Carbohydrates", "Sugar", ""),
    7: Question("Which part of body is this? ", "Liver", "Spleen", "Bladder", "Gall", ""),
    8: Question("Ecosystem consists of …", "Biotic community", " Plants & Animals ", "Diffrent Species", "Various Insects", ""),
    9: Question("Which organism would most likely come between the grass and the snake? ", "rabbit", "wheat", "coyote", "clover","" ),
    10: Question("Which system is represented on picture ? ", "Digestive", "Eco System ", " Planetary ", " Elemntary System", "")
}

questions_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
order_counter = 0
# this will be used in randomizing questions order


class Chemistry:
    def __init__(self, app):
        self.score = 0
        self.app = app

        # after each start of the quiz window,
        # reset the counter and randomize the question order
        global order_counter
        order_counter = 0
        global questions_order
        random.shuffle(questions_order)

        #-----------------------------Chemistry Window--------------------------------#

        self.chemistry_window = Window(
            self.app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; chemistry_container_1 = Image container, chemistry_container_2 = Question container, chemistry_container_3 = filler container, chemistry_container_4 = upper answer button container, chemistry_container_5 = filler container, chemistry_container_6 = lower answer button container, chemistry_container_7 = bottom container with score and question
        chemistry_container_1 = Box(
            self.chemistry_window, width=700, height=250, border=2)
        chemistry_container_2 = Box(
            self.chemistry_window, width=700, height=100, border=2)
        chemistry_container_3 = Box(
            self.chemistry_window, width=700, height=25, border=2)
        chemistry_container_4 = Box(
            self.chemistry_window, width=700, height=100, border=2)
        chemistry_container_5 = Box(
            self.chemistry_window, width=700, height=25, border=2)
        chemistry_container_6 = Box(
            self.chemistry_window, width=700, height=100, border=2)
        chemistry_container_7 = Box(
            self.chemistry_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
        chemistry_filler_box_1 = Box(chemistry_container_4,
                                     align="left",
                                     width=150,
                                     height=100)
        chemistry_filler_box_2 = Box(chemistry_container_4,
                                     align="right",
                                     width=150,
                                     height=100)
        chemistry_button_1 = Box(chemistry_container_4,
                                 align="left",
                                 width=180,
                                 height=80)
        chemistry_button_2 = Box(chemistry_container_4,
                                 align="right",
                                 width=180,
                                 height=80)

        # containers where the lower buttons are positioned
        chemistry_filler_box_3 = Box(chemistry_container_6,
                                     align="left",
                                     width=150,
                                     height=100)
        chemistry_filler_box_4 = Box(chemistry_container_6,
                                     align="right",
                                     width=150,
                                     height=100)
        chemistry_button_3 = Box(chemistry_container_6,
                                 align="left",
                                 width=180,
                                 height=80)
        chemistry_button_4 = Box(chemistry_container_6,
                                 align="right",
                                 width=180,
                                 height=80)

        # bottom section with score and questions
        chemistry_bottom = Box(chemistry_container_7,
                               align="bottom",
                               width=700,
                               height=50)
        chemistry_bottom_question = Box(chemistry_bottom,
                                        align="right",
                                        width=200,
                                        height=25)
        chemistry_bottom_score = Box(chemistry_bottom,
                                     align="left",
                                     width=100,
                                     height=25)

        #-----------------------------Chemistry Widgets------------------------------#

        # Question Image
        self.chemistry_image = Picture(chemistry_container_1, 
                                width=400,
                                height=200,  
                                image=img_dict.get(0)         
                                )

        # Question Text
        self.chemistry_question = Text(chemistry_container_2,
                                       text="Question",
                                       width=100,
                                       height=100)
        self.chemistry_question.bg = "#FF8108"

        # Score & Question Num
        self.chemistry_question_number = Text(chemistry_bottom_question,
                                              text="Question Num: 1/10")
        self.chemistry_question_score = Text(
            chemistry_bottom_score, text="Score: 0")

        # Answer Buttons
        self.chemistry_answer_1 = PushButton(chemistry_button_1,
                                             align="left",
                                             width=100,
                                             height=70,
                                             command=self.check_a1)
        self.chemistry_answer_1.bg = "#54C03D"
        self.chemistry_answer_1.font = "sans-serif"
        self.chemistry_answer_2 = PushButton(chemistry_button_2,
                                             align="right",
                                             width=100,
                                             height=70,
                                             command=self.check_a2)
        self.chemistry_answer_2.bg = "#2D73A9"
        self.chemistry_answer_2.font = "sans-serif"
        self.chemistry_answer_3 = PushButton(chemistry_button_3,
                                             align="left",
                                             width=100,
                                             height=70,
                                             command=self.check_a3)
        self.chemistry_answer_3.bg = "#DB4692"
        self.chemistry_answer_3.font = "sans-serif"
        self.chemistry_answer_4 = PushButton(chemistry_button_4,
                                             align="right",
                                             width=100,
                                             height=70,
                                             command=self.check_a4)
        self.chemistry_answer_4.bg = "#FFFA13"
        self.chemistry_answer_4.font = "sans-serif"

        self.next_question()

    def next_question(self):
        global order_counter

        # ----------------------- check if end of the quiz ----------------------------- #
        if order_counter >= 10:
            # display the final score
            # maybe something that looks better than popup?
            self.chemistry_window.info(
                "Congratulation", "Your score: " + str(self.score)+" /10")

            # in the later stages remember to pass info
            # if the user has passed the test
            # to unlock the ultimate test
            self.chemistry_window.destroy()

        # ------------------- update question and answers --------------------- #
        q = list_questions[questions_order[order_counter]].get_q_text()

        # Code below will retrive the current question number and it's image
        questionNum = questions_order[order_counter]
        if questionNum == 7:
          self.chemistry_image.value= img_dict.get(7)
        elif questionNum == 9:
          self.chemistry_image.value= img_dict.get(9)
        elif questionNum == 10:
          self.chemistry_image.value= img_dict.get(10)
        else:
          self.chemistry_image.value= img_dict.get(0)


        # randomizing the answers
        answers = list_questions[questions_order[order_counter]
                                 ].get_randomize_answers()
        a1 = answers[0]
        a2 = answers[1]
        a3 = answers[2]
        a4 = answers[3]

        self.chemistry_question.value = q
        self.chemistry_answer_1.text = a1
        self.chemistry_answer_2.text = a2
        self.chemistry_answer_3.text = a3
        self.chemistry_answer_4.text = a4

        # set the counter for the next question
        order_counter += 1

        # ----------------------- update score and question number --------------------- #

        self.chemistry_question_score.value = "Score: " + str(self.score)
        self.chemistry_question_number.value = "Question Num: " + \
            str(order_counter) + "/10"

    def check_a1(self):
        """this function is called after pressing answer button 1
            it checks if the answer was correct and continue to the next question 
        """
        answer = self.chemistry_answer_1.text
        print(answer)

        # the counter is already set for the next question
        # so we need to reduce it by one
        if list_questions[questions_order[order_counter - 1]].is_answer_correct(answer):
            self.score += 1

        # after checking the answer we can move to the next question
        self.next_question()

    def check_a2(self):
        """this function is called after pressing answer button 2
            it checks if the answer was correct and continue to the next question 
        """
        answer = self.chemistry_answer_2.text
        print(answer)

        # the counter is already set for the next question
        # so we need to reduce it by one
        if list_questions[questions_order[order_counter - 1]].is_answer_correct(answer):
            self.score += 1

        # after checking the answer we can move to the next question
        self.next_question()

    def check_a3(self):
        """this function is called after pressing answer button 3
            it checks if the answer was correct and continue to the next question 
        """
        answer = self.chemistry_answer_3.text
        print(answer)

        # the counter is already set for the next question
        # so we need to reduce it by one
        if list_questions[questions_order[order_counter - 1]].is_answer_correct(answer):
            self.score += 1

        # after checking the answer we can move to the next question
        self.next_question()

    def check_a4(self):
        """this function is called after pressing answer button 4
            it checks if the answer was correct and continue to the next question 
        """
        answer = self.chemistry_answer_4.text
        print(answer)

        # the counter is already set for the next question
        # so we need to reduce it by one
        if list_questions[questions_order[order_counter - 1]].is_answer_correct(answer):
            self.score += 1

        # after checking the answer we can move to the next question
        self.next_question()
