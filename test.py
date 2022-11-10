import queue
from re import A


from collections import deque

# 튜플이나 리스트나 x,y로 할당하면 변수하나에 요소하나씩 들어간다
a = [10, 20, 1]
x, y, z = a
print(x, y, z)

queue = deque()
queue.append((1, 2))
print(queue)
a, b = queue.popleft()
print(a, b)


q=deque([1])
q.append(0)
print(q)
a=q.popleft()
print(a)
