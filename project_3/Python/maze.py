maze = open('maze.txt')

x = 0
y = 0
inc = 32

for r in maze:
    for c in r:
        print(c,end = "")
##        if x == 480:
##            x = 0
##        else:
##            x += inc
##        print (x,y)
##    y += inc