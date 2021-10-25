from src import helpu

import time

######### FUNCTIONS ###########

def chunk1(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def chunk2(lst, n):
    tp_lst = []
    for i in range(0, len(lst), n):
        tp_lst.append(lst[i:i + n])
    return tp_lst

def chunky(lst, n):
    def chunkdat(lst,n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    return list(chunkdat(lst, n))

####### General config ###########

ATTEMPS = 20000


####### Test config ###########
chunk_size = 2000

tst = ["a" for i in range(500000)]

### METHOD 1
a = time.time()

for i in range(ATTEMPS):
    u = chunky(tst, chunk_size)

b = round(time.time()-a, 5)
print(b)

### METHOD 2
a = time.time()
for i in range(ATTEMPS):
    u = chunk2(tst, chunk_size)

b = round(time.time()-a, 5)
print(b)




