# PUA, Charles Michael G.
# TW23

A = {"a", "b", "c", "d", "f", "g"}
B = {"b", "c", "l", "m", "o", "h"}
C = {"c", "d","f", "h", "i", "j", "k"}

# a. How many elements are there in set A and B
totalAB = A.union(B)
print(len(totalAB))

# b. How many elements are there in B that is not part of A and C
diffB = B.difference(A, C)
print(len(diffB))

#c. Show the following using set operations

# i. [h, i, j, k]
setI = C.intersection({"h", "i", "j", "k"})
print(f"[{', '.join(setI)}]")

# ii. [c, d, f]
setII1 = A.intersection(B, C)
setII2 = A.intersection(C)
setII3 = setII1.union(setII2)
print(f"[{', '.join(setII3)}]")

# iii. [b, c, h]
setIII = A.intersection(B).union(B.intersection(C))
print(f"[{', '.join(setIII)}]")


