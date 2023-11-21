import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', help="Some description")

parser.add_argument('--max',help='max num of something', type=int)
parser.add_argument('--verbose',action='store_true')
parser.add_argument('--color','-c')

parser.add_argument('files',help='filenames(s)')
parser.add_argument('files',nargs="*")
parser.add_argument('files',nargs="+")
parser.add_argument('--files',nargs="+")

args = parser.parse_args()
print(args.name)
print(args.files)
