# -------------------------------------------------------------------------------
# Name:        mathematics.py
# Purpose:     responsible for maths quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window, TextBox, Picture
from question import Question
# from PIL import Image, ImageFont
import random


list_questions = {
    1: Question("An empty container weights 120g. \nWhen 50 lollipops were put in it the weight changed to 870g.‏‏‎‏‏‎‏‎ \nWhat is the weight of one lollipop?", "15 Grams", "10 grams", "5 grams", "20 grams", ""),
    2: Question("Anne is going to Malta.\nHow many euros will she get for £150 \nwhen the exchange rate is 1.18 euros to a pound?", "177 euros ", "178 euros", "176 euros", "175 euros", ""),
    3: Question("A car travels at a constant speed of 63 mph for 20 minutes. \nHow far does the car travel in this time?", "21 miles ", "20 miles", "3 miles", "19 miles", "imgs/math_q3.png"),
    4: Question("A liquid is warmed from –3C to +5C.\nBy how many degrees has its temperature risen?", "By 8 ", "By 4", "By -8", "By -4", ""),
    5: Question("Some water has been added to this measuring jar.\nHow much more water is needed to fill the jar to 1.5 litres? ", "0.6 litres", "0.7 litres", "0.5 litres", "1 liter", "imgs/math_q5.PNG"),
    6: Question("The number of pupils in each year group in a secondary school was recorded \nand this pie chart drawn.\nThere are 1200 pupils in the school.\n\nHow many pupils were there in S5/6? ", "200 pupils", "150 pupils", "210 pupils", "190 pupils", "imgs/math_q6.PNG"),
    7: Question("The number of people using a gym each day was recorded for a week \nand this compound bar chart was drawn.\nWho has used the gym the most? Male of Female? ", "Female ", "Male", "", "", "imgs/math_q7.PNG"),
    8: Question("Sally scored the following marks in three of her tests. Maths: 25 out of 40\nEnglish: 32 out of 50\nScience: 38 out of 60\nGeography: 39 out of 70. In which subject did she do best in?", "English ", "Maths", "Science", "Geography", ""),
    9: Question("Calculate the perimeter of the shape. ", "52 cm", "50 cm", "54 cm", "51 cm", "imgs/math_q9.PNG"),
    10: Question("How many pounds will you get by increasing £80 by 60%", "128£", "126£", "122£", "125£", "")
}

questions_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
order_counter = 0
# this will be used in randomizing questions order


class Mathematics:
    def __init__(self, app):
        self.score = 0
        app = app

        # after each start of the quiz window,
        # reset the counter and randomize the question order
        global order_counter
        order_counter = 0
        global questions_order
        random.shuffle(questions_order)

        #------------------------------Mathematics Window-----------------------------------#

        self.math_window = Window(app, width=850, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; mathematics_container_1 = Image container, mathematics_container_2 = Question container, mathematics_container_3 = filler container, mathematics_container_4 = upper answer button container, mathematics_container_5 = filler container, mathematics_container_6 = lower answer button container, mathematics_container_7 = bottom container with score and question
        mathematics_container_1 = Box(
            self.math_window, width=850, height=250)
        mathematics_container_2 = Box(
            self.math_window, width=850, height=100, border=2)
        mathematics_container_3 = Box(
            self.math_window, width=700, height=25)
        mathematics_container_4 = Box(
            self.math_window, width=700, height=100)
        mathematics_container_5 = Box(
            self.math_window, width=700, height=25)
        mathematics_container_6 = Box(
            self.math_window, width=700, height=100)
        mathematics_container_7 = Box(
            self.math_window, width=700, height=100)

        # containers where the upper buttons are positioned
        math_filler_box_1 = Box(mathematics_container_4,
                                align="left",
                                width=150,
                                height=100)
        math_filler_box_2 = Box(mathematics_container_4,
                                align="right",
                                width=150,
                                height=100)
        mathematics_button_1 = Box(mathematics_container_4,
                                   align="left",
                                   width=180,
                                   height=80)
        mathematics_button_2 = Box(mathematics_container_4,
                                   align="right",
                                   width=180,
                                   height=80)

        # containers where the lower buttons are positioned
        math_filler_box_3 = Box(mathematics_container_6,
                                align="left",
                                width=150,
                                height=100)
        math_filler_box_4 = Box(mathematics_container_6,
                                align="right",
                                width=150,
                                height=100)
        mathematics_button_3 = Box(mathematics_container_6,
                                   align="left",
                                   width=180,
                                   height=80)
        mathematics_button_4 = Box(mathematics_container_6,
                                   align="right",
                                   width=180,
                                   height=80)

        # bottom section with score and questions
        mathematics_bottom = Box(mathematics_container_7,
                                 align="bottom",
                                 width=700,
                                 height=50)
        mathematics_bottom_question = Box(mathematics_bottom,
                                          align="right",
                                          width=200,
                                          height=25)
        mathematics_bottom_score = Box(mathematics_bottom,
                                       align="left",
                                       width=100,
                                       height=25)

        #-----------------------------Mathematics Widgets------------------------------#‎‎‏‏‎‏‏‎

        # Question Image
        self.math_image = Picture(mathematics_container_1,
                                  width=850,
                                  height=250)

        # Question Text
        self.math_question = TextBox(mathematics_container_2,
                                     text="Question",
                                     width=100,
                                     height=100, multiline=True)
        self.math_question.bg = "#FF8108"
        self.math_question.font = "sans-serif"
        self.math_question.text_size = 12

        # Score & Question Num
        self.math_question_number = Text(mathematics_bottom_question,
                                         text="Question Num: 1/10")
        self.math_question_score = Text(
            mathematics_bottom_score, text="Score: 0")

        # Answer Buttons
        self.math_answer_1 = PushButton(mathematics_button_1,
                                        align="left",
                                        width=100,
                                        height=70,
                                        command=self.check_a1)
        self.math_answer_1.bg = "#54C03D"
        self.math_answer_1.font = "sans-serif"
        self.math_answer_2 = PushButton(mathematics_button_2,
                                        align="right",
                                        width=100,
                                        height=70,
                                        command=self.check_a2)
        self.math_answer_2.bg = "#2D73A9"
        self.math_answer_2.font = "sans-serif"
        self.math_answer_3 = PushButton(mathematics_button_3,
                                        align="left",
                                        width=100,
                                        height=70,
                                        command=self.check_a3)
        self.math_answer_3.bg = "#DB4692"
        self.math_answer_3.font = "sans-serif"
        self.math_answer_4 = PushButton(mathematics_button_4,
                                        align="right",
                                        width=100,
                                        height=70,
                                        command=self.check_a4)
        self.math_answer_4.bg = "#FFFA13"
        self.math_answer_4.font = "sans-serif"

        self.next_question()

    def next_question(self):
        global order_counter

        # ----------------------- check if end of the quiz ----------------------------- #
        if order_counter >= 10:
            # display the final score
            # maybe something that looks better than popup?
            self.math_window.info(
                "Congratulation", "Your score: " + str(self.score)+" /10")

            # in the later stages remember to pass info
            # if the user has passed the test
            # to unlock the ultimate test
            self.math_window.destroy()

        try:

            # ------------------- update question and answers --------------------- #
            q = list_questions[questions_order[order_counter]].get_q_text()

            # Code below will set an image for the question
            if list_questions[questions_order[order_counter]].get_img_parameter() == "":
                self.math_image.value = "imgs/img_blank.PNG"
            else:
                self.math_image.value = list_questions[questions_order[order_counter]
                                                       ].get_img_parameter()

            self.showAllAnswersButtons()
            # randomizing the answers
            answers = list_questions[questions_order[order_counter]
                                     ].get_randomize_answers()
            a1 = answers[0]
            a2 = answers[1]
            a3 = answers[2]
            a4 = answers[3]

            self.math_question.value = q
            self.math_answer_1.text = a1
            self.math_answer_2.text = a2
            self.math_answer_3.text = a3
            self.math_answer_4.text = a4

            self.hideBlankButtons()

            # set the counter for the next question
            order_counter += 1

            # ----------------------- update score and question number --------------------- #

            self.math_question_score.value = "Score: " + str(self.score)
            self.math_question_number.value = "Question Num: " + \
                str(order_counter) + "/10"
        except IndexError:
            pass

    def check_a1(self):
        """this function is called after pressing answer button 1
            it checks if the answer was correct and continue to the next question 
        """
        answer = self.math_answer_1.text
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
        answer = self.math_answer_2.text
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
        answer = self.math_answer_3.text
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
        answer = self.math_answer_4.text
        print(answer)

        # the counter is already set for the next question
        # so we need to reduce it by one
        if list_questions[questions_order[order_counter - 1]].is_answer_correct(answer):
            self.score += 1

        # after checking the answer we can move to the next question
        self.next_question()

    def showAllAnswersButtons(self):
        self.math_answer_1.show()
        self.math_answer_2.show()
        self.math_answer_3.show()
        self.math_answer_4.show()

    def hideBlankButtons(self):
        if self.math_answer_1.text == "":
            self.math_answer_1.hide()
        if self.math_answer_2.text == "":
            self.math_answer_2.hide()
        if self.math_answer_3.text == "":
            self.math_answer_3.hide()
        if self.math_answer_4.text == "":
            self.math_answer_4.hide()
