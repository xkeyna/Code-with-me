#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:50:36 2024

@author: sakinahrosli
"""

import pandas as pd
import json
import ast

# Load file
df = pd.read_excel('OppoMalaysia_Raw_File.xlsx')


# Filter data from 2020-07-01 to 2020-09-30
start_time = '2020-07-01'
end_time = '2020-09-30 23:59:59'
# Filter data between two dates
filtered_df = df.loc[(df['created_timestamp'] >= start_time)
                     & (df['created_timestamp'] <= end_time)].copy()


# check missing values
print('Missing data:')
print(filtered_df.isnull().sum())
# shares and video_views has missing values

# replace the missing values with 0 assuming no interactions
filtered_df['shares'] = filtered_df['shares'].fillna("{'count': 0}")
filtered_df['video_views'] = filtered_df['video_views'].fillna(0)
# replace for comments column just in case for future data
filtered_df['comments'] = filtered_df['comments'].fillna(
    "{'summary': {'total_count': 0}}")

print('missing values handled')

# Convert strings to dictionaries
for column in ['shares', 'reactions', 'comments']:
    filtered_df[column] = filtered_df[column].apply(ast.literal_eval)


def create_total_interactions(df):
    '''Count total interaction'''

    # assign variable into total_interactions dictionary
    total_interactions = {
        "all": df['interactions'].sum(),
        "video_views": df['video_views'].sum(),
        "shares": df['shares'].apply(lambda x: x['count']).sum(),
        "reactions": df['reactions'].apply(lambda x: x['summary']['total_count']).sum(),
        "comments": df['comments'].apply(lambda x: x['summary']['total_count']).sum()
    }

    total_interactions["non_video_interactions"] = total_interactions["all"] - \
        total_interactions["video_views"]

    # Convert all values to int
    total_interactions = {k: int(v) for k, v in total_interactions.items()}

    return total_interactions


def create_total_post(df):
    '''Count each category total type of post'''
    total_post = df['type'].value_counts().to_dict()
    total_post['all'] = sum(total_post.values())

    # Sort the dict by values in descending order
    total_post = dict(
        sorted(total_post.items(), key=lambda item: item[1], reverse=True))

    return total_post


def create_interactions_by_type(df):
    ''' Count interaction by type photo, video, others '''
    # Group by type and calculate counts and sums
    grouped = df.groupby("type")["interactions"].agg(['count', 'sum'])

    # Initialize the list with the required variables
    interactions_by_type = [
        {"id": "photo", "name": "Photo", "count": 0, "interactions": 0},
        {"id": "video", "name": "Video", "count": 0, "interactions": 0},
        {"id": "others", "name": "Others", "count": 0, "interactions": 0}
    ]

    # Loop through grouped data to populate the values
    for type_, data in grouped.iterrows():
        count = data['count']
        interaction_sum = data['sum']

        # access the dict by list indices
        if type_ == 'photo':
            interactions_by_type[0]['count'] = int(count)
            interactions_by_type[0]['interactions'] = int(interaction_sum)
        elif type_ == 'video':
            interactions_by_type[1]['count'] = int(count)
            interactions_by_type[1]['interactions'] = int(interaction_sum)
        else:
            interactions_by_type[2]['count'] += int(count)
            interactions_by_type[2]['interactions'] += int(interaction_sum)

    return interactions_by_type


# Call the functions
total_interactions = create_total_interactions(filtered_df)
total_post = create_total_post(filtered_df)
interactions_by_type = create_interactions_by_type(filtered_df)


# Create list to store the data
data = [{
    "total_interactions": total_interactions,
    "total_post": total_post,
    "interactions_by_type": interactions_by_type
}]


# Convert to JSON string
json_data = json.dumps({'data': data}, indent=3)
# print(json_data)

# Writing to filtered_data.json
with open("summary_data_Nurul.json", "w") as outfile:
    outfile.write(json_data)

print('Done. Json file created')
