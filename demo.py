import pandas as pd
import xlrd
import matplotlib.pyplot as plt
from tabulate import tabulate

df = pd.read_excel('New Substances Risk Assessment Summaries.xlsx')

df = df['Additional information']
df = df.apply(lambda x: x.split())

dict = {str(i)+'.':0 for i in range(1997,2021)}

for item in df:
    for word in item:
        if word in dict:
            dict[word] += 1
            break


# sum = 0
# for item in dict:
#     sum += dict[item]
#
#
# xs = [item for item in dict]
# ys = [dict[item] for item in dict]
#
# plt.bar(xs,ys)
# plt.xticks(xs, fontsize=5)
# plt.show()

results = [(item, dict[item]) for item in dict]
print(tabulate(results, headers=('year','occurences')))





