import csv
import argparse
import re
import random
parser = argparse.ArgumentParser()

def gen_data(outfile):
    writer = csv.writer(outfile, delimiter=',')
    indices = [[5, 1], [1, 7], [3, 10], [5, 7], [7, 10], [10, 5], [5, 1]]
    writer.writerow(['Daily Minutes of Exercise', 'Heart Health Rating'])
    for (idx, item) in enumerate(indices):
        if idx == len(indices)-1:
            return
        to_write = item
        writer.writerow(to_write)
        next_item = indices[idx+1:][0]
        while (to_write != next_item and idx < len(indices)):
            print('writing: ', to_write)
            for (idx, num) in enumerate(to_write):
                if to_write[idx] > next_item[idx]:
                    to_write[idx] -= 1
                elif to_write[idx] < next_item[idx]:
                    to_write[idx] += 1
                else:
                    pass
            writer.writerow(to_write)



with open('test_scatterplot.csv', 'w') as outfile:
    gen_data(outfile)
        # questions can be in any order
        # need to order the questions
        # then make sure row data is all same


