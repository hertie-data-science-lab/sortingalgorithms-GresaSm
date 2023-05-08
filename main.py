from bucket import bucketSort

# testing the bucket sort algorithm

# defining a list to be sorted
my_list = [12, 23, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3]

print("Original list: ", my_list)

# sorting the list using bucket sort

sorted_list = bucketSort(my_list)

print("Sorted list: ", sorted_list)