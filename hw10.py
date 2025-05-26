import pickle

filename = 'score.bin'

def input_scores() :
    print('[점수 입력]')
    score = []
    i = 1
    while True:
        a = int(input(f'#{i}? '))
        if a > -1:
            score.append(a)
            i += 1
        else :
            return score

def get_average(lst)  :
    su = 0
    for i in lst:
       su += i
    aver = su/len(lst)
    return aver

def show_scores(lst):
    for i in lst:
        print(i, end =' ')
    print()

def show(lst):
    print()
    print('[점수 출력]')
    aver = get_average(lst)
    print('개인점수:', end=' ')
    show_scores(lst)
    print(f'평균: {aver:.1f}')
    print()

def save_data(lst, filepath):
    with open(filepath, 'wb') as file:
            pickle.dump(lst, file)


def load_data(filepath) :
    with open (filepath, 'rb') as file:
        score = pickle.load(file)

        return score


# 주프로그램부

import os

if os.path.exists(filename):
    print('[파일읽기]')
    score = load_data(filename)
    show(score)
else:
    score = input_scores()
    show(score)
    save_data(score, filename)
            
