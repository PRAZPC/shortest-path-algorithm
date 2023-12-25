import sys 
from heapq import heapify ,heappush , heappop

def algo(graph , start,end):
    inf = sys.maxsize
    node={{'A':{'Current':inf,'Next':[]}}, {'B':{'Current':inf,'Next':[]} }, {'C':{'Current':inf,'Next':[]}},{'D':{'Current':inf,'Next':[]}}
    }
    node[start]['Current']=0
    visited = []
    temp = start 
    for i in range(5):
        if temp not in visited :
            visited.append(temp)
            min =[]
            for j in graph[temp]:
                if j not in visited :
                    Current = node[temp]['Current'] + graph[temp][j]




if __name__=="__main__":
    graph = {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22} ,
        'E':{'C':5,'D':11 ,'F':1},
        'F': {'D':22,'E':1}

    }

start = 'A'
end = 'F'



