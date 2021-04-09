import pandas as pd
import sys

filename = sys.argv[1]
outfile = sys.argv[2]

df = pd.read_excel(filename)
print("file read")
df = df.pivot(index="Temperature", columns="Well Position", values="Fluorescence")


alpha = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
num = df.columns.size
num = num/16
num = int(num)
labels = []
for i in range(num):
    for letter in alpha:
        string = letter + str(i+1)
        labels.append(string)

df = df.reindex(labels, axis="columns")

df.to_excel(outfile)
print("file written")
