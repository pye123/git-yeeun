def buy(lst) :
    print('[구입]')
    item = input('상품명? ')
    if item == '' :
        print()
        return False
    num = int(input('수량은? '))
    lst[item] = num
    print(f'장바구니에 {item} {num}개가 담겼습니다. ')
    print()

def show(lst):
    print(f'>>>장바구니 보기: {lst}')
    print()

def find(lst):
    print('[검색]')
    item = input('장바구니에서 확인하고자 하는 상품은? ')
    if item in lst :
        print(f'{item}은(는) {lst[item]}개 담겨 있습니다.')
    else : print(f'장바구니에 {item}은(는) 없습니다.')

shopping_bag = {}
while True :
    if buy(shopping_bag) == False :
        break
show(shopping_bag)
find(shopping_bag)
