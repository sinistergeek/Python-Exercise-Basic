import re

filename = 'programming_quotes.txt'
word = re.compile(r'one')
with open(filename,'r') as ip_file:
    for ip_line in ip_file:
        if word.search(ip_line):
            print(ip_line,end='')
