from queue import PriorityQueue     # 底层是小根堆，优先输出最小值
q = PriorityQueue()
for i in range(10, 0, -1):
    q.put((i, i*i))
while not q.empty():
    print(q.get(), end=" ")
"""
(1, 1) (2, 4) (3, 9) (4, 16) (5, 25) (6, 36) (7, 49) (8, 64) (9, 81) (10, 100) 
"""
