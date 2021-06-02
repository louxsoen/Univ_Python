let = [1, 3, 5, 7, 9]

for i in let:
    print(i+2, end = ' ')

print("")

for i in range(5):
    print(i+1, end = ' ')

print("")
start = int(input("구구단 입력 : "))

for i in range(9):
    print("%d * %d = %d" %(start, i + 1, start * (i+1) ))
    i += 1

