# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:52:46 2023

@author: Hannah
"""

from merge import mergeSort


def bucketSort(array):
    if len(array) <= 1:
        return array

    # Create empty buckets

    num_buckets = len(array)
    buckets = [[] for _ in range(num_buckets)]

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(0.1 * j)
        buckets[index_b].append(j)

    # Sort the elements of each bucket using merge sort
    for i in range(num_buckets):
        if len(buckets[i]) > 1:
            buckets[i] = mergeSort(buckets[i])

    # Concatenate the sorted buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    # Applying the merge sort algorithm for a stable sort

    return sorted_array


           