import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number',help='the number to take to the square',type=int)
args = parser.parse_args()
print(args.number * args.number)
