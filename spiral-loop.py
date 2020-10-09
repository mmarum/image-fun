import json

# https://stackoverflow.com/questions/398299/looping-in-a-spiral

def spiral(X, Y):
    grid = []
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            grid.append([x, y])
            # DO STUFF...
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return grid

#grid = spiral(13, 13)

# NOTE: 15 is a great number
# for the gray-scale spiral
grid = spiral(15, 15)

# BUT: 35 might be a better number to use
# for the 35-pixel-wide facial display
# (uses the convert.py)
#grid = spiral(35, 35)

print(grid)

# This script should simply write out s var to file

f = open("grid.json", "w")
f.write(json.dumps(grid))
f.close()

# to be used by the html page
# Next few lines just show how js can iter thru s

for i in range(len(grid)):
    #print(i, grid[i])
    pass
