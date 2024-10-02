#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:37:43 2024

@author: sakinahrosli
"""

from itertools import chain


def calculate_balls(n, q, j=None):
    ''' q is number of buckets,
    n is number of balls,
    j is label of the balls based on the bucket they are in '''
    # imagine the bucket as individual list
    # elements in the list will represent balls
    # create a list to contain each bucket as a list
    buckets = [[] for i in range(0, q)]
    # number of balls
    label = q
    # loop each bucket to store the ball
    while n > 0:
        for bucket in buckets:
            # terminate if no more balls
            if n == 0:
                break
            bucket.append(label)
            # decrease number of balls
            n -= 1
            # decrease label according to bucket label
            label -= 1
            # when one loop completed, reset i back to initial bucket number q
            if label == 0:
                label = q

    # calculate number of balls corresponding to label j
    # create a dict from the list
    bucket_dict = {}
    for bucket in buckets:
        # get the first element as the name for key dict
        bucket_dict[bucket[0]] = bucket[0:]

    # Print total if j is specified
    if j is not None and j in bucket_dict:
        total = len(bucket_dict[j])
        print(f'Label {j}: {total} balls')

    return bucket_dict


dict1 = calculate_balls(40, 7, 5)


def output_lineballs(n, q):
    ''' outputs a list of integers representing the line of balls '''
    # retrieve the dict
    bucket_dict = calculate_balls(n, q)

    # unpack dict values into a single list
    single_list = list(chain(*bucket_dict.values()))

    return single_list


print(output_lineballs(20, 6))
