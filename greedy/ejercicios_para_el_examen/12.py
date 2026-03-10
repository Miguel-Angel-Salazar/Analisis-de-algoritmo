import heapq

def min_salas(intervalos):

    intervalos.sort(key=lambda x: x[0])

    heap = []

    for inicio, fin in intervalos:

        if heap and heap[0] <= inicio:
            heapq.heappop(heap)

        heapq.heappush(heap, fin)

    return len(heap)