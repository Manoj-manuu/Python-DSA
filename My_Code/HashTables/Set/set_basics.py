my_set = {1,2,3,4}
#my_set = set([1,2,3,4,5,6,7])
my_set.add(5)
my_set.update([6,7,8])
my_set.remove(8)
print(my_set)

other_set = {8,9,10}
union_set = my_set.union(other_set)
print(union_set)

intersection_set = my_set.intersection(other_set)
print(intersection_set)

difference_set = my_set.difference(other_set)
print(difference_set)

if 1 in my_set:
    print("hii")