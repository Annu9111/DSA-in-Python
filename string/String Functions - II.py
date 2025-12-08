#question:https://www.geeksforgeeks.org/problems/string-functions-ii/1?page=1&category=python&sortBy=submissions
# Function to check if string
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    if b.startswith("gfg") and b.endswith("gfg"):
        print("Yes")
    else:
        print("No")