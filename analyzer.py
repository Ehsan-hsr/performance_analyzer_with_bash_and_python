import csv
import datetime


def mean_calc(data_list):
    return sum(data_list)/len(data_list)

data_dict ={}
data = None
with open("cpu_usage_log", "r") as f:
    data = csv.reader(f)
    for i in data:
        if i[0] in data_dict:
            data_dict[i[0]].append(float(i[4]))
        else:
            data_dict[i[0]] = []
            data_dict[i[0]].append(float(i[4]))


n_index = list(data_dict)[-1]
n_1_index = list(data_dict)[-2]

progress_percent = mean_calc(data_dict[n_index]) - mean_calc(data_dict[n_1_index])
if progress_percent < 0:
    print(f"[+]Your program performance has been imporved by {abs(progress_percent)} %.")
else:
    print(f"[+]Your program performance has been reduced by {abs(progress_percent)} %!!!!!")
                           

with open("tmp", "w") as f:
    for i in data_dict:
        f.write(f"{i}  {mean_calc(data_dict[i])}\n")
