class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'


h1 = House('ул. 5 Армии д 12', 14)
h2 = House('СНТ Солнышко д 59', 2)

print(h1)
print(h2)
print(len(h1))
print(len(h2))
