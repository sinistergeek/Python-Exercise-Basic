def PatternCount(Text,Pattern):
    count = 0
    for i in range(len(Text)):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count
