year = 0
for i in range(2000, 2101):
    if((i % 4 == 0) & (i % 100 != 0) | (i % 400 == 0)):
        print(i, end = ' ')

print("")