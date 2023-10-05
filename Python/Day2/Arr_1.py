# Day - 2 : Introduction to Arrays.

# Code of questions discussed in the class.

#-----------------------------------------------------------------------------------------------------------.

# Q1 - Find out the sum of alll the elements of array, after taking size and elements as input from the user.

n_ele = int(input("Enter the number of elements in the array: "))

arr1 = []   # initializing an empty array.
sum = 0
for ele in range(n_ele):
    print("Enter the", ele+1, "element: ", end="")
    val = int(input())   # taking input elements from user.
    arr1.append(val)     # adding input values into the array.
    sum += val           # updating sum of elements of arr1.

print("successfully array created: ", arr1)   # printing array.
print("The sum of all the elements of the arr1 is: ", sum)  # printing sum.

#-----------------------------------------------------------------------------------------------------------.

