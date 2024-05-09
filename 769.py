def brute_force(text,pattern):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            match = text[i+j] == pattern[j]
            if not match:
                break
            if  j == len(pattern) - 1:
                occurrences.append(i)
    return occurrences 
input_text = "CODEWITHCODER"
input_pattern  = "CODE"
occurrences = brute_force(input_text,input_pattern)
if occurrences:
    print(f"The pattern found at indices: {occurrences}.")
else:
    print("The pattern is not present in the text.")
