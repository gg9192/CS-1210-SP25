# I am making the case for 2 functions. One has weights and one does not. 
# One is a CSV and one is not. different format so hard to do one function
# without doing some crazy hack. Just provide the correct one as the solution 
# is the better approach IMHO
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
    res = [in_neighbors, out_neighbors]
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
        res = res = [in_neighbors, out_neighbors,weights] #create the graph and return it
        return res

def getActiveNeighbors(graph, node: str, activeSet:set):
    # I assume that you pass in an instance of my graph object
    res = set()
    in_edges = graph[0].get(node, []) # get all the nodes that have an edge to this node
    for node in in_edges: 
        if node in activeSet: 
            res.add(node)
    return res