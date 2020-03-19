import heapq

F=[20,58,60,32,12]
heapq.heapify(F)


print(F)

heapq.heappush(F,80)
print(F)

heapq.heappop(F)
print(F)