def find_set(all_set,key):

    for i in range(len(all_set)):
        if key in all_set[i]:
            return i

def kruskal(edge,v):
    edge.sort(key=lambda x:x[2])
    all_set=[ ]
    for k in vert:
        a=[]
        a.append(k)
        all_set.append(a)
    st_edge=[]
    i=0
    ct=0
    while ct<n-1:
        x=edge[i][0]
        y=edge[i][1]
        s1=find_set(all_set,x)
        s2=find_set(all_set,y)
        if s1!=s2:
            a=[]
            a.append([x,y,edge[i][2]])
            st_edge.append(a)
            all_set[s1]=all_set[s1]+all_set[s2]
            del all_set[s2]
            ct=ct+1
        i=i+1
    return st_edge
    #	driver code
#//first write the example graph and then take input to the program from the same graph.
edge=[['a','b',5],['b','d',6],['c','d',4],['a','c',7
],['a','e',2],['b','e',3],['d','e',5],['c','e',4]]
vert=['a','b','c','d','e']
n=len(vert)
st_edge=kruskal(edge,vert)
print(st_edge)
