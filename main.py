#while
i = 0
while i < 5:
    print("While:",i)
    i += 1

#for
for i in range(5):
    print("For:",i)

#if,else,elif
age = 34
if age < 18:
    print("Маленький")
elif age == 18:
    print("18")
else:
    print("Дорослий")

#def
def say_hello(name):
    print("Привіт,", name)

say_hello("Ростик")

#str
text = "Python"
print(len(text))         # Довжина
print(text.upper())      # ВЕРХНІМИ
print(text.lower())      # нижніми
print(text[0])           # Перша літера
print(text[-1])          # Остання літера

#list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])         # перший елемент
print(len(fruits))       # довжина списку

#dist(словник) типу як в js Object
person = {"name": "Ivan", "age": 25}
print(person["name"])
person["age"] += 1
print(person["age"])

#input
name = input("Як тебе звати? ")
print("Привіт,", name)

# type data
type(10)        # int
type(3.14)      # float
type("hi")      # str
type([1,2,3])   # list
type({"a":1})   # dict

#Шаблоний рядок
name = "Rostik"
age = 20
print(f"Мене звати {name}, мені {age} років.")

# operators
# ==  # дорівнює
# !=  # не дорівнює
# <   # менше
# >   # більше
# <=  # менше або дорівнює
# >=  # більше або дорівнює
