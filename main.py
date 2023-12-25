from function import algo
from heapq import heapify ,heappush , heappop


if __name__=="__main__":
    graph= {
        'A':{'B':1,'C':2,'E':11},
        'B':{'A':1,'C':8,'D':2},
        'C':{'A':2,'B':8,'E':3,'D':2},
        'D':{'B':8,'C':2,'E':10,'F':15} ,
        'E':{'C':3,'D':10 ,'F':1,'A':11},
        'F': {'D':15,'E':1}

    }
algo(graph,'A','D')

