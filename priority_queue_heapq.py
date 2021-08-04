from heapq import heappush, heappop, heapify

# heap[0] is smallest
# heapq.heappush(heap, item)
# heapq.heappop(heap) # return smallest
# heapq.heappushpop(heap, item) # == push + pop
# heap[0] # peek smallest
# heapq.heapify(list())
# heap.heapreplace(heap, item) # == pop + push
# heapq.merge(*iterables, key=None, reverse=False)
# heapq.nlargest(n, iterable, key=None)

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]

l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(heapsort(l))
l2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(l2)
print(l2)

h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
print(h)
heappop(h)
print(h)