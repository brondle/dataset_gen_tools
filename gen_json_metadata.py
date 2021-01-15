import csv
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-sf', '--suggested_features', nargs='+')
parser.add_argument('-o', '--outfile')
parser.add_argument('-i', '--infile')

data = {'fields': []}

def pair(arg):
    print('arg: ', arg)
    pairs = [[int(x) for x in arg.split(',')]]
    print ('pairs: ', pairs)
    return [range(x[0], x[1]) for x in pairs]
parser.add_argument('-ca', '--categorical', type=pair, nargs='+')
parser.add_argument('-co', '--continuous', type=pair, nargs='+')

args = parser.parse_args()
with open(args.infile, 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    csv_list = list(map(tuple, reader))
    for idx, cell in enumerate(csv_list[0]):
        for i in args.categorical:
            if idx in i[0]:
                data['fields'].append({
                    'type': 'categorical',
                    'id': cell
                })
                break

        for i in args.continuous:
            if idx in i[0]:
                data['fields'].append({
                    'type': 'continuous',
                    'id': cell
                })
                break
with open(args.outfile, 'w') as outfile:
    json.dump(data, outfile)



