#파이썬프로그래밍2분반2주차과제_202310645박예은
#조건1

def get_radius(prompt) :
    r=int(input(prompt))
    return r

result=get_radius('넓이를 구하고자 하는 원의 반지름은? ')
print('반지름 ', result, '인 원의 넓이 = 3.14 * ', result, ' * ', result, ' = ', 3.14*result*result, sep='')


#조건2

def get_circle_area(r) :
    s=3.14*r*r
    return s

r=int(input('넓이를 구하고자 하는 원의 반지름은? '))
result=get_circle_area(r)
print('반지름 ', r, '인 원의 넓이 = 3.14 * ', r, ' * ', r, ' = ',result, sep='')
