def is_orthogonal(u, v):
    if len(u) != len(v):
        raise ValueError("inte lika långa")

    prod = 0
    for i, ui in enumerate(u):
        prod += ui * v[i]
    return prod == 0

def is_orthogonal2(u, v):
    if len(u) != len(v):
        raise ValueError("inte lika långa")
   
    return sum([ ui * v[i] for i, ui in enumerate(u) ]) == 0

print("True", is_orthogonal2([0, 1], [1, 0]))
print("False", is_orthogonal2([0, 1], [1, 1]))
#print("False", is_orthogonal2([0, 1], [1, 0, 2]))