import sys
from heapq import heapify, heappush, heappop

def algo(graph, start, end):
    inf = sys.maxsize
    node = {
        'A': {'Current': inf, 'Next': []},
        'B': {'Current': inf, 'Next': []},
        'C': {'Current': inf, 'Next': []},
        'D': {'Current': inf, 'Next': []},
        'E': {'Current': inf, 'Next': []},
        'F': {'Current': inf, 'Next': []}
    }
    node[start]['Current'] = 0
    visited = []
    temp = start
    for i in range(5):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    Current = node[temp]['Current'] + graph[temp][j]
                    if Current < node[j]['Current']:
                        node[j]['Current'] = Current
                        node[j]['Next'] = node[temp]['Next'] + [temp]
                    heappush(min_heap, (node[j]['Current'], j))
            heapify(min_heap)
            temp = min_heap[0][1]
    print('short distance is ', str(node[end]['Current']))
    print('shortest path is ', str(node[end]['Next'] + [end]))



   