# Queues follow the First-In-First-Out(FIFO) principle, meaning that the item that goes in first is the one that comes out first.

from queue import Queue

waitingList = Queue()

waitingList.put('xaomi')
waitingList.put('nokia')
waitingList.put('samsung')
waitingList.put('oneplush')

for x in list(waitingList.queue):
    print(x)

print(waitingList.get())

print(waitingList.empty())