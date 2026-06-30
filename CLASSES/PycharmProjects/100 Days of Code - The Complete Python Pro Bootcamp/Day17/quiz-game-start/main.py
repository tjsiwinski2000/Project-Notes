from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Create empty list
# [] always means list , note: this will be a list of question objects
question_bank=[]

for d in question_data:
    #Variables: question_text, question_ans will  contain dictionary value
    question_text = d["question"]
    question_ans =  d["correct_answer"]

    #Create new object with values in question_text, question_ans
    new_question= Question(question_text,question_ans)
    # ".append"  , not +=
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")