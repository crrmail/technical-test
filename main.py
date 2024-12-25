#Print is a function that receive y as input to print y*y square with capital N
def Print(y):
    square = ""
    for i in range(y):
        for j in range(y):
            if j == 0:
                square += "X"
            elif i == j:
                square += "X"
            elif j == (y - 1):
                square += "X"
            else:
                square += "O"
        square += "\n"
    print(square)
    
#You can specify your wanted "y" value here.
y = 5
Print(y)