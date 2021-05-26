# -------------------------------------------------------------------------------
# Name:        geography.py
# Purpose:     responsible for geography quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window, Picture

from question import Question
import random


list_questions = {
    1: Question("What does each star on the flag of the United States stand for?", "States", "Ex-Presidents", "Cities", "Universities", ""),
    2: Question("What colour is the spot in the middle of the Japanese flag?", "Red", "White", "Pink", "Colar", ""),
    3: Question("Baku is the capital city of which eastern European country?", "Georgia", "Azerbaijan", "Russia", "Belarus", ""),
    4: Question("In which country is the worlds highest waterfall?", "USA", "UK", "Venezuela", "Australia", ""),
    5: Question("What is the highest mountain in Britain?", "Ben Nevis", "Ben Macdui", "Braeriach", "Aonach Mor", ""),
    6: Question("What is the unit of currency in Spain?", "Pounds", "Euros", "Dollars", "Peseta", ""),
    7: Question("Which country is it? (pic)", "Brazil", "Mexico", "Argentina", "Venezuela", "imgs/geo_q7.PNG"),
    8: Question("What is the name of this ocean? (pic)", "Pacific Ocean", "Arctic Ocean", "Atlantic Ocean", "Indian Ocean", "imgs/geo_q8.PNG"),
    9: Question("Which country has this flag? (pic) ", "Russia", "France", "The Netherlands", "Belgium", "imgs/geo_q9.PNG"),
    10: Question("Where is this building located? (pic)", "Rome, Italy", "Milan, Italy", "Paris, France", "Barcelona, Spain", "imgs/geo_q10.PNG")
}

questions_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
order_counter = 0
# this will be used in randomizing questions order


class Geography:
    def __init__(self, app):
        self.score = 0
        app = app

        # after each start of the quiz window,
        # reset the counter and randomize the question order
        global order_counter
        order_counter = 0
        global questions_order
        random.shuffle(questions_order)

        #-----------------------------Geography Window--------------------------------#

        self.geography_window = Window(
            app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; geography_container_1 = Image container, geography_container_2 = Question container, geography_container_3 = filler container, geography_container_4 = upper answer button container, geography_container_5 = filler container, geography_container_6 = lower answer button container, geography_container_7 = bottom container with score and question
        geography_container_1 = Box(
            self.geography_window, width=700, height=250)
        geography_container_2 = Box(
            self.geography_window, width=700, height=100, border=2)
        geography_container_3 = Box(
            self.geography_window, width=700, height=25)
        geography_container_4 = Box(
            self.geography_window, width=700, height=100)
        geography_container_5 = Box(
            self.geography_window, width=700, height=25)
        geography_container_6 = Box(
            self.geography_window, width=700, height=100)
        geography_container_7 = Box(
            self.geography_window, width=700, height=100)

        # containers where the upper buttons are positioned
        geography_filler_box_1 = Box(geography_container_4,
                                     align="left",
                                     width=150,
                                     height=100)
        geography_filler_box_2 = Box(geography_container_4,
                                     align="right",
                                     width=150,
                                     height=100)
        geography_button_1 = Box(geography_container_4,
                                 align="left",
                                 width=180,
                                 height=80)
        geography_button_2 = Box(geography_container_4,
                                 align="right",
                                 width=180,
                                 height=80)

        # containers where the lower buttons are positioned
        geography_filler_box_3 = Box(geography_container_6,
                                     align="left",
                                     width=150,
                                     height=100)
        geography_filler_box_4 = Box(geography_container_6,
                                     align="right",
                                     width=150,
                                     height=100)
        geography_button_3 = Box(geography_container_6,
                                 align="left",
                                 width=180,
                                 height=80)
        geography_button_4 = Box(geography_container_6,
                                 align="right",
                                 width=180,
                                 height=80)

        # bottom section with score and questions
        geography_bottom = Box(geography_container_7,
                               align="bottom",
                               width=700,
                               height=50)
        geography_bottom_question = Box(geography_bottom,
                                        align="right",
                                        width=200,
                                        height=25)
        geography_bottom_score = Box(geography_bottom,
                                     align="left",
                                     width=100,
                                     height=25)

        #-----------------------------Geography Widgets--------------------------------#

        # Question Image
        self.geography_image = Picture(geography_container_1,
                                       width=700,
                                       height=250)

        # Question Text
        self.geography_question = Text(geography_container_2,
                                       text="Question",
                                       width=100,
                                       height=100)
        self.geography_question.bg = "#FF8108"

        # Score & Question Num
        self.geography_question_number = Text(geography_bottom_question,
                                              text="Question Num: 1/10")
        self.geography_question_score = Text(
            geography_bottom_score, text="Score: 0")

        # Answer Buttons
        self.geography_answer_1 = PushButton(geography_button_1,
                                             align="left",
                                             width=100,
                                             height=70,
                                             command=self.check_a1)
        self.geography_answer_1.bg = "#54C03D"
        self.geography_answer_1.font = "sans-serif"
        self.geography_answer_2 = PushButton(geography_button_2,
                                             align="right",
                                             width=100,
                                             height=70,
                                             command=self.check_a2)
        self.geography_answer_2.bg = "#2D73A9"
        self.geography_answer_2.font = "sans-serif"
        self.geography_answer_3 = PushButton(geography_button_3,
                                             align="left",
                                             width=100,
                                             height=70,
                                             command=self.check_a3)
        self.geography_answer_3.bg = "#DB4692"
        self.geography_answer_3.font = "sans-serif"
        self.geography_answer_4 = PushButton(geography_button_4,
                                             align="right",
                                             width=100,
                                             height=70,
                                             command=self.check_a4)
        self.geography_answer_4.bg = "#FFFA13"
        self.geography_answer_4.font = "sans-serif"

        self.next_question()

    def next_question(self):
        global order_counter

        # ----------------------- check if end of the quiz ----------------------------- #
        if order_counter >= 10:
            # display the final score
            # maybe something that looks better than popup?
            self.geography_window.info(
                "Congratulation", "Your score: " + str(self.score)+" /10")

            # in the later stages remember to pass info
            # if the user has passed the test
            # to unlock the ultimate test
            self.geography_window.destroy()
        try:
          # ------------------- update question and answers --------------------- #

          q = list_questions[questions_order[order_counter]].get_q_text()

          # Code below will set an image for the question
          if list_questions[questions_order[order_counter]].get_img_parameter() == "":
              self.geography_image.value = "imgs/img_blank.PNG"
          else:
              self.geography_image.value = list_questions[questions_order[order_counter]
                                                          ].get_img_parameter()

          # randomizing the answers
          answers = list_questions[questions_order[order_counter]
                                  ].get_randomize_answers()
          a1 = answers[0]
          a2 = answers[1]
          a3 = answers[2]
          a4 = answers[3]

          self.geography_question.value = q
          self.geography_answer_1.text = a1
          self.geography_answer_2.text = a2
          self.geography_answer_3.text = a3
          self.geography_answer_4.text = a4

          # set the counter for the next question
          order_counter += 1

          # ----------------------- update score and question number --------------------- #

          self.geography_question_score.value = "Score: " + str(self.score)
          self.geography_question_number.value = "Question Num: " + \
              str(order_counter) + "/10"
        except IndexError:
            pass

    def check_a1(self):
        """this function is called after pressing answer button 1
            it checks if the answer was correct and continue to the next question 
        """
        answer = self.geography_answer_1.text
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
        answer = self.geography_answer_2.text
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
        answer = self.geography_answer_3.text
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
        answer = self.geography_answer_4.text
        print(answer)

        # the counter is already set for the next question
        # so we need to reduce it by one
        if list_questions[questions_order[order_counter - 1]].is_answer_correct(answer):
            self.score += 1

        # after checking the answer we can move to the next question
        self.next_question()
