from random import randint

class matrix:
    def __init__(self, size, body=None):
        self.size = size
        self.body = [[y for y in range((size)*x+1, (size)*x+size+1)] for x in range(size)] if not(body) else body

def rot(mat, section=None):
    if not(section):
        section = (0, mat.size)

    origin, size = section[0], section[1]-1 #-1 to account for python's origin indexed arrays
    body = [row for row in mat.body]
    body_ = [row[::] for row in body] #copy of body

    if size+1 >= 2:
        #take care of corners
        body[origin][origin] = body_[origin][size] #right upper corner to left upper corner
        body[size][origin] = body_[origin][origin] #left upper corner to left lower corner
        body[size][size] = body_[size][origin] #left lower corner to right lower corner
        body[origin][size] = body_[size][size] #right lower corner to right upper corner
    if size+1 > 2:
        for x in (origin, size):
            for y in range(origin, size):
                if y > origin and y < size: 
                    body[x][y] = body_[y][size-x]
                    body[y][x] = body_[x][y]

        rot(mat, (1, size))
    
    
       
        

        

def mprint(mat):
    for row in mat:
        print(row)
        
a = matrix(4)
mprint(a.body)
rot(a)
mprint(a.body)

#apprently python is so cool that you can rotate a matrix just by doing:
reveresed(list(zip(*a)))
