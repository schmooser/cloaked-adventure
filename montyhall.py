__author__ = 'Pavel Popov'

import random
#import matplotlib.pyplot as plt


def set_choices(doors=3):
    correct_choice = -1
    choices = [0 for i in range(doors)]
    random.seed()
    for i in range(doors):
        if random.random() >= 1.0-1.0/float(doors):
            choices[i] = 1
            correct_choice = i
            break
    if correct_choice == -1:
        choices[-1] = 1
        correct_choice = doors-1
    return (choices, correct_choice)


def do_choice(doors=3):
    random.seed()
    return random.randint(0, doors-1)


def remove_choices(choices, choice):
    random.seed()

    if choice == choices[1]:  # chosen correct choice
        choice = 0
    else:
        choice = 1

    return {'choices': [1,0], 'choice': choice, 'correct_choice': 0}


def check_solution(choices, change):
    change_f = lambda x: 1 if x == 0 else 0

    if change:
        choices['choice'] = change_f(choices['choice'])

    return choices['choice'] == choices['correct_choice']


def montyhall(doors=3, change=True):
    choices = set_choices(doors)
    choice = do_choice(doors)
    new_choices = remove_choices(choices, choice)
    res = check_solution(new_choices, change)
    return 1 if res else 0
    # print check_solution(new_choices, True)

def central_limit_theorem(series_length, num_of_series):
    n = series_length
    data = []
    for i in range(num_of_series):
        data.append([random.random() for x in range(n)])
    sum_of_i = lambda i: sum([data[j][i] for j in range(num_of_series)])
    data_sum = map(sum_of_i, range(n))

    #plt.hist(data_sum, bins=500)
    #plt.show()

#if __name__ == '__main__':
    # central_limit_theorem(50000, 50)
    #print sum([montyhall(3,True) for i in range(1000)])
    #print sum([montyhall(3,False) for i in range(1000)])

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("sum([montyhall(3,True) for i in range(1000)])",
                        number=10,
                        setup="from __main__ import montyhall"))
    print(timeit.timeit("sum([montyhall(3,False) for i in range(1000)])",
                        number=10,
                        setup="from __main__ import montyhall"))
