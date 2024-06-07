print("obs exp"*len(type_totals))
for s in sorted(shift_totals):
    pairs = [
            f"{defects[s,t]:3d} {float(except[s,t]):5.2f}"
            for t in sorted(type_totals)
            ]
    print(f"{' '.join(pairs)} {shift_totals[s]:3d}")
    footers = [f"{type_totals[t]:3d}"
    for t in sorted(type_totals)]
print(f"{' '.join(footers)} {total:3d}")

