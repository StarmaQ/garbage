from random import randint

class matrix:
    def __init__(self, size, body=None):
        self.size = size
        self.body = [[y for y in range((size)*x+1, (size)*x+size+1)] for x in range(size)] if not(body) else body

def rot(mat, section=None):
    if not(section):
        section = ((0, 0), (mat.size, mat.size))
        
    size = mat.size-1 #-1 to account for python's 0 indexed arrays
    body = [row for row in mat.body]
    body_ = body[::] #copy of body
    
    if size+1 == 2:
        #take care of corners
        body[0][0] = body_[0][size] #right upper corner to left upper corner
        body[size][0] = body_[0][0] #left upper corner to left lower corner
        body[size][size] = body_[size][0] #left lower corner to right lower corner
        body[0][size] = body_[size][size] #right lower corner to right upper corner
    if size+1 > 2:
        for i, row in enumerate(body):
            
        rot(mat, ((1, 1), (size-1, size-1)))
    
    
       
        

        

def mprint(mat):
    for row in mat:
        print(row)
a = matrix(2)
mprint(a.body)
rot(a)
mprint(a.body)
