# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати, нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)
import math
class Triangle:

    def __init__(self,  a, b, c):
        """Создание треугольника и вывод значений сторон треугольника на экран"""
        self.a = a
        self.b = b
        self.c = c
        self._check = [self.a, self.b, self.c]
        if max(self._check) > (sum(self._check)-max(self._check)):
            raise Exception("Don't create the Triangle")


    def area_calculation(self):
        """Вычисление площади"""
        p = sum(self._check)/2
        return int(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))

    def calculation_of_perimeter(self):
        """Вычисление периметра"""
        return sum(self._check)

# main
if __name__ == "__main__":
    a = int(input("Input side A-Triangle: "))
    b = int(input("Input side B-Triangle: "))
    c = int(input("Input side C-Triangle: "))
    result = Triangle(a, b, c)
    print(f"Площадь треугольника = {result.area_calculation()}")
    print(f"Периметр треугольника = {result.calculation_of_perimeter()}")
