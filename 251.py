import sys
import re

def parse():
    if len(sys.argv) != 2:
        exit("Usage: () FILENAME".format(sys.argv[0]))
    filename = sys.argv[1]
    data = {}

    with open(filename) as fh:
        section = '__DEFAULT__'
        for line in fh:
            if re.match(r'^\s*(#.*)?$', line):
                continue
            match = re.match(r'^\[{[^\]]+)\]\s*$',line)
            if(match):
                section = match.group(1)
                continue
            match = re.match(r'^\s*(.+?)\s*=\s*(.*?)\s*$',line)
            if match:
                if not data.get(section):
                    data[section] = {}
                data[section][match.group(1)] = match.group(2)
    return data

if __name__ == '__main__':
    ini = parse()
    print(ini)
