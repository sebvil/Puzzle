def read_grid(filename):
    s = open(filename).readlines()
    t = []
    for i in s:
        temp = i.strip().split("\t")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        t.append(temp)
    return t

def check(grid):
    temp = []
    for i in range(len(grid)):
        temp_row = []
        row = grid[i]
        for j in range(len(row)):
            sum = 0
            if i > 0:
                sum += grid[i-1][j]
            if i < len(grid) - 1:
               sum += grid[i+1][j]
            if j > 0:
                sum += grid[i][j-1]
            if j < len(row) - 1:
               sum += grid[i][j+1]

            print(i, j, sum)
            if sum == 9:
                temp_row.append("0")
            else:
                temp_row.append(" ")
        temp.append(temp_row)
    return temp
if __name__== "__main__":
    y =read_grid("t9.txt")
    x = check(y)

    for i in x:
        print(i)
