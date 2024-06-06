from fractions import Fraction 
P_shift = {
        shift: Fraction(shift_totals[shift],total)
        for shift in sorted(shift_totals)
        }
P_type = {
        type: Fraction(type_totals[types],total)
        for type in sorted(type_totals)
        }
