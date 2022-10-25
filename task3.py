def rock(jewels, stone):
    count_jewels = 0
    for i in range(len(jewels)):
        st = jewels[i]
        if st in stone:
            count_jewels += stone.count(st)
    return count_jewels

jewels = input("jewels = ")
stone = input("stone = ")
print(rock(jewels, stone))