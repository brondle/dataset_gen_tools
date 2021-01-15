import csv
import argparse
import re
import random
parser = argparse.ArgumentParser()

def clean_and_sub(outfile, infile):
    writer = csv.writer(outfile, delimiter=',')
    reader = csv.reader(infile, delimiter=",")
    percentage_indices = []
    total = 0
    #     map = {0 : ['Dusk', 'Dawn', 'Stars', 'Moon', 'River', 'Forest'], 1: ['tortoiseshell box', 'jet black box', 'golden casket', 'pewter box'], 2: ['troll', 'drawing lots', 'Volunteer'], 3: ['Black', 'White', 'Head', 'Tails', 'Left', 'Right']}

    map = {0 : ['Dusk', 'Dawn'], 1: ['Tails', 'Heads'], 2: ['Left', 'Right'], 3: ['Snake', 'Rat', 'Cat', 'Owl']}
    writer.writerow(['Dusk or Dawn', 'Heads or Tails', 'Left or Right', 'Pet', 'House'])
    for (idx, row) in enumerate(reader):
        new_row = [0] * (len(map) + 1)
        flag = False
#        for i, x in enumerate(row):
#            if i == 8:
#                print('x: ', x)
#                new_row[len(map)] = x
        print('new row: ')
        for i, v in map.items():
            val = random.randrange(0, len(v))
            print('val: ', val)
            new_row[i] = val
            print('sum: ', sum(new_row))
            sum_v = sum(new_row)
        if sum_v == 6 or sum_v == 5:
            new_row[len(map)] = "Gryffindor"
        elif sum_v == 4 or sum_v == 3:
            new_row[len(map)] = "Hufflepuff"
        elif sum_v == 2 or sum_v == 1:
            new_row[len(map)] = "Ravenclaw"
        else:
            new_row[len(map)] = "Slytherin"


#                for z in v:
#                    if z in x:
#                        flag = True
#                        print('x: ', x)
#                        print('i: ', i)
#                        new_row[i] = x
        #if 0 not in new_row:
        writer.writerow(new_row)

with open('out_test.csv', 'w') as outfile:
    with open('sorting_hat.csv', 'r') as infile:
        clean_and_sub(outfile, infile)
        # questions can be in any order
        # need to order the questions
        # then make sure row data is all same


