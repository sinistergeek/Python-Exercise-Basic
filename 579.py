import re

values = ["Learn","Live","Python"]
for value in values:
    result = re.match("\AL.+",value)
    if result:
        print("START MATCH [L]:",value)
    result2 = re.match(".+n\Z",value)
    if result2:
        print("END MATCH [n]:",value)
