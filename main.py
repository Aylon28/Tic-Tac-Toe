def print_field():
    print('---------')
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            if tic_tac[i][j] == '_':
                print(' ', end=' ')
            else:
                print(str(tic_tac[i][j]), end=' ')
        print('|')
    print('---------')


tic_tac = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
filling = 'X'
print_field()

while True:
    while True:
        while True:
            try:
                inp_ = input('Enter the coordinates: ').split()
                x = int(inp_[0])
                y = int(inp_[1])
                break
            except:
                print('You should enter numbers!')
        if x < 1 or x > 3 or y < 1 or y > 3:
            print('Coordinates should be from 1 to 3!')
        else:
            break
    if tic_tac[x - 1][y - 1] == '_':
        tic_tac[x - 1][y - 1] = filling
        if filling == 'X':
            filling = 'O'
        else:
            filling = 'X'
    else:
        print('This cell is occupied! Choose another one!')
    print_field()
    X_S = 0
    O_S = 0
    for i in range(3):
        for j in range(3):
            if tic_tac[i][j] == 'X':
                X_S += 1
            elif tic_tac[i][j] == 'O':
                O_S += 1
    if abs(X_S - O_S) >= 2:
        print('Impossible')
        break
    else:
        X_S = 0
        O_S = 0
        for i in range(3):
            if tic_tac[i][0] == tic_tac[i][1] == tic_tac[i][2]:
                if tic_tac[i][0] == 'X':
                    X_S += 1
                elif tic_tac[i][0] == 'O':
                    O_S += 1
            if tic_tac[0][i] == tic_tac[1][i] == tic_tac[2][i]:
                if tic_tac[0][i] == 'X':
                    X_S += 1
                elif tic_tac[0][i] == 'O':
                    O_S += 1
        if tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2] or tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0]:
            if tic_tac[1][1] == 'X':
                X_S += 1
            elif tic_tac[1][1] == 'O':
                O_S += 1
        if X_S + O_S > 1:
            print('Impossible')
            break
        elif X_S == 1:
            print('X wins')
            break
        elif O_S == 1:
            print('O wins')
            break
        else:
            for row in tic_tac:
                if '_' in row:
                    break
            else:
                print('Draw')
                break
