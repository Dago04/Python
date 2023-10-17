mi_set =   set([1,2,3,4,5,])

print(type(mi_set))
print(mi_set)

print(2 in mi_set)


s1 = {1,2,3}
s1.clear()
s1.add(7)
s1.discard(6)
s2 = {3,4,5}
s2.remove(4)
s2.pop()
s3 = s1.union(s2)

print(s3)