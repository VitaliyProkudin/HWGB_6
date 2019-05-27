

# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла



import os.path
PATH_WORKER = os.path.abspath(r"C:\Users\vitaliy.prokudin\YandexDisk\Книги + курсы\Программирование\Python_обучающие курсы\les_6\hard_HW_workers.txt")
PATH_HOURS = os.path.abspath(r"C:\Users\vitaliy.prokudin\YandexDisk\Книги + курсы\Программирование\Python_обучающие курсы\les_6\hard_HW_hours_of.txt")

class Wages:
    def __init__(self, str_workers, str_hourse):
        # Реализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла
        self._str_workers = str_workers
        self._str_hourse = str_hourse
        self.payroll_result = list()

    def get_all_dict(self):
        return self._str_hourse, self._str_workers

    def payroll_worker(self, name_worker, surname_worker):
        for i in range(len(self._str_workers)):
            if name_worker in self._str_workers[i] and surname_worker in self._str_workers[i]:
                for j in range(len(self._str_hourse)):
                    if name_worker in self._str_hourse[j] and surname_worker in self._str_hourse[j]:
                        result = int(self._str_hourse[j][2]) / int(self._str_workers[i][4])
                        if result > 1:
                            cash = ((result-int(result)) * 2 * int(self._str_workers[i][2])) + int(result) * int(self._str_workers[i][2])

                            return cash
                        else:
                            cash = int(self._str_workers[i][2]) * result
                            if cash != int(cash):
                                cash = float('{:.2f}'.format(cash))
                            return cash
                return False

# ----main----start
with open(PATH_WORKER, encoding="UTF-8") as workers:
    with open(PATH_HOURS, encoding="UTF-8") as hourse:
        workers_list = list()
        for line in workers.readlines():
            workers_list.append(line.split())
        hourse_list = list()
        for line in hourse.readlines():
            hourse_list.append(line.split())
# ----main----for user
        a = Wages(workers_list, hourse_list)
        print(a.payroll_worker('Василий', 'Сидоров'))
        # print(a.get_all_dict())


