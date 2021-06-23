key = int(input("정수 키 입력 : "))

arr = []

for i in range(5):
    get = input("영문자 : ")
    a = ord(get) + key
    arr.append(chr(a)) # chr 최대한 쓸지 말것

print(arr[2:3])
