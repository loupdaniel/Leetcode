import pandas as pd


student_data = {
    "student_id": [1,2,3,4],
    "age": [15,11,11,20],
    "ages": [16,17,18,19]
}

df = pd.DataFrame(student_data, columns = ["student_id", "age", "ages"])

def getDataframeSize(df):
    x = len(df.columns)
    y = round(df.size/x)
    return print(f'[{x}, {y}]')

getDataframeSize(df)