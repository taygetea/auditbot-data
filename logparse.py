import json
from collections import Counter

wordlist = open("minidic-WORDLIST.txt")
wordlist = [x[:-2] for x in wordlist]  # first thousand
print wordlist
rawlog = open("lesswrong_logs.json")
print "Loading JSON..."
logdict = json.load(rawlog)
logs = []
users = set()
for day in logdict.keys():
    for line in logdict[day]:
        if line[3] == u'olivia':
            logs.append(line)
            users.add(line[3])
print "Removing common words..."
uncommons = []
for line in logs:
    clean = line[4].split()  # Naive, will miss stuff
    for elem in clean:
        if elem not in wordlist:
            uncommons.append(elem)
print Counter(uncommons).most_common(1000)
