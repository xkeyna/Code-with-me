#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:32:12 2024

@author: sakinahrosli
"""

import pandas as pd
import itertools
from itertools import product


def create_combination_table(*args):
    ''' create a table containing all possible combinations'''
    # create a list for all the variables
    n = list(args)
    # get the combinations using product
    combinations = list(itertools.product(n, repeat=len(n)))
    # convert the list into dataframe row
    df = pd.DataFrame(combinations)
    # add A at each column name
    df.columns = ['A' + str(col) for col in df.columns]
    # create column is_identical and compare across all the columns for each row
    df['is_identical'] = df.nunique(axis=1) == 1
    return df


data = create_combination_table('lion', 'dog', 'fish')
