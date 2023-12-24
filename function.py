import sys 
from heapq import heapify ,heappush , heappop

def algo(graph , start,end):
    inf = sys.maxsize
    node={'A':{'Current':inf,'Next':[]}, {'B':{'Current':inf,'Next':[]}} , {'C':{'Current':inf,'Next':[]}},{'D':{'Current':inf,'Next':[]}}
    }


if __name__="__main__":
    graph=
    {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':2},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2}

    }

start = 'A'
end = []


