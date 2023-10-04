# Pattern questions

# Question- 1 : https://takeuforward.org/wp-content/uploads/2022/08/P1.png

for rows in range(1, 6):
    for cols in range(1, 6):
        print("*", end="")
    print()

# Question- 2 : https://takeuforward.org/wp-content/uploads/2022/08/P2.png

for rows in range(1, 6):
    for cols in range(1, rows+1):
        print("*", end="")
    print()

# Question- 3 : https://takeuforward.org/wp-content/uploads/2022/08/P3.png

for rows in range(1, 6):
    for cols in range(1, rows+1):
        print(cols, end="")
    print()

# Question- 4 : https://takeuforward.org/wp-content/uploads/2022/08/P4.png

for rows in range(1, 6):
    for cols in range(1, rows+1):
        print(rows, end="")
    print()

# Question- 5 : https://takeuforward.org/wp-content/uploads/2022/08/P5.png

for rows in range(1, 6):
    for cols in range(1, 7-rows):    # for cols in range(7-rows, 0, -1)
        print("*", end="")
    print()

# Question- 6 : https://takeuforward.org/wp-content/uploads/2022/08/P6.png

for rows in range(1, 6):
    for cols in range(1, 7-rows):
        print(cols, end="")
    print()

# Question- 7 : https://takeuforward.org/wp-content/uploads/2022/08/P7.png

for rows in range(1, 6):
    for spaces in range(4-rows, -1, -1):
        print(" ", end="")
    for cols in range(1, rows+1):
        print('*', end="")
    for cols in range(rows-1, 0, -1):
        print("*", end="")
    for spaces in range(4-rows, -1, -1):
        print(" ", end="")
    print()

# Question- 8 : https://takeuforward.org/wp-content/uploads/2022/08/P8.png

for rows in range(1, 6):
    for spaces in range(0, rows-1):
        print(" ", end="")
    for cols in range(1, 7-rows):
        print("*", end="")
    for cols in range(1, 6-rows):
        print("*", end="")
    for spaces in range(0, rows-1):
        print(" ", end="")
    print()

# Question- 9 : https://takeuforward.org/wp-content/uploads/2022/08/P9.png

for rows in range(1, 6):
    for spaces in range(4-rows, -1, -1):
        print(" ", end="")
    for cols in range(1, rows+1):
        print('*', end="")
    for cols in range(rows-1, 0, -1):
        print("*", end="")
    for spaces in range(4-rows, -1, -1):
        print(" ", end="")
    print()
for rows in range(1, 6):
    for spaces in range(0, rows-1):
        print(" ", end="")
    for cols in range(1, 7-rows):
        print("*", end="")
    for cols in range(1, 6-rows):
        print("*", end="")
    for spaces in range(0, rows-1):
        print(" ", end="")
    print()

# Question- 10 : https://takeuforward.org/wp-content/uploads/2022/08/P10.png

for rows in range(1, 6):
    for cols in range(1, rows+1):
        print("*", end="")
    print()
for rows in range(1, 5):
    for cols in range(4-rows, -1, -1):
        print("*", end="")
    print()


# Question- 11 : https://takeuforward.org/wp-content/uploads/2022/08/P11.png

for rows in range(1, 6):
    if rows % 2 != 0:
        for cols in range(1, rows+1):
            if cols % 2 != 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
    else:
        for cols in range(1, rows+1):
            if cols % 2 != 0:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()

# Question- 12 : https://takeuforward.org/wp-content/uploads/2022/08/P12.png

for rows in range(1, 5):
    for cols in range(1, rows+1):
        print(cols, end="")
    for spaces in range(rows, 8-rows):
        print(" ", end="")
    for cols in range(rows, 0, -1):
        print(cols, end="")
    print()

# Question- 13 : https://takeuforward.org/wp-content/uploads/2022/08/P13.png

Count = 1
for rows in range(1, 6):
    for cols in range(1, rows+1):
        print(Count, end=" ")
        Count += 1
    print()

# Question- 14 : https://takeuforward.org/wp-content/uploads/2022/08/P14.png

for rows in range(1, 6):
    for cols in range(1, rows+1):
        print(chr(cols+64), end="")
    print()

# Question- 15 : https://takeuforward.org/wp-content/uploads/2022/08/P15.png

for rows in range(1, 6):
    for cols in range(1, 5-rows):
        print(chr(cols+64), end="")
    print()

# Question- 16 : https://takeuforward.org/wp-content/uploads/2022/08/P16.png

for rows in range(1, 6):
    for cols in range(1, rows+1):
        print(chr(rows+64), end="")
    print()

# Question- 17 : https://takeuforward.org/wp-content/uploads/2022/08/P17.png

for rows in range(1, 5):
    for spaces in range(5, rows, -1):
        print(" ", end="")
    for cols in range(1, rows+1):
        print(chr(64+cols), end="")
    for cols in range(rows, 1, -1):
        print(chr(cols+63), end="")
    print()

# Question- 18 : https://takeuforward.org/wp-content/uploads/2022/08/P18.png

for rows in range(1, 6):
    for cols in range(rows+1, 1, -1):
        print(chr(71-cols), end="")
    print()

# Question- 19 : https://takeuforward.org/wp-content/uploads/2022/08/P19.png

for rows in range(1, 6):
    for cols in range(6-rows, 0, -1):
        print("*", end="")
    for spaces in range(rows, 1, -1):
        print(" ", end="")
    for spaces in range(rows, 1, -1):
        print(" ", end="")
    for cols in range(5-rows, -1, -1):
        print("*", end="")
    print()
for rows in range(1, 6):
    for cols in range(1, rows+1):
        print("*", end="")
    for spaces in range(rows, 10-rows):
        print(" ", end="")
    for cols in range(rows, 0, -1):
        print("*", end="")
    print()

# Question- 20 : https://takeuforward.org/wp-content/uploads/2022/08/P20.png

for rows in range(1, 6):
    for cols in range(1, rows+1):
        print("*", end="")
    for spaces in range(rows, 10-rows):
        print(" ", end="")
    for cols in range(rows, 0, -1):
        print("*", end="")
    print()
for rows in range(1, 5):
    for cols in range(5, rows, -1):
        print("*", end="")
    for spaces in range(rows*2):
        print(" ", end="")
    for cols in range(1, 6-rows):
        print("*", end="")
    print()

# Question- 21 : https://takeuforward.org/wp-content/uploads/2023/01/Screenshot-2023-01-02-at-1.54.55-PM-1.jpg

for rows in range(1, 5):
    if rows == 1 or rows == 4:
        for cols in range(1, 5):
           print("*", end=" ")
    else:
        for cols in range(1, 5):
            if cols == 1 or cols == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

# Question- 22 : https://takeuforward.org/wp-content/uploads/2022/08/P22.png

n = 4
for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        top = i
        bottom = j
        right = (2 * n - 2) - j
        left = (2 * n - 2) - i
        
        print((n - min(min(top, bottom), min(left, right))), end=" ")
    print()


    

    