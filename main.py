from guizero import App, Text, PushButton, Box, Window

#------------------------------Application Window------------------------------------#

app = App(title="Quiz Game", width=700, height=700, bg="#FFED7C")

#------------------------------Mathematics Window-----------------------------------#

math_window = Window(app, width=700, height=700, bg="#FFED7C")
math_window.hide()


#once mathematics button is clicked, shows a new window of a quiz
def show_math():
    math_window.show()


#Quiz contantainers from top to bottom; mathematics_container_1 = Image container, mathematics_container_2 = Question container, mathematics_container_3 = filler container, mathematics_container_4 = upper answer button container, mathematics_container_5 = filler container, mathematics_container_6 = lower answer button container, mathematics_container_7 = bottom container with score and question
mathematics_container_1 = Box(math_window, width=700, height=250, border=2)
mathematics_container_2 = Box(math_window, width=700, height=100, border=2)
mathematics_container_3 = Box(math_window, width=700, height=25, border=2)
mathematics_container_4 = Box(math_window, width=700, height=100, border=2)
mathematics_container_5 = Box(math_window, width=700, height=25, border=2)
mathematics_container_6 = Box(math_window, width=700, height=100, border=2)
mathematics_container_7 = Box(math_window, width=700, height=100, border=2)

#containers where the upper buttons are positioned
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

#containers where the lower buttons are positioned
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

#bottom section with score and questions
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

#-----------------------------Mathematics Widgets------------------------------#

#Question Text
math_question = Text(mathematics_container_2,
                     text="Question",
                     width=100,
                     height=100)
math_question.bg = "#FF8108"

#Score & Question Num
math_question_number = Text(mathematics_bottom_question,
                            text="Question Num: 1/10")
math_question_score = Text(mathematics_bottom_score, text="Score: 0")

#Answer Buttons
math_answer_1 = PushButton(mathematics_button_1,
                           align="left",
                           width=100,
                           height=70)
math_answer_1.bg = "#54C03D"
math_answer_1.font = "sans-serif"
math_answer_2 = PushButton(mathematics_button_2,
                           align="right",
                           width=100,
                           height=70)
math_answer_2.bg = "#2D73A9"
math_answer_2.font = "sans-serif"
math_answer_3 = PushButton(mathematics_button_3,
                           align="left",
                           width=100,
                           height=70)
math_answer_3.bg = "#DB4692"
math_answer_3.font = "sans-serif"
math_answer_4 = PushButton(mathematics_button_4,
                           align="right",
                           width=100,
                           height=70)
math_answer_4.bg = "#FFFA13"
math_answer_4.font = "sans-serif"

#-----------------------------Chemisrtry Window--------------------------------#

chemistry_window = Window(app, width=700, height=700, bg="#FFED7C")
chemistry_window.hide()


#once chemistry button is clicked, shows a new window of a quiz
def show_chemistry():
    chemistry_window.show()


#Quiz contantainers from top to bottom; chemistry_container_1 = Image container, chemistry_container_2 = Question container, chemistry_container_3 = filler container, chemistry_container_4 = upper answer button container, chemistry_container_5 = filler container, chemistry_container_6 = lower answer button container, chemistry_container_7 = bottom container with score and question
chemistry_container_1 = Box(chemistry_window, width=700, height=250, border=2)
chemistry_container_2 = Box(chemistry_window, width=700, height=100, border=2)
chemistry_container_3 = Box(chemistry_window, width=700, height=25, border=2)
chemistry_container_4 = Box(chemistry_window, width=700, height=100, border=2)
chemistry_container_5 = Box(chemistry_window, width=700, height=25, border=2)
chemistry_container_6 = Box(chemistry_window, width=700, height=100, border=2)
chemistry_container_7 = Box(chemistry_window, width=700, height=100, border=2)

#containers where the upper buttons are positioned
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

#containers where the lower buttons are positioned
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

#bottom section with score and questions
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

#Question Text
chemistry_question = Text(chemistry_container_2,
                          text="Question",
                          width=100,
                          height=100)
chemistry_question.bg = "#FF8108"

#Score & Question Num
chemistry_question_number = Text(chemistry_bottom_question,
                                 text="Question Num: 1/10")
chemistry_question_score = Text(chemistry_bottom_score, text="Score: 0")

#Answer Buttons
chemistry_answer_1 = PushButton(chemistry_button_1,
                                align="left",
                                width=100,
                                height=70)
chemistry_answer_1.bg = "#54C03D"
chemistry_answer_1.font = "sans-serif"
chemistry_answer_2 = PushButton(chemistry_button_2,
                                align="right",
                                width=100,
                                height=70)
chemistry_answer_2.bg = "#2D73A9"
chemistry_answer_2.font = "sans-serif"
chemistry_answer_3 = PushButton(chemistry_button_3,
                                align="left",
                                width=100,
                                height=70)
chemistry_answer_3.bg = "#DB4692"
chemistry_answer_3.font = "sans-serif"
chemistry_answer_4 = PushButton(chemistry_button_4,
                                align="right",
                                width=100,
                                height=70)
chemistry_answer_4.bg = "#FFFA13"
chemistry_answer_4.font = "sans-serif"

#-----------------------------Geography Window--------------------------------#

geography_window = Window(app, width=700, height=700, bg="#FFED7C")
geography_window.hide()


#once geography button is clicked, shows a new window of a quiz
def show_geography():
    geography_window.show()


#Quiz contantainers from top to bottom; geography_container_1 = Image container, geography_container_2 = Question container, geography_container_3 = filler container, geography_container_4 = upper answer button container, geography_container_5 = filler container, geography_container_6 = lower answer button container, geography_container_7 = bottom container with score and question
geography_container_1 = Box(geography_window, width=700, height=250, border=2)
geography_container_2 = Box(geography_window, width=700, height=100, border=2)
geography_container_3 = Box(geography_window, width=700, height=25, border=2)
geography_container_4 = Box(geography_window, width=700, height=100, border=2)
geography_container_5 = Box(geography_window, width=700, height=25, border=2)
geography_container_6 = Box(geography_window, width=700, height=100, border=2)
geography_container_7 = Box(geography_window, width=700, height=100, border=2)

#containers where the upper buttons are positioned
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

#containers where the lower buttons are positioned
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

#bottom section with score and questions
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

#Question Text
geography_question = Text(geography_container_2,
                          text="Question",
                          width=100,
                          height=100)
geography_question.bg = "#FF8108"

#Score & Question Num
geography_question_number = Text(geography_bottom_question,
                                 text="Question Num: 1/10")
geography_question_score = Text(geography_bottom_score, text="Score: 0")

#Answer Buttons
geography_answer_1 = PushButton(geography_button_1,
                                align="left",
                                width=100,
                                height=70)
geography_answer_1.bg = "#54C03D"
geography_answer_1.font = "sans-serif"
geography_answer_2 = PushButton(geography_button_2,
                                align="right",
                                width=100,
                                height=70)
geography_answer_2.bg = "#2D73A9"
geography_answer_2.font = "sans-serif"
geography_answer_3 = PushButton(geography_button_3,
                                align="left",
                                width=100,
                                height=70)
geography_answer_3.bg = "#DB4692"
geography_answer_3.font = "sans-serif"
geography_answer_4 = PushButton(geography_button_4,
                                align="right",
                                width=100,
                                height=70)
geography_answer_4.bg = "#FFFA13"
geography_answer_4.font = "sans-serif"

#-----------------------------English Window--------------------------------#

english_window = Window(app, width=700, height=700, bg="#FFED7C")
english_window.hide()


#once english button is clicked, shows a new window of a quiz
def show_english():
    english_window.show()


#Quiz contantainers from top to bottom; english_container_1 = Image container, english_container_2 = Question container, english_container_3 = filler container, english_container_4 = upper answer button container, english_container_5 = filler container, english_container_6 = lower answer button container, english_container_7 = bottom container with score and question
english_container_1 = Box(english_window, width=700, height=250, border=2)
english_container_2 = Box(english_window, width=700, height=100, border=2)
english_container_3 = Box(english_window, width=700, height=25, border=2)
english_container_4 = Box(english_window, width=700, height=100, border=2)
english_container_5 = Box(english_window, width=700, height=25, border=2)
english_container_6 = Box(english_window, width=700, height=100, border=2)
english_container_7 = Box(english_window, width=700, height=100, border=2)

#containers where the upper buttons are positioned
english_filler_box_1 = Box(english_container_4,
                           align="left",
                           width=150,
                           height=100)
english_filler_box_2 = Box(english_container_4,
                           align="right",
                           width=150,
                           height=100)
english_button_1 = Box(english_container_4, align="left", width=180, height=80)
english_button_2 = Box(english_container_4,
                       align="right",
                       width=180,
                       height=80)

#containers where the lower buttons are positioned
english_filler_box_3 = Box(english_container_6,
                           align="left",
                           width=150,
                           height=100)
english_filler_box_4 = Box(english_container_6,
                           align="right",
                           width=150,
                           height=100)
english_button_3 = Box(english_container_6, align="left", width=180, height=80)
english_button_4 = Box(english_container_6,
                       align="right",
                       width=180,
                       height=80)

#bottom section with score and questions
english_bottom = Box(english_container_7, align="bottom", width=700, height=50)
english_bottom_question = Box(english_bottom,
                              align="right",
                              width=200,
                              height=25)
english_bottom_score = Box(english_bottom, align="left", width=100, height=25)

#-----------------------------English Widgets--------------------------------#

#Question Text
english_question = Text(english_container_2,
                        text="Question",
                        width=100,
                        height=100)
english_question.bg = "#FF8108"

#Score & Question Num
english_question_number = Text(english_bottom_question,
                               text="Question Num: 1/10")
english_question_score = Text(english_bottom_score, text="Score: 0")

#Answer Buttons
english_answer_1 = PushButton(english_button_1,
                              align="left",
                              width=100,
                              height=70)
english_answer_1.bg = "#54C03D"
english_answer_1.font = "sans-serif"
english_answer_2 = PushButton(english_button_2,
                              align="right",
                              width=100,
                              height=70)
english_answer_2.bg = "#2D73A9"
english_answer_2.font = "sans-serif"
english_answer_3 = PushButton(english_button_3,
                              align="left",
                              width=100,
                              height=70)
english_answer_3.bg = "#DB4692"
english_answer_3.font = "sans-serif"
english_answer_4 = PushButton(english_button_4,
                              align="right",
                              width=100,
                              height=70)
english_answer_4.bg = "#FFFA13"
english_answer_4.font = "sans-serif"

#-----------------------------Ulitimate Window--------------------------------#

ultimate_window = Window(app, width=700, height=700, bg="#FFED7C")
ultimate_window.hide()


#once ultimate test button is clicked, shows a new window of a quiz
def show_ultimate():
    ultimate_window.show()


#Quiz contantainers from top to bottom; ultimate_container_1 = Image container, ultimate_container_2 = Question container, ultimate_container_3 = filler container, ultimate_container_4 = upper answer button container, ultimate_container_5 = filler container, ultimate_container_6 = lower answer button container, ultimate_container_7 = bottom container with score and question
ultimate_container_1 = Box(ultimate_window, width=700, height=250, border=2)
ultimate_container_2 = Box(ultimate_window, width=700, height=100, border=2)
ultimate_container_3 = Box(ultimate_window, width=700, height=25, border=2)
ultimate_container_4 = Box(ultimate_window, width=700, height=100, border=2)
ultimate_container_5 = Box(ultimate_window, width=700, height=25, border=2)
ultimate_container_6 = Box(ultimate_window, width=700, height=100, border=2)
ultimate_container_7 = Box(ultimate_window, width=700, height=100, border=2)

#containers where the upper buttons are positioned
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

#containers where the lower buttons are positioned
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

#bottom section with score and questions
ultimate_bottom = Box(ultimate_container_7,
                      align="bottom",
                      width=700,
                      height=50)
ultimate_bottom_question = Box(ultimate_bottom,
                               align="right",
                               width=200,
                               height=25)
ultimate_bottom_score = Box(ultimate_bottom,
                            align="left",
                            width=100,
                            height=25)

#-----------------------------Ultimate Widgets--------------------------------#

#Question Text
ultimate_question = Text(ultimate_container_2,
                         text="Question",
                         width=100,
                         height=100)
ultimate_question.bg = "#FF8108"

#Score & Question Num
ultimate_question_number = Text(ultimate_bottom_question,
                                text="Question Num: 1/10")
ultimate_question_score = Text(ultimate_bottom_score, text="Score: 0")

#Answer Buttons
ultimate_answer_1 = PushButton(ultimate_button_1,
                               align="left",
                               width=100,
                               height=70)
ultimate_answer_1.bg = "#54C03D"
ultimate_answer_1.font = "sans-serif"
ultimate_answer_2 = PushButton(ultimate_button_2,
                               align="right",
                               width=100,
                               height=70)
ultimate_answer_2.bg = "#2D73A9"
ultimate_answer_2.font = "sans-serif"
ultimate_answer_3 = PushButton(ultimate_button_3,
                               align="left",
                               width=100,
                               height=70)
ultimate_answer_3.bg = "#DB4692"
ultimate_answer_3.font = "sans-serif"
ultimate_answer_4 = PushButton(ultimate_button_4,
                               align="right",
                               width=100,
                               height=70)
ultimate_answer_4.bg = "#FFFA13"
ultimate_answer_4.font = "sans-serif"

#------------------------------ Main Menu Window ------------------------------#

#Menu containers from top to botton e.g container 1, 2, 3, 4, 5, 6, 7
menu_container_1 = Box(app, width=700, height=100)
menu_container_2 = Box(app, width=700, height=100)
menu_container_3 = Box(app, width=700, height=100)
menu_container_4 = Box(app, width=700, height=100)
menu_container_5 = Box(app, width=700, height=100)
menu_container_6 = Box(app, width=700, height=100)
menu_container_7 = Box(app, width=700, height=100)

#button container nunmber 1
filler_box_1 = Box(menu_container_2, align="top", width=700, height=20)
button_1_container = Box(menu_container_2,
                         align="bottom",
                         width=170,
                         height=55)
filler_box_2 = Box(menu_container_2, align="bottom", width=700, height=20)

#button  container number 2
filler_box_3 = Box(menu_container_3, align="top", width=700, height=20)
button_2_container = Box(menu_container_3,
                         align="bottom",
                         width=170,
                         height=55)
filler_box_4 = Box(menu_container_3, align="bottom", width=700, height=20)

#button  container number 3
filler_box_5 = Box(menu_container_4, align="top", width=700, height=20)
button_3_container = Box(menu_container_4,
                         align="bottom",
                         width=170,
                         height=55)
filler_box_6 = Box(menu_container_4, align="bottom", width=700, height=20)

#button  container number 4
filler_box_7 = Box(menu_container_5, align="top", width=700, height=20)
button_4_container = Box(menu_container_5,
                         align="bottom",
                         width=170,
                         height=55)
filler_box_8 = Box(menu_container_5, align="bottom", width=700, height=20)

#button  container number 5
filler_box_9 = Box(menu_container_6, align="top", width=700, height=20)
button_5_container = Box(menu_container_6,
                         align="bottom",
                         width=170,
                         height=55)
filler_box_10 = Box(menu_container_6, align="bottom", width=700, height=20)

#-------------------------------Main Menu Buttons----------------------------------#

Mathematics = PushButton(button_1_container,
                         text="Mathematics",
                         width=100,
                         height=60,
                         align="bottom",
                         command=show_math)
Mathematics.bg = "#7D7268"
Mathematics.font = "sans-serif"

Chemistry = PushButton(button_2_container,
                       text="Chemistry",
                       width=100,
                       height=60,
                       align="bottom",
                       command=show_chemistry)
Chemistry.bg = "#54C03D"
Chemistry.font = "sans-serif"

Geography = PushButton(button_3_container,
                       text="Geography",
                       width=100,
                       height=60,
                       align="bottom",
                       command=show_geography)
Geography.bg = "#449BB0"
Geography.font = "sans-serif"

English = PushButton(button_4_container,
                     text="English",
                     width=100,
                     height=60,
                     align="bottom",
                     command=show_english)
English.bg = "#FEAD5F"
English.font = "sans-serif"

UnltimateTest = PushButton(button_5_container,
                           text="Unltimate Test",
                           width=100,
                           height=60,
                           align="bottom",
                           command=show_ultimate)
UnltimateTest.bg = "#DB4692"
UnltimateTest.font = "sans-serif"

app.display()
