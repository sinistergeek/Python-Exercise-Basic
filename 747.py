from itertools import *
from Chapter_4.ch04_ex4 import corr
for p, q in combinations(range(9),2):
    header_p, *data_p = list(column(source,p))
    header_q, *data_q = list(column(source,q))
    if header_p == header_q:
        continue
    r_pq = corr(data_p,data_q)
    print("{2:4.2f}:{0} vs {1}".format(header_p,headerq,r_pq))
