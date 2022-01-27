class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_num = 0
        self.q_total = len(q_list)

    def ask_qestions(self):
        while self.q_num < self.q_total:
            cur_q = self.q_list[self.q_num]
            asw = input(f"Q.{self.q_num + 1} : {cur_q.text} [True/False] - ").title()
            self.q_num += 1