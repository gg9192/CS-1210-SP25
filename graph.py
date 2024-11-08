class Graph:
    def __init__(self,in_n,out,weights={}):
        self.in_neighbors = in_n
        self.out_neighbors = out
        self.weights = weights

# I am making the case for 2 functions. One has weights and one does not. 
# One is a CSV and one is not. 
def loadNetwork_txt():
    with open('soc-Epinions1.txt', 'r') as file:
        in_neighbors = {}
        out_neighbors = {}
        for line in file: #iterate over lines of files
            if not (line[0] == '#'): # lines starting with '#' are comments, ignore those
                a,b = line.split()
                in_l = in_neighbors.get(b,[]) # get or defualt the empty list
                in_l.append(a) # add a to the adj. list
                in_neighbors[b] = in_l
                out_l = out_neighbors.get(a,[]) #do the same for out_neighbors
                out_l.append(b)
                out_neighbors[a] = out_l
                #no weights on this graph!
    res = Graph(in_neighbors, out_neighbors) #create the graph and return it
    return res



def loadNetwork_csv():
    pass

g = loadNetwork_txt()
print(g.out_neighbors)