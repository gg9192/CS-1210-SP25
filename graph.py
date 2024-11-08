class Graph:
    def __init__(self,in_n,out,weights={}):
        self.in_neighbors = in_n
        self.out_neighbors = out
        self.weights = weights


def loadNetwork_txt():
    with open('soc-Epinions1.txt', 'r') as file:
        in_neighbors = {}
        out_neighbors = {}
        for line in file:
            if not (line[0] == '#'):
                a,b = line.split()
                a.strip()
                b.strip()
                in_l = in_neighbors.get(b,[])
                in_l.append(a)
                in_neighbors[b] = in_l
                out_l = in_neighbors.get(a,[])
                out_l.append(b)
                out_neighbors[a] = out_l
                #no weights on this graph!
    res = Graph(in_neighbors, out_neighbors)
    return res



def loadNetwork_csv():
    pass


loadNetwork_txt()