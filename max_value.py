#sorted list
A = [1 , 2 , -3 , -4 , 5]


#use max() function
print(f"use max() func => {max(A)}")


#max_value
def max_value(A):
    my_max = A[0]

    for idx in range(1 , len(A)):
        if my_max < A[idx]:
            my_max = A[idx]

    return my_max   


print(f"use my func => {max_value(A)}")