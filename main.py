df = {1:[{1:1,2:6}],
      2:[2,6,7,8,9,7],
      3:[3,6,7,8,9,7],
      4:[4,6,7,8,9,7],
      5:[5,6,7,8,9,7],
      6:[6,6,7,8,9,7]}



class Stacion():
    """docstring"""
    df
    def __init__(self, nomer, vr):
        """Constructor"""
        self.nomer = nomer
        self.vr = vr
        self.df =df[i]


    def name(self):
        return f"Исследовательская выработка № {self.vr} Cтанция №{self.nomer}"


q = int(input("Введите номер станции"))

is_3= ["Исследовательская выработка №3"]
for i in range(1,7):
    Stacion(i,"3")
    is_3.append(Stacion(i,"3"))

print(f"{is_3[q].name()}  \n Данные по замерам: {is_3[q].df}" )
