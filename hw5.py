def read_single_digit(number):
    if number == '1':
        print('일', end=' ')
    elif number == '2':
        print('이', end=' ')
    elif number == '3':
        print('삼', end=' ')
    elif number == '4':
        print('사', end=' ')
    elif number == '5':
        print('오', end=' ')
    elif number == '6':
        print('육', end=' ')
    elif number == '7':
        print('칠', end=' ')
    elif number == '8':
        print('팔', end=' ')
    elif number == '9':
        print('구', end=' ')
    elif number == '0':
        print('영', end=' ')


def read_number(number):
    if len(number) == 3:
        read_single_digit(number[0])
        read_single_digit(number[1])
        read_single_digit(number[2])
    elif len(number) == 2:
        print('영', end=' ')
        read_single_digit(number[0])
        read_single_digit(number[1])
    elif len(number) ==1:
        print('영', end=' ')
        print('영', end=' ')
        read_single_digit(number[0])
    else :
        print('오류: 세 자리수 이하의 10진 정수를 입력해주세요.')
        
    
num = input('세 자리 정수 입력: ')

read_number(num)
