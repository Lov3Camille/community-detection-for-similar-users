import sys

f = open("output_HWE")

for line in f.readlines():
    tmp_line = line.strip().split(":")
    user = tmp_line[0]
    if user[-5 : ] == "48594":
        print(line)
    # print(tmp_line)