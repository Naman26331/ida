from itertools import groupby
from operator import itemgetter

def mapper(line):
    """Map phase: emit (word, 1) for every word in the line."""
    for word in line.lower().split():
        word = word.strip(".,!?;:\"'()")
        if word:
            yield (word, 1)

def reducer(word, counts):
    """Reduce phase: add all the counts of a word."""
    return (word, sum(counts))

documents = [
    "Big data needs big storage",
    "Hadoop stores big data",
    "MapReduce processes data in parallel",
    "Data is processed by Hadoop MapReduce",
]

# 1. Map
mapped = []
for line in documents:
    mapped.extend(mapper(line))
print("Mapper output (first 8 pairs):")
print(mapped[:8])

# 2. Shuffle and sort (group the pairs with the same key)
shuffled = sorted(mapped, key=itemgetter(0))
print("\nAfter shuffle and sort (first 8 pairs):")
print(shuffled[:8])

# 3. Reduce
result = []
for word, group in groupby(shuffled, key=itemgetter(0)):
    counts = [count for _, count in group]
    result.append(reducer(word, counts))

print("\nReducer output (word count):")
for word, total in result:
    print(word, "\t", total)
