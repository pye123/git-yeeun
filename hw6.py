def display_multiplication_table(n,m) :
    for i in range(1,10):
        for j in range(n,m+1):
            print(f'{j} x {i} = {j*i:2d}', end='    ')
        print()
    print()

display_multiplication_table(2,5)
display_multiplication_table(6,9)
