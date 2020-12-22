class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        number = self.question_number + 1
        self.question_number += 1
        user_answer = input(f"Q{number}. {question.text}: (True/False)?: ")
        check = self.check_answer(user_answer, question.answer)
        if check:
            self.score += 1
        print(f"Your score is {self.score}/{number}")

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            return True
        else:
            print("That's wrong")
            print(f"The correct answer is {correct_answer}")
            return False
