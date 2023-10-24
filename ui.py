#part 5
from tkinter import *
#part 6
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


#part 5
class QuizzInterface:

  def __init__(self, quiz_brain: QuizBrain):#, quiz_brain: QuizBrain -> part 6
    #part 6
    self.quiz = quiz_brain
    
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    #label score
    self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
    self.score_label.grid(row=0, column=1)

    #question Canvas
    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text((150,125),
                                                 width=280,
                                                 text="Text", 
                                                 fill=THEME_COLOR, 
                                                 font=("Arial", 20, "italic")
                                                )
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    #buttons right and wrong with images
    self.false_img = PhotoImage(file="images/false.png")
    self.true_img = PhotoImage(file="images/true.png")
    self.false_button = Button(
      image=self.false_img,
      highlightthickness=0, command=self.false_pressed)
    self.false_button.grid(row=2, column=1)
    self.true_button = Button(
      image=self.true_img, highlightthickness=0, command=self.true_pressed)
    self.true_button.grid(row=2, column=0)
    #part6
    self.get_next_question()

    self.window.mainloop()

  #part 6  
  def get_next_question(self):
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      #part9
      self.score_label.config(text=f"Score: {self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text=q_text)
    else:
      self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
      self.true_button.config(state="disable")
      self.false_button.config(state="disable")

  #part 8
  def true_pressed(self):
    is_right = self.quiz.check_answer("True")
    #part 8
    self.give_feedback(is_right)
    self.window.after_cancel()
    

  #part8
  def false_pressed(self):
    is_right = self.quiz.check_answer("False")
    #part9
    self.give_feedback(is_right)

  #part8
  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)
      