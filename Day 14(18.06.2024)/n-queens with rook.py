'''i/p: 6*6                     6*6
        2                       2 3
        _ _ _ _ _ r             q _ _ _ _ _
        q _ _ _ _ _             _ _ q _ _ _
        _ _ q _ _ _             _ _ _ r _ _ 
        _ _ _ _ q _             _ _ _ _ _ q
        _ q _ _ _ _             _ q _ _ _ _
        _ _ q _ _ _             _ _ _ _ q _
'''
'''def n_queens(n):
    ans=[]
    col=[]
    posdiag=[]
    negdiag=[]
    board=[['.']*n for i in range(n)]
    def backtrack(r):
        if r==n:
            l=[" ".join(i) for i in board]
            ans.append(l)
            return
        for c in range(n):
            if c in col or (r+c) in posdiag or (r-c) in negdiag:
                continue
            board[r][c]='Q'
            col.append(c)
            posdiag.append(r+c)
            negdiag.append(r-c)
            
            backtrack(r+1)
            
            board[r][c]="."
            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
    backtrack(0)
    return ans
n=int(input())'''


'''
ip:
   6*6-->square matrix
   (2,3)-->rooq position
  
   - - - - - r     q - - - - -
   q - - - - -     - - q - - -
   - - q - - -     - - - r - -
   - - - - q -     - - - - - q
   - q - - - -     - q - - - - 
   - - - q - -     - - - - q -
   
   queen(q) cannot be placed in same row,col,diagnol
   if rooq(elephant) present in any of the row the queen can't be placed in the row and col
'''

'''def is_valid(board, row, col, n,p,q):
    for i in range(col):# check horizontal
        if board[row][i] == 'q' or row==p or i==q:
            return False
    i = row
    j = col
    while i>=0 and j >= 0 : # upper left diag
        if board[i][j] == 'q':
            return False
        i -= 1 
        j -= 1 
    i = row
    j = col
    while i<n and j >=0: #bottom left diag
        if board[i][j] == 'q':
            return False
        i += 1 
        j -= 1
        
    return True
def solve(n,p,q): 
    board = [['-' for i in range(n)] for j in range(n)]
    def backtrack(col):
        if col == n:
            return True
        for i in range(n):
            if is_valid(board, i, col, n,p,q):
                board[i][col] = 'q'
                
                if backtrack(col+1):
                    return True
                
                board[i][col] = '-'
        
        return False
    
    if backtrack(0):
        for row in board:
            print("".join(row))
    else:
        print("no solution")
p=int(input())
q=int(input())
solve(n,p,q)'''

'''
ip:
   6*6-->square matrix
   (2,3)-->rooq position
  
   - - - - - r     q - - - - -
   q - - - - -     - - q - - -
   - - q - - -     - - - r - -
   - - - - q -     - - - - - q
   - q - - - -     - q - - - - 
   - - - q - -     - - - - q -
   
   queen(q) cannot be placed in same row,col,diagnol
   if rooq(elephant) present in any of the row the queen can't be placed in the row and col
'''

def is_valid(board, row, col, n):
    for i in range(col):# check horizontal
        if board[row][i] == 'q':
            return False
    i = row
    j = col
    while i>=0 and j >= 0: # upper left diag
        if board[i][j] == 'q':
            return False
        i -= 1 
        j -= 1 
    i = row
    j = col
    while i<n and j >=0: #bottom left diag
        if board[i][j] == 'q':
            return False
        i += 1 
        j -= 1
        
    return True
def solve(n,max):
    board = [['-' for i in range(n)] for j in range(n)]
    def backtrack(col,max):
        if col == n:
            return True
        for i in range(n):
            if is_valid(board, i, col, n):
                board[i][col] = 'q'
                max=max+1
                if backtrack(col+1,max):
                    return True
                
                board[i][col] = '-'
        print(max)
        return False
    
    if backtrack(0,max):
        for row in board:
            print("".join(row))
    else:
        print("no solution")
n = int(input())
solve(n,0)