# -------------------------------------------------------------------------------
# Name:        english.py
# Purpose:     responsible for english quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window

from question import Question

list_questions = {
    1: Question("Can you swim?", "In a pool", "Yes, I can", "Very good", "Butterfly"),
    2: Question("Did he go to work or to school?", "English lesson", "No, he doesn't", "At 3:00 PM", "To work"),
    3: Question("Has your class finished? ", "Yes, it has", "In five minutes", "It's English", "Yes, it done"),
    4: Question("Where is my pen?", "Because it's lost", "On the table", "No, you don't", "Take this"),
    5: Question("Who did you visit?", "I visit my mother", "Yes, I did", "I visited Judy", "I was swimming"),
    6: Question("Shall we go to your place or mine?", "My place", "It is yours", "Yes, we shall", "No, we haven't"),
    7: Question("When will Lucy arrive?", "At 7 PM", "No, she won't", "From France", "Yesterday"),
    8: Question("Who called here so late?", "It's midnight", "It was Ryan", "Yes, I called", "Let's order pizza"),
    9: Question("Do you want to watch a movie?", "At the cinema", "Yes, I watched it", "No, I don't", "Yes, I has"),
    10: Question("Have you done the laundry?", "Yes, I do", "On Wednesday", "No, I haven't", "Tomorrow")
}

questions_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
# this will be used in randomizing questions order


class English:
    def __init__(self, app):
        app = app

        #-----------------------------English Window--------------------------------#

        english_window = Window(app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; english_container_1 = Image container, english_container_2 = Question container, english_container_3 = filler container, english_container_4 = upper answer button container, english_container_5 = filler container, english_container_6 = lower answer button container, english_container_7 = bottom container with score and question
        english_container_1 = Box(
            english_window, width=700, height=250, border=2)
        english_container_2 = Box(
            english_window, width=700, height=100, border=2)
        english_container_3 = Box(
            english_window, width=700, height=25, border=2)
        english_container_4 = Box(
            english_window, width=700, height=100, border=2)
        english_container_5 = Box(
            english_window, width=700, height=25, border=2)
        english_container_6 = Box(
            english_window, width=700, height=100, border=2)
        english_container_7 = Box(
            english_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
        english_filler_box_1 = Box(english_container_4,
                                   align="left",
                                   width=150,
                                   height=100)
        english_filler_box_2 = Box(english_container_4,
                                   align="right",
                                   width=150,
                                   height=100)
        english_button_1 = Box(english_container_4,
                               align="left", width=180, height=80)
        english_button_2 = Box(english_container_4,
                               align="right",
                               width=180,
                               height=80)

        # containers where the lower buttons are positioned
        english_filler_box_3 = Box(english_container_6,
                                   align="left",
                                   width=150,
                                   height=100)
        english_filler_box_4 = Box(english_container_6,
                                   align="right",
                                   width=150,
                                   height=100)
        english_button_3 = Box(english_container_6,
                               align="left", width=180, height=80)
        english_button_4 = Box(english_container_6,
                               align="right",
                               width=180,
                               height=80)

        # bottom section with score and questions
        english_bottom = Box(english_container_7,
                             align="bottom", width=700, height=50)
        english_bottom_question = Box(english_bottom,
                                      align="right",
                                      width=200,
                                      height=25)
        english_bottom_score = Box(
            english_bottom, align="left", width=100, height=25)

        #-----------------------------English Widgets--------------------------------#

        # Question Text
        self.english_question = Text(english_container_2,
                                     text="Question",
                                     width=100,
                                     height=100)
        self.english_question.bg = "#FF8108"

        # Score & Question Num
        self.english_question_number = Text(english_bottom_question,
                                            text="Question Num: 1/10")
        self.english_question_score = Text(
            english_bottom_score, text="Score: 0")

        # Answer Buttons
        self.english_answer_1 = PushButton(english_button_1,
                                           align="left",
                                           width=100,
                                           height=70,
                                           command=self.next_question)
        self.english_answer_1.bg = "#54C03D"
        self.english_answer_1.font = "sans-serif"
        self.english_answer_2 = PushButton(english_button_2,
                                           align="right",
                                           width=100,
                                           height=70,
                                           command=self.next_question)
        self.english_answer_2.bg = "#2D73A9"
        self.english_answer_2.font = "sans-serif"
        self.english_answer_3 = PushButton(english_button_3,
                                           align="left",
                                           width=100,
                                           height=70,
                                           command=self.next_question)
        self.english_answer_3.bg = "#DB4692"
        self.english_answer_3.font = "sans-serif"
        self.english_answer_4 = PushButton(english_button_4,
                                           align="right",
                                           width=100,
                                           height=70,
                                           command=self.next_question)
        self.english_answer_4.bg = "#FFFA13"
        self.english_answer_4.font = "sans-serif"

        self.next_question()

    def next_question(self):
        global counter
        q = list_questions[questions_order[counter]].get_q_text()
        a1 = list_questions[questions_order[counter]].get_a1_text()
        a2 = list_questions[questions_order[counter]].get_a2_text()
        a3 = list_questions[questions_order[counter]].get_a3_text()
        a4 = list_questions[questions_order[counter]].get_a4_text()

        self.english_question.value = q

        self.english_answer_1.text = a1
        self.english_answer_2.text = a2
        self.english_answer_3.text = a3
        self.english_answer_4.text = a4

        counter += 1
