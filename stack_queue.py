stack = list(range(6))
stack.append(10)
stack.append(20)
stack.pop()

from collections import deque
queue = deque(['simon', 'helen', 'dudu'])
queue.append('neinei')
queue.popleft()
queue.popleft()