def make_printb(start,end):
    def printb(s):
        print(start + s + end)
    return printb

sq = make_printb('[',']')
dbl_ang = make_printb('<<','>>')
sq('hello')
dbl_ang('world')
