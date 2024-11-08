class Graph:
    def __init__(self,in_n,out,weights={}):
        self.in_neighbors = in_n
        self.out_neighbors = out
        self.weights = weights #maps f"{source}:{dest}" to the weight

# I am making the case for 2 functions. One has weights and one does not. 
# One is a CSV and one is not. 
def loadNetwork_txt():
    with open('soc-Epinions1.txt', 'r') as file:
        in_neighbors = {}
        out_neighbors = {}
        for line in file: #iterate over lines of files
            if not (line[0] == '#'): # lines starting with '#' are comments, ignore those
                source,dest = line.split()
                in_l = in_neighbors.get(dest,[]) # get or defualt the empty list
                in_l.append(source) # add a to the adj. list
                in_neighbors[dest] = in_l
                out_l = out_neighbors.get(source,[]) #do the same for out_neighbors
                out_l.append(dest)
                out_neighbors[source] = out_l
                #no weights on this graph!
    res = Graph(in_neighbors, out_neighbors) #create the graph and return it
    return res

def loadNetwork_csv():
    with open('soc-sign-bitcoinotc.csv', 'r') as file:
        in_neighbors = {}
        out_neighbors = {}
        weights = {} #maps f"{source}:{dest}" to the weight
        for line in file: #iterate over lines in the file
            source, dest, weight, timestamp = line.split(',') # get everything but ignore the timestamp
            in_l = in_neighbors.get(dest,[]) # get or defualt the empty list
            in_l.append(source) # add a to the adj. list
            in_neighbors[dest] = in_l
            out_l = out_neighbors.get(source,[]) #do the same for out_neighbors
            out_l.append(dest)
            out_neighbors[source] = out_l
            weight_str = f"{source}:{dest}" #note that this is directed from the specification. 
            #The same weight does not exist for f"{dest}:{source}"
            weights[weight_str] = weight
        res = Graph(in_neighbors, out_neighbors,weights) #create the graph and return it
        return res

loadNetwork_csv()