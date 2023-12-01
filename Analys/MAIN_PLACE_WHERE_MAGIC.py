# a = [1,2]
# b = ["s","2"]
# a.insert(0,"no")
# a.pop()
# print(a)
# del a[1]
# try:
#     a.remove(1)
# except ValueError:
#     print("Такого элемента нет")
# print(a)
# print((54).__eq__(54))
# print(list(range(1,10+1,2)))


# s = "12234"
# print(s.split("2"))


# capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
# print(list(capitals.keys()) + list(capitals.values()))


# # print("Hello WO", "Ik", end="****")
# aName = 'Ildar'
# age = 14
# print(aName, "is", age, "years old.")
# print("%s is %.1f years old." % (aName, age))


# def removeDupWithoutOrder(str):
#     return "".join(sorted(set(str)))[::-1]
# # ответ: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
# list = [sym.upper() for sym in 'CATTTTT' if sym != "+"]
# print(removeDupWithoutOrder(list))