class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_num = 0
        self.q_total = len(q_list)
        self.score = 0

    def check_answer(self, asw, c_asw):
        if asw.lower() == c_asw.lower():
            self.score += 1
            print('\nYou got it right!\n')
        else:
            print('\nYou got it wrong!\n')
        print(f"The correct answer was {c_asw}.\n")


    def ask_qestions(self):
        while self.q_num < self.q_total:
            cur_q = self.q_list[self.q_num]
            asw = input(f"Q.{self.q_num + 1} : {cur_q.text} [True/False] - ")
            self.check_answer(asw, cur_q.answer)
            self.q_num += 1
        
        print(f"You have completed the quiz!\nYour final score is: {self.score}/{self.q_total}")

        