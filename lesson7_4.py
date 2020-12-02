
class Drob:

    def __init__(self, chilitel, znamentel):
        self.chilitel = chilitel
        self.znamentel = znamentel

    def __mul__(self, other):
        new_chilitel = self.chilitel * other.chilitel
        new_znamentel = self.znamentel * other.znamentel

        return Drob(new_chilitel, new_znamentel)

    def __str__(self):
        return f"{self.chilitel}\n{min(len(str(self.znamentel)), len(str(self.chilitel))) * '-'}\n{self.znamentel}"


drob1 = Drob(1, 3)
drob2 = Drob(1, 2)
drob3 = drob1 * drob2
drob4 = drob3 * drob1
print(drob4)


# 2)деление дробей a*d/b*c
# 3)сложениe (a*d+c*b)/(b*d))
# 4)вычитание(a*d-c*b)/(b*d))

actions = ['*', '/', '+', '-']

first = str(input('Введите первую дробь: '))
second = str(input('Введите вторую дробь: '))
action = str(input('Выберите операцию (*, /, +, -): '))
while True:
    if action not in actions:
        action = str(input('Выберите корректную операцию (*, /, +, -): '))
    else:
        break

a = int(first.split('/')[0])
b = int(first.split('/')[1])
c = int(second.split('/')[0])
d = int(second.split('/')[1])

if action == '*':
    print(str(a * c) + '/' + str(b * d))
elif action == '/':
    print(str(a * d) + '/' + str(b * c))
elif action == '+':
    print(str((a * d) + (c * b)) + '/' + str(b * d))
elif action == '-':
    print(str((a * d) - (c * b)) + '/' + str(b * d))







