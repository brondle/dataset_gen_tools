import csv
import argparse
import re
import random
from dateutil import parser as dateparser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-o', '--outfile')
arg_parser.add_argument('-i', '--infile')

args = arg_parser.parse_args()

START_DATE = dateparser.parse("1/1/1995")
END_DATE = dateparser.parse("1/1/2016")

def clean_and_sub(outfile, infile):
    writer = csv.writer(outfile, delimiter=',')
    reader = csv.reader(infile, delimiter=",")
    #skip headers
    for (idx, row) in list(enumerate(reader))[1:]:
        date = dateparser.parse(row[0])
        if date >= START_DATE and date <= END_DATE and row[2] not in (None, "") and row[3] not in (None, ""):
#            print(date.strftime("%Y-%m-%d"))
            out_data = [date.strftime("%Y"),date.strftime("%m")] + row[1:]
            writer.writerow(out_data)






print(__name__)
if __name__ == "__main__":
  with open(args.outfile, 'w') as outfile:
    with open(args.infile, 'r') as infile:
        clean_and_sub(outfile, infile)
