#Практическое занятие 1: Простые операции с переменными
'''
x=10;
y=5;

summa = x + y;
minus = x - y; 
umnojenie = x * y;
delenie = x / y;
print("summa =", summa, "minus =", minus, "umnojenie =", umnojenie, "delenie =", delenie);
'''


#Практическое занятие 2: Работа со строками
'''
name = "Kanstantsin"
age = 37
hobby = "Computer applications"

about_me = "Меня зовут " + name + ". Мне " + str(age) + "лет. И хобби у меня:" + hobby + "."
print(about_me)
'''


#Практическое занятие 3: Работа с числами
'''
import math
radius = 5.0
area = math.pi * radius**2

print(area)
'''

#Практическое занятие 4: Работа с булевыми значениями
'''
is_raining = False
is_sunny = False
if is_raining:
    print ("weather is raining")
elif is_sunny:
    print ("weather is sunny")
else: print("weather is not sunny and rainny")
'''

#Практическое занятие 5: Работа со списками

fruits = ["яблоко", "банан", "апельсин", "киви", "чихуахуа"]
fruits.append("груша")
for fruits in fruits:
    print(fruits)