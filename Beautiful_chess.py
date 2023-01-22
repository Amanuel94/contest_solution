T = int(input())

for i in range(T):
    
    input()
    board = []
    
    def func(board):
        for i in range(1, 7):
            for j in range(1,7):
                TL = board[i-1][j-1] == "#"
                TR = board[i-1][j+1] == "#"
                
                if (TL and TR):
                    return i+1, j+1
                    
    
    for i in range(8):
        board.append(input())
        
    print(func(board)[0],func(board)[1])
        
    

           
