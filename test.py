A0 = (dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5))))
A3 = (sorted(A0[s] for s in A0))
A4 = [i for i in range(10) if i in A3]
