    t = int(input())
    queue = list(input().split())
    q = int(input())
    new = []
    for _ in range(q):
        new.append(input())
     
    queue.extend(new)
    queue.sort()
    for i,val in enumerate(new):
        print(queue.index(val)-i)
     
     
