# -------------------------------------------------------------------------------
# Name:        ultimate.py
# Purpose:     responsible for ultimate quiz (all question combined)
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------


from geography import list_questions as list_q_geo
from mathematics import list_questions as list_q_math
from chemistry import list_questions as list_q_chem
from english import list_questions as list_q_eng
from guizero import App, Text, PushButton, Box, Window, Picture
import pickle
import random

menu_score_disp = 0

list_questions = {}
i = 1
#getting ready the questions 
for x in range(1, 11):
    list_questions[i] = list_q_math[x]
    i += 1

for x in range(1, 11):
    list_questions[i] = list_q_chem[x]
    i += 1

for x in range(1, 11):
    list_questions[i] = list_q_geo[x]
    i += 1

for x in range(1, 11):
    list_questions[i] = list_q_eng[x]
    i += 1

questions_order = []
# create an array [1,2...40]
for x in range(list_questions.__len__()):
    questions_order.append(x+1)
order_counter = 0
# this will be used in randomizing questions order


# dictionary has been created to accomodate score and highscore for this program
get_session_scores = {
                  "highscore": 0,
                  "score": 0   
                  }



class Ultimate:
    def __init__(self, app):
        # score & highscore is being loaded in from a separate file
        start_up = open("startup_vars", "rb")
        get_dict_data = pickle.load(start_up)


        self.score = 0
        self.highscore = get_dict_data.get("highscore")
        app = app

        # after each start of the quiz window,
        # reset the counter and randomize the question order
        global order_counter
        order_counter = 0
        global questions_order
        random.shuffle(questions_order)

        #-----------------------------Ultimate Window--------------------------------#

        self.ultimate_window = Window(app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; ultimate_container_1 = Image container, ultimate_container_2 = Question container, ultimate_container_3 = filler container, ultimate_container_4 = upper answer button container, ultimate_container_5 = filler container, ultimate_container_6 = lower answer button container, ultimate_container_7 = bottom container with score and question
        ultimate_container_1 = Box(
            self.ultimate_window, width=700, height=250, border=2)
        ultimate_container_2 = Box(
            self.ultimate_window, width=700, height=100, border=2)
        ultimate_container_3 = Box(
            self.ultimate_window, width=700, height=25, border=2)
        ultimate_container_4 = Box(
            self.ultimate_window, width=700, height=100, border=2)
        ultimate_container_5 = Box(
            self.ultimate_window, width=700, height=25, border=2)
        ultimate_container_6 = Box(
            self.ultimate_window, width=700, height=100, border=2)
        ultimate_container_7 = Box(
            self.ultimate_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
        ultimate_filler_box_1 = Box(ultimate_container_4,
                                    align="left",
                                    width=150,
                                    height=100)
        ultimate_filler_box_2 = Box(ultimate_container_4,
                                    align="right",
                                    width=150,
                                    height=100)
        ultimate_button_1 = Box(ultimate_container_4,
                                align="left",
                                width=180,
                                height=80)
        ultimate_button_2 = Box(ultimate_container_4,
                                align="right",
                                width=180,
                                height=80)

        # containers where the lower buttons are positioned
        ultimate_filler_box_3 = Box(ultimate_container_6,
                                    align="left",
                                    width=150,
                                    height=100)
        ultimate_filler_box_4 = Box(ultimate_container_6,
                                    align="right",
                                    width=150,
                                    height=100)
        ultimate_button_3 = Box(ultimate_container_6,
                                align="left",
                                width=180,
                                height=80)
        ultimate_button_4 = Box(ultimate_container_6,
                                align="right",
                                width=180,
                                height=80)

        # bottom section with score and questions
        ultimate_bottom = Box(ultimate_container_7,
                              align="bottom",
                              width=700,
                              height=50,
                              border=True)
        ultimate_bottom_question = Box(ultimate_bottom,
                                       align="right",
                                       width=200,
                                       height=25,
                                       )
        ultimate_bottom_score = Box(ultimate_bottom,
                                    align="left",
                                    width=100,
                                    height=25,
                                    )

        ultimate_bottom_highscore = Box(ultimate_bottom, 
                                    width=150,
                                    height=25,
                                    align="left",
                                    )
        
        

        #-----------------------------Ultimate Widgets--------------------------------#

        # Question Image
        self.ultimate_image = Picture(ultimate_container_1,
                                  width=400,
                                  height=200)

        # Question Text
        self.ultimate_question = Text(ultimate_container_2,
                                      text="Question",
                                      width=100,
                                      height=100)
        self.ultimate_question.bg = "#FF8108"

        # Score, High Score & Question Num 
        self.ultimate_question_number = Text(ultimate_bottom_question,
                                             text="Question Num: 1/10")

        self.ultimate_question_score = Text(
            ultimate_bottom_score, text="Score: 0")

        self.high_score_display = Text(ultimate_bottom_highscore,
            text="High Score: " + str(self.highscore),
            align="bottom")
        

        # Answer Buttons
        self.ultimate_answer_1 = PushButton(ultimate_button_1,
                                            align="left",
                                            width=100,
                                            height=70,
                                            command=self.check_a1)
        self.ultimate_answer_1.bg = "#54C03D"
        self.ultimate_answer_1.font = "sans-serif"
        self.ultimate_answer_2 = PushButton(ultimate_button_2,
                                            align="right",
                                            width=100,
                                            height=70,
                                            command=self.check_a2)
        self.ultimate_answer_2.bg = "#2D73A9"
        self.ultimate_answer_2.font = "sans-serif"
        self.ultimate_answer_3 = PushButton(ultimate_button_3,
                                            align="left",
                                            width=100,
                                            height=70,
                                            command=self.check_a3)
        self.ultimate_answer_3.bg = "#DB4692"
        self.ultimate_answer_3.font = "sans-serif"
        self.ultimate_answer_4 = PushButton(ultimate_button_4,
                                            align="right",
                                            width=100,
                                            height=70,
                                            command=self.check_a4)
        self.ultimate_answer_4.bg = "#FFFA13"
        self.ultimate_answer_4.font = "sans-serif"

        self.next_question()

    def next_question(self):
        global order_counter, menu_score_disp

        # ----------------------- check if end of the quiz ----------------------------- #
        if order_counter >= 40:
            # display the final score
            # maybe something that looks better than popup?

            # saves
            get_session_scores["score"] = self.score
            if self.score >= self.highscore:
              self.highscore = self.score
              self.high_score_display.value = "High Score: " + str(self.highscore)

              get_session_scores["highscore"] = self.highscore

            start_up = open("startup_vars", "wb")
            pickle.dump(get_session_scores, start_up)
            start_up.close()

            self.ultimate_window.info(
                "Congratulation", "Your score: " + str(self.score)+" /40")

            menu_score_disp = str(self.score)
            

            # in the later stages remember to pass info
            # if the user has passed the test
            # to unlock the ultimate test
            self.ultimate_window.destroy()
            
        
        try:
          # ------------------- update question and answers --------------------- #
          q = list_questions[questions_order[order_counter]].get_q_text()

          # Code below will set an image for the question
          if list_questions[questions_order[order_counter]].get_img_parameter() == "":
              self.ultimate_image.value = "imgs/img_blank.PNG"
          else:
              self.ultimate_image.value = list_questions[questions_order[order_counter]
                                                    ].get_img_parameter()

          # randomizing the answers
          answers = list_questions[questions_order[order_counter]
                                  ].get_randomize_answers()
          a1 = answers[0]
          a2 = answers[1]
          a3 = answers[2]
          a4 = answers[3]

          self.ultimate_question.value = q
          self.ultimate_answer_1.text = a1
          self.ultimate_answer_2.text = a2
          self.ultimate_answer_3.text = a3
          self.ultimate_answer_4.text = a4

          # set the counter for the next question
          order_counter += 1

          # ----------------------- update score and question number --------------------- #

          self.ultimate_question_score.value = "Score: " + str(self.score)
          self.ultimate_question_number.value = "Question Num: " + \
              str(order_counter) + "/40"
        except IndexError:
            pass
        
        return menu_score_disp

    def check_a1(self):
        """this function is called after pressing answer button 1
            it checks if the answer was correct and continue to the next question 
        """
        answer = self.ultimate_answer_1.text
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
        answer = self.ultimate_answer_2.text
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
        answer = self.ultimate_answer_3.text
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
        answer = self.ultimate_answer_4.text
        print(answer)

        # the counter is already set for the next question
        # so we need to reduce it by one
        if list_questions[questions_order[order_counter - 1]].is_answer_correct(answer):
            self.score += 1

        # after checking the answer we can move to the next question
        self.next_question()
