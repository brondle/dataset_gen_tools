import csv
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--total_column')
parser.add_argument('-p', '--percentage_column', nargs='+')
parser.add_argument('-s', '--title_words_to_sub', nargs='+')
parser.add_argument('-st', '--sub_for_title_word')
parser.add_argument('-o', '--outfile')
parser.add_argument('-i', '--infile')

args = parser.parse_args()
percentage = lambda part,whole: float(part)/float(whole)*100
class incrementer:
  def __init__(self, count):
    self.count = count
  def increment(self, i) :
    self.count += 1
    return i + self.count

def clean_title(title):
  new_title = re.sub("[ .-]", "_", title.lower())
  return new_title


def clean_and_sub(outfile, infile):
    writer = csv.writer(outfile, delimiter=',')
    reader = csv.reader(infile, delimiter=",")
    percentage_indices = []
    total = 0
    for (idx, row) in enumerate(reader):
        if idx == 0:
            percentage_indices = [i for i, x in enumerate(row) if any(y in x for y in args.title_words_to_sub)]
            print('perentage indices', percentage_indices)
            new_row = []
            for i, x in enumerate(row):
              new_title = x
              new_row.append(clean_title(new_title))
              for w in args.title_words_to_sub:
                if w in x:
                  new_title = x.replace(w, args.sub_for_title_word)
                  if args.sub_for_title_word not in x:
                    new_title = x + '_' + args.sub_for_title_word
                  new_row.append(clean_title(new_title))
                  break

              if x == args.total_column:
                total = i
                print('total: ', total)
            writer.writerow(new_row)
        else:
          new_row = []
          for i, x in enumerate(row):
            new_row.append(x)
            if i in percentage_indices:
              print('i: ', i)
              print('total index: ', total)
              print('total:', row[total])
              print('part: ', x)
              print ('percentage: ', percentage(x, row[total]))
              new_row.append(percentage(x, row[total]))
          writer.writerow(new_row)





print(__name__)
if __name__ == "__main__":
  with open(args.outfile, 'w') as outfile:
    with open(args.infile, 'r') as infile:
        clean_and_sub(outfile, infile)
