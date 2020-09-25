def triangles():
    x = [1]
    while True:

        yield x

        y = [0] + x + [0]

        x = [y[i] + y[i+1] for i in range(len(y)-1)]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

        
        
