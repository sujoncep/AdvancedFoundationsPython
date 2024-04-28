# A deque(double-ended queue) is a data structure that allows insertion and deletion of elements from both ends. Python provides a built-in implementation of deque through the collections module.

from collections import deque
waitingList = deque()

waitingList.append('xaomi')
waitingList.append('nokia')
waitingList.append('samsung')
waitingList.append('oneplush')

print(waitingList)

waitingList.appendleft('iphone')
# get item from left
waitingList.popleft()
print(waitingList)

# get item from right
waitingList.pop()
print(waitingList)
