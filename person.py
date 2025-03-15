class Person:
    def __init__(self, carbs=0, fats=0, protein=0, cals=0): #g, s, and k have default values of zero
        self.carbs = carbs
        self.fats = fats
        self.protein = protein
        self.cals = cals

    def __str__(self):
        return f"\n{round(self.cals, 2)} kcals\n{round(self.carbs, 2)} g carbohydrates\n{round(self.fats, 2)} g fats\n{round(self.protein, 2)} g protein\n"

    def __add__(self, other): #operator overloading of the + symbol
        cals = self.cals + other.cals
        carbs = self.carbs + other.carbs
        protein = self.protein + other.protein
        fats = self.fats + other.fats
        return Person(carbs, fats, protein, cals)

    def add_carbs(self, carbs):
        self.carbs += carbs

    def add_fats(self, fats):
        self.fats += fats

    def add_protein(self, p):
        self.protein += p

    def add_cals(self, cals):
        self.cals += cals

    def get_cals(self):
        return self.cals

    def get_carbs(self):
        return self.carbs

    def get_fats(self):
        return self.fats

    def get_prot(self):
        return self.protein


