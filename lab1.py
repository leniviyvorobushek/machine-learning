class Pupa:
  def __init__(self):
    self.count = 0

  def do_work(self, spisok1, spisok2):
    spisok = []
    self.count += len(spisok1)
    for i in range (0, len(spisok1)):
      spisok.append(spisok1[i]+spisok2[i])
    print('Работа Пупы:', spisok)
    return spisok

  def take_salary(self):
    salary = 2 * self.count
    print('Зарплата Пупы: ', salary)
    return salary

class Lupa:
  def __init__(self):
    self.count = 0

  def do_work(self, spisok1, spisok2):
    spisok = []
    self.count += len(spisok1)
    for i in range (0, len(spisok1)):
      spisok.append(spisok1[i] - spisok2[i])
    print('Работа Лупы: ', spisok)
    return spisok

  def take_salary(self):
    salary = 2 * self.count
    print('Зарплата Лупы: ', salary)
    return salary

class Accountant():
  def give_salary(self, worker):
    return worker.take_salary()


accountant = Accountant()

lupa = Lupa()
lupa.do_work([1, 2, 3], [4, 5, 6])

pupa = Pupa()
pupa.do_work([1, 2, 3], [4, 5, 6])
pupa.do_work([7, 8, 9], [10, 11, 12])

accountant.give_salary(lupa)
accountant.give_salary(pupa)