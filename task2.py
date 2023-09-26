countBush = int(input("Введите колличество кустов: "))
countBerries = [int(
    input(f"Введите колличество ягод на кусте {i+1}: ")) for i in range(countBush)]
countBerries = countBerries + countBerries[:2]
maxBerries = 0
for i in range(countBush):
    maxBerries = max(
        maxBerries, countBerries[i] + countBerries[i+1] + countBerries[i+2])
print(maxBerries)
