def scalar_vector_product(alpha,*args):
    return [alpha*sum(t)for t in zip(*args)]

scalar_v=5
vector_list = [1,3,5,7,11,13]
print(scalar_vector_product(scalar_v,vector_list))
