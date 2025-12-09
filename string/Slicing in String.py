#question:https://www.geeksforgeeks.org/problems/slicing-in-string-python/1?page=1&category=python&sortBy=submissions
# Function to join given bound_by and tag
def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
  mid=len(bound_by)//2
  return bound_by[0 : mid   ] + tag_name + bound_by[mid:  ]