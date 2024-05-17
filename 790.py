class Student:
    def __init__(self,scores):
        self.scores = scores

    def get_scores_sum(self):
        j = 0
        for i in self.score:
            j += i
        return j

scores = [55,75,80,62,77]
s1 = Student(scores)
total = s1.get_scores_sum()
print(total)
