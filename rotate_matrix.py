from random import randint

class matrix:
    def __init__(self, size, body=None):
        self.size = size
        self.body = [[y for y in range((size)*x+1, (size)*x+size+1)] for x in range(size)] if not(body) else body

def rot(mat, section=None):
    if not(section):
        section = ((0, 0), (mat.size, mat.size))
        
    size = mat.size-1 #-1 to account for python's 0 indexed arrays
    body = mat.body
    
    if size+1 == 1:
        return mat 
    elif size+1 == 2:
        #hardcoded rotate for 2x2 matrix
        body = [[body[0][1], body[1][1]], [body[0][0], body[1][0]]]
        return matrix(size+1, body)
    else:
        #take care of corners
        corner1 = body[0][0] #remember left upper corner
        body[0][0] = body[0][size] #right upper corner to left upper corner
        corner2 = body[size][0] #remember left lower corner
        body[size][0] = corner1 #left upper corner to left lower corner
        corner3 = body[size][size] #remember right lower corner
        body[size][size] = corner2 #left lower corner to right lower corner
        body[0][size] = corner3 #right lower corner to right upper corner
        
        rot(mat, ((1, 1), (size-1, size-1)))
        
        return matrix(size+1, body)
        

        

def mprint(mat):
    for row in mat:
        print(row)
a = matrix(3)
mprint(a.body)
print()
mprint(rot(a).body)
