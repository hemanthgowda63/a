def near_vertex(d,vt):
    min=999
    for i in range(len(d)):
        if i not in vt:
            if d[i]<min:
                min=d[i]
                v=i
    return v

def path(v,pv,a):
    if pv[v]!=-1:
        a.append(pv[v])
        path(pv[v],pv,a)

def print_paths(d,pv):
    for i in range(len(d)):
        print
    print("path to vertex:",i)
    a=[]
    path(i,pv,a)
    a.reverse()
    a.append(i)
    print(a)

def dijkstra(graph):
    n=len(graph)
    d=[]
    pv=[]
    vt=[]
    for i in range(n):
        d.append(999)
        pv.append(-1)
        s=0
        d[s]=0
        for i in range(n):
            v=near_vertex(d,vt)

            vt.append(v)
            adj_vertex=graph[v]
            for val in adj_vertex:
                if val[0] not in vt:
                    if d[v]+val[1]<d[val[0]]:
                        d[val[0]]=d[v]+val[1]
                        pv[val[0]]=v
    print_paths(d,pv)

graph={0:[[3,7]],1:[[2,4]],2:[[4,6]],3:[[1,2],[2,5]],
4:[[3,4]]}

dijkstra(graph)
