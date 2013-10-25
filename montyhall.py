__author__ = 'Pavel Popov'

import random
import sys


def check_solution(choice, change):
    change_f = lambda x: 1 if x == 0 else 0
    if change:
        choice = change_f(choice)
    return choice == 0


def montyhall(doors, change):
    do_choice = lambda x: random.randint(0, x-1)
    choice = 0 if do_choice(doors) == do_choice(doors) else 1
    return 1 if check_solution(choice, change) else 0


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'timeit':
        import timeit
        number=10
        print(timeit.timeit("sum([montyhall(3,True) for i in range(1000)])",
                            number=number,
                            setup="from __main__ import montyhall"))
        print(timeit.timeit("sum([montyhall(3,False) for i in range(1000)])",
                            number=number,
                        setup="from __main__ import montyhall"))
    else:
        print('Changed - %d' % sum([montyhall(3,True) for i in range(1000)]));
        print('Not Changed - %d' % sum([montyhall(3,False) for i in range(1000)]));


