def collection(num):
    newCollection = set()
    for i in range(num):
        newCollection.add(int(input(f"Введите число {i+1}: ")))
    return newCollection


numberN = int(input("Введите количествово элементов первого множества: "))
nCollection = collection(numberN)

numberM = int(input("Введите количествово элементов второго множества: "))
mCollection = collection(numberM)

sortColletion = sorted(nCollection.intersection(mCollection))
print("Первое множество:")
print(*nCollection)
print("Второе множество:")
print(*mCollection)
print("Отсортированный набор из двух множеств:")
print(*sortColletion)
