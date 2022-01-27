class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_num = 0

    def next_question(self):
        cur_q = self.q_list[self.q_num]
        asw = bool(input(f"Q.{self.q_num + 1} : {cur_q.text} [True/False] - ").title())