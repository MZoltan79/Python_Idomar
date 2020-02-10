#!/usr/bin/env python3


def union(stand, allproducts):
    product: str
    for product in stand:
        if product not in allproducts:
            allproducts.append(product)


stand_of_julia = ['alma', 'paradicsom', 'kelbimbó']
stand_of_kate = ['alma', 'körte', 'sóska']
stand_of_steve = ['paradicsom', 'paprika', 'hagyma', 'krumpli']

all_products = stand_of_julia[:]
union(stand_of_kate, all_products)
union(stand_of_steve, all_products)
print(all_products)

# És egy jóval egyszerűbb módszer
all_products2 = list(set(stand_of_julia) | set(stand_of_kate) | set(stand_of_steve))
print(all_products2)
