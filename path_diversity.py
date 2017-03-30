import networkx as nx
import sys

G = nx.DiGraph()
MAX_AS_LENGTH = 10

def bfs_path(s,d,max_length):
    g = nx.DiGraph(G)
    visited = set()
    queue = []
    # instead of adding node to queue, now adding path to queue
    # here we want to trace back path after finding the target node d
    queue.append([s])
    valid_path = []
    idx =0
    while idx < len(queue):
        path = queue[idx]
	idx +=1
        v = path[-1]
        # the vertex is now the last node in a path
        if v not in visited:
            for n in g.neighbors(v):
                if n not in visited:
                    if ( g[v][n]['label'] == 3 or g[v][n]['label'] == 2):
                        #delete all the neighbor of x of n having nx == c2p or p2p
                        for x in g.neighbors(n):
                            if (g[n][x]['label'] == 1 or g[n][x]['label'] == 2):
                                g.remove_edge(n,x)
                                #print('delete',n,x)

                # for each new neighbor discovered, a new path will be created
                # each new path then added to the queue
                # by doing so we can trace all the path that have been investigate
                # we will stop the checking when 1> we meet the destination d, or 2> we reach a certain path length
                # if the limit on path length is set to 5, then stop discovery when having a new path with length = 6
                new_path=list(path)
                new_path.append(n)
                if n == d:
                    #print('found path ',new_path)
                    valid_path.append(new_path)
                if len(new_path) == max_length+1:
                    #print('path',new_path)
                    break
                queue.append(new_path)
            visited.add(v)

    return valid_path

def disjoint_path(paths):
    v = set()
    path = []
    for p in paths:
        repeated = False
	tmp_v = set()
        for i,n in enumerate(p):
            if (i > 0 and i < (len(p)-1)):
                tmp_v.add(n)
		if n in v:
                    repeated = True
                    break
        if not repeated:
            path.append(p)
	    v = v.union(tmp_v)
    return path

def print_path(paths,op,f):
    op.append(str(len(paths)))
    if len(paths) != 0:
        for p in paths:
            op.append(str(p).strip('[]'))
            op.append(str(len(p)))

    delimiter = ';'
    #print(delimiter.join(op))
    f.write(delimiter.join(op))
    f.write('\n')

net_topo_f = 'network'
src_dst_f =  sys.argv[1]
output_f = src_dst_f+'_result'

with open(net_topo_f,'r') as f:
    reader = f.readlines()
    for line in reader:
        s = line.split()
        G.add_edge(s[0],s[1],weight=s[2],label=int(s[3]))

sd = []
with open(src_dst_f,'r') as f:
    reader = f.readlines()
    for line in reader:
        s = line.split()
        sd.append(s)

print('number of edges',G.number_of_edges())
print('number of nodes',G.number_of_nodes())

with open(output_f,'w') as f:
    for n in sd:
        s = n[0]
        d = n[1]
        paths = bfs_path(s,d,MAX_AS_LENGTH)
        dj_paths = disjoint_path(paths)
        output=[s]
        output.append(d)
        print_path(dj_paths,output,f)
    print('finish')
