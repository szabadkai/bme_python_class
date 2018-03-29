>>> fh=open("war_and_peace.txt")
>>> counter=0
>>>
for line in fh:
    if "dog" in line:
        count = count+1
>>> count=0
>>>
for line in fh:
    if "dog" in line:
        count = count+1
>>> count
>>> fh=open("war_and_peace.txt")
>>>
for line in fh:
    if "dog" in line:
        for word in line.split():
            if word.lower()== "dog":
                count=count +1
>>> count
>>> from collections import Counter
>>> fh=open("war_and_peace.txt")
>>> war_and_peace=Counter
>>> war_and_peace=Counter()
>>>
for line in fh:
    war_and_peace.update(line.lower().split())
>>> war_and_peace['dog']
>>> war_and_peace.most_common(5)
