import re

sentence = "The ghost that says boo haunts the loo"


found = re.findall(".oo",sentence)
for match in found:
    print(match)

"""
boo
loo
"""