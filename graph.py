import os # comes with python itself

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
    
def loadNetwork(filename):
    with open(filename, 'r') as file:
        in_neighbors = {}
        out_neighbors = {}
        ext = filename.split('.')[-1] # get the extention
        for line in file: #iterate over lines in the file
            data = [] 
            if ext == 'csv':
                data = line.split(',')
            elif ext == 'txt':
                data = line.split()
            source, dest, weight, = 0,0,0
            if len(data) >= 3: # weighted case
                source, dest, weight = data[0], data[1], data[2]
            else: # unweighted
                source, dest, weight = data[0], data[1], 1 # get the data

            # in neighbors
            in_l = in_neighbors.get(dest,set) # get or defualt the empty set
            strr = f"{source}:{weight}"
            in_l.add(strr)
            in_neighbors[dest] = in_l
            # out neighbors
            out_l = in_neighbors.get(source,set) # get or defualt the empty set
            strr = f"{dest}:{weight}"
            out_l.add(strr)
            out_neighbors[dest] = out_l
    return [in_neighbors, out_neighbors]

def getActiveNeighbors(graph, node: str, activeSet:set):
    res = set()
    in_edges = graph[0].get(node, set) # get all the nodes that have an edge to this node
    for node in in_edges: 
        if node in activeSet: 
            res.add(node)
    return res


if __name__ == "__main__":
    file = ""
    for _ in range(2):
        fn = input('please enter the file name\n')
        if fn not in os.listdir():
            continue
        else:

            exit(0)

    print('No valid file name was entered, goodbye')