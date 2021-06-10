def all():
    def num_lib(val):
        return val == '0' or val == '1' or val == '2' or val == '3' or val == '4' or val == '5' or val == '6' or val == '7' or val == '8' or val == '9'

    def num_test(val_str):
        n = 0
        var = ''
        try: 
            while num_lib(val_str[n]):
                var += val_str[n]
                n += 1
        except: pass
        return (int(var), n)

    def calculate(str, a, b):
        if str == '+':
            return a + b
        if str == '-':
            return a - b
        if str == '*':
            return a * b
        if str == '/':
            return a / b
        if str == '^':
            return a ** b

    def operator(op):
        return op == '+' or op == '-' or op == '*' or op == '/' or op == '^'

    status = False
    omo = input('')



    #print(char + '=')
    while True:
        try: 
            if omo[0] == '-': #for negative numbers
                status = True #because here the numbers are string format
                omo = omo[1:]

            a = num_test(omo)[0]

            if status == True:
                a = -a
                status = False
            a_end = num_test(omo)[1]
            omo = omo[a_end:]

            if omo == '':
                #print(number1)
                break

            op = omo[0]
            omo = omo[1:]

            b = num_test(omo)[0]
            b_end = num_test(omo)[1]

            result = calculate(op, a, b)
            a = result
            omo = str(a) + omo[b_end:]

            print(omo)

        except: break


print("adf")
all()