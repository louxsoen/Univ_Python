while(1):
    a = int(input("양의 정수? \'종료 | 0 입력\' "))   

    if( a == 0 ):
        print("감사합니다.")
        break

    for i in range(a):
        if(a % (i+1) == 0):
            print(i+1, end = ' ')

    print("")

