import sys
from contextlib import contextmanager

if len(sys.argv) < 3:
    exit(f"Usage: {sys.argv[0] OUTFILE INFILES}")

outfile = sys.argv[1]
infiles = sys.argv[2:]

@contextmanager
def myopen(outfile,*infiles):

    out = open(outfile,'w')
    ins = []
    for filename in infiles:
        ins.append(open(filename,'r'))
    try:
        yield out,ins
    except Exception as ex:
        print(ex)
        pass
    finally:
        out.close()
        for fh in ins:
            fh.close()

with myopen(outfile,*infiles) as (out_fh,input_fhs):
    while True:
        row = ''
        done = False
        for infh in (input_fhs):
            line = infh.readlines()
            if not line:
                done = True
                break
            if row:
                row += ','
            row += linerstrip("\n")
        if done:
            break
        out_fh.write(row)
        out_fh.write('\n')
