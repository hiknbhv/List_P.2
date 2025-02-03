#Assignment 1
ten_list = [20, 20, 49, 71, 97, 29, 10, 33, 33, 49]
ten_squares = [x**2 for x in range(10)]
# TODO: put in the square brackets a list comprehension.  See notes
print(ten_squares)

#Assignment 2
for x in ten_list:
    if ten_list.count(x) > 1:
        ten_list.remove(x)
print(ten_list)
#TODO:  Total RECALL from previous notes/assignments/etc.