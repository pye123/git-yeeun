shopping_bag = {}

print('[구입]')
while True :
    item = input('상품명? ')
    if item == '' :
        break
    num = int(input('수량은? '))
    shopping_bag[item] = num
    print(f'장바구니에 {item} {num}개가 담겼습니다. ')
    print()

print()
print(f'>>>장바구니 보기: {shopping_bag}')
print()

print('[검색]')
while True :
    item = input('장바구니에서 확인하고자 하는 상품은? ')
    if item == '' :
        break
    elif item in shopping_bag :
        print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')
    else : print(f'{item}은(는) 장바구니에 없습니다.')
    print()

