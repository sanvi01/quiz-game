import question_model


class QuizBrain:

    def __init__(self,q_list):
        self.question_no = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        # if self.question_no < len(self.q_list):
        #     return True
        # else:
        #     return False
        return self.question_no < len(self.q_list)

    def next_q(self):
        question = self.q_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}) {question.text} (True/False)? ")
        self.check_answer(user_ans, question.ans)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer")
        print(f"Correct answer is {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_no}.")
