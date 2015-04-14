import json

wordlist = open("minidic-WORDLIST.txt")
rawlog = open("lesswrong_logs.json")
logdict = json.load(rawlog)
words = []
users = set()
for day in logdict.keys():
    for line in logdict[day]:
        if line[1] == u'PRIVMSG':
            words.append(line)
            users.add(line[3])
print words[:10]
