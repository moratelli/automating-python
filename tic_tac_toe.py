import pprint

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

the_board['mid-M'] = 'X'
the_board['top-L'] = 'O'
the_board['top-M'] = 'O'
the_board['top-R'] = 'O'
the_board['mid-L'] = 'X'
the_board['low-R'] = 'X'


def print_board(board):
    print(board['top-L'] + " | " + board['top-M'] + " | " + board['top-R'])
    print("---------")
    print(board['mid-L'] + " | " + board['mid-M'] + " | " + board['mid-R'])
    print("---------")
    print(board['low-L'] + " | " + board['low-M'] + " | " + board['low-R'])


print_board(the_board)
