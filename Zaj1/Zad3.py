class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return True if self.score == other.score else False
    def __ne__(self, other):
        return True if self.score != other.score else False
    def __lt__(self,other):
        return True if self.score < other.score else False
    def __gt__(self,other):
        return True if self.score > other.score else False
    def __str__(self):
        return f"Imie: {self.name}, wynik: {self.score}"

