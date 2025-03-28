def get_fixed_price(discount_rate, price) :
    fixed_price=price/(1-discount_rate/100)
    return fixed_price

discount_rate=int(input('할인율은? '))
a_price=int(input('A 상품의 할인된 가격은? '))
b_price=int(input('B 상품의 할인된 가격은? '))

a_fixed_price=get_fixed_price(discount_rate, a_price)
b_fixed_price=get_fixed_price(discount_rate, b_price)

print('A 상품의 정가는', a_fixed_price, '원')
print('B 상품의 정가는', b_fixed_price, '원')
