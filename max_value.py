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

#use for loops to find max value in list
def alternate(A):
    for v in A:
        for x in A:
            if v < x:
                break
            else:
                return v
    return None



#print results
print(f"use my func => {max_value(A)}")
print(f"for loops result => {alternate(A)}")