def rep_char(c,n):
    print(c*n)

def draw_line_string(msg):
    msg1=f'Hello {msg},'
    msg2='Welcome to Seoul.'
    nstr=len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(f'{msg1}\n{msg2}')
    rep_char('-',nstr)

name=input('Input his/her name: ')
draw_line_string(name)
