a = [15,12,9,8,6,4,1]



class Data:
    df = a
    def __init__(self, name):
        self.name = name


    def asd(self,x):
        self.srez = self.df[0:x]
        return self.srez



d1 = Data("Дата 1")
print(d1.df)
print(d1.asd(6))
