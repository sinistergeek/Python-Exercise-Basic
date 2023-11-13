import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.search(r"(\d{4})\s",s)
print(result.group(1))
