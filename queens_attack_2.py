"""
 @Author: hardcodecoder
 @Date:   07:25:32 Sunday 12 July 2020
 @Last modified by:   hardcodecoder
 @Last modified time: 07:26:32 Sunday 12 July 2020
 
"""

"""
Given a chess board of size N x N, Queen position (row number, column number).
Find the total number of cells the queen can attack.

Also find the total number of cells the queen can attack
if there are k obstancles in the chessboard.

Note: 
The obstacles may or may not be in the path of queen's attack.
There may be more than 1 obstacle in the same cell or in the same row/column/diagnol
It is gauranteed that no obstacle is present in the queen position
"""




n = int(input("Enter the size of the board: "))
qr,qc = map(int, input("Enter queens position (row column): ").split())

r1 = qc - 1     # row left of the queen
r2 = n - qc     # row right of the queen
c1 = qr - 1     # column bottom of the queen
c2 = n - qr     # column top of the queen

#Number of diagnol cell to attck
diagnol_bl = min(qr-1, qc-1)    # diagnol bottom leeft of the queen
diagnol_tr = min(n-qr, n-qc)    # diagnol top right of the queen

diagnol_br = min(qr-1, n-qc)    # diagnol bottom right of the queen
diagnol_tl = min(qc-1, n-qr)    # diagnol top left of the queen

# number of cells queen can attck
attack_without_ob = r1+r2+c1+c2+diagnol_bl+diagnol_tr+diagnol_br+diagnol_tl

k = int(input("Enter no. of obstacles: "))
print("Enter the row and column of each obstacle on each line")
obstacles_list = [list(map(int, input().split())) for i in range(k)]

for obstacle in obstacles_list:
    # obr => obstacle row number
    # obc => obstacle column number
    obr, obc = obstacle[0], obstacle[1]


    # Start cheking all rows and column
    # if obstacle is present update the 
    # number of attacking cell

    if obr == qr and obc < qc:
        r1 = min(r1, qc-obc-1)

    elif obr == qr and obc > qc:
        r2 = min(r2, obc-qc-1)

    elif obc == qc and obr < qr:
        c1 = min(c1, qr-obr-1)

    elif obc == qc and obr > qr:
        c2 = min(c2, obr-qr-1)

    # End of rows and columns check


    # Start checking all diagnols
    # if obstacle is present update the 
    # number of attacking cell
    elif obr < qr and obc < qc and qr-obr == qc-obc:
        diagnol_bl = min(diagnol_bl, qc-obc-1)
    
    elif obr < qr and obc > qc and qr-obr == obc - qc:
        diagnol_br = min(diagnol_br, obc-qc-1)

    elif obr > qr and obc < qc and obr-qr == qc-obc:
        diagnol_tl = min(diagnol_tl, qc-obc-1)
    
    elif obr > qr and obc > qc and obr-qr == obc-qc:
        diagnol_tr = min(diagnol_tr, obc-qc-1)

    # End of diagnols check


print("Cells the queen can attack without any obstaclles: ", attack_without_ob)

print("Cells the queen can attack with obstacles: ", r1+r2+c1+c2+diagnol_bl+diagnol_tr+diagnol_br+diagnol_tl)

 
