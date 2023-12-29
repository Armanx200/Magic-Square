def MagicSquare(n): #only works for odd numbers
    magicSquare = [[-1 for _ in range(n)] for _ in range(n)]
    row, col = n // 2, 0

    for i in range(1, n * n + 1):
        magicSquare[row][col] = i

        if i % n == 0:     #if magicSquare[row-1][col-1] != 0:
            col -= 1
        else:
            row -= 1
            col += 1
        row = (row + n) % n
        col = (col + n) % n

    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()

#---------- Main ----------#
MagicSquare(5)