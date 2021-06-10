a = int(input('정수 a를 입력하시오. : '))
b = int(input('정수 b를 입력하시오. : '))
c = 1
print('GCD계산기 | GCD(Grestest Common Divisor은 두 수의 최대공약수를 지칭합니다.')
print('GCD({}, {}) = {}'.format(a, b, c))

if a == b: # GCD(a, b)가 a또는 b가 되는 경우의 수
        c = a
elif b > a: # b가 a보다 크면 a와 b 스위치
    a, b = b, a
    
div_a = []
div_b = []

for i in range(1, a):
    if a % i == 0:
        div_a.append(i)

for i in range(1, b):
    if b % i == 0:
        div_b.append(i)

while(1):
        c = a % b;
        if(c == 0):
            c = b
            exit
        a = b;
        b = c;

print('GCD({}, {}) = {}'.format(a, b, c))

print(div_a)
print(div_b)


# Fail