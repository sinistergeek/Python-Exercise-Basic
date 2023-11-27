import sys,csv

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} FILENAME\n".format(sys.argv[0]))
    exit()

file=sys.argv[1]
count = 0

with open(file) as fh:
    rd = csv.reader(fh,delimiter=';')
    for row in rd:
        print(row)
        count += int(row[2])
print("Total: {}".format(count))
