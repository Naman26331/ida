from itertools import combinations

transactions = [
    {"bread", "milk"},
    {"bread", "diaper", "beer", "eggs"},
    {"milk", "diaper", "beer", "cola"},
    {"bread", "milk", "diaper", "beer"},
    {"bread", "milk", "diaper", "cola"},
]
min_support = 0.4
min_confidence = 0.7
N = len(transactions)

def support(itemset):
    count = sum(1 for t in transactions if itemset.issubset(t))
    return count / N

# Step 1: frequent 1-itemsets
items = sorted({item for t in transactions for item in t})
current = [frozenset([i]) for i in items if support(frozenset([i])) >= min_support]

frequent = {}
k = 1
while current:
    for s in current:
        frequent[s] = support(s)
    k += 1
    # Join step: build candidate k-itemsets
    candidates = {a | b for a in current for b in current if len(a | b) == k}
    # Prune step (Apriori principle): every (k-1)-subset must be frequent
    previous = set(current)
    candidates = [c for c in candidates
                  if all(frozenset(sub) in previous for sub in combinations(c, k - 1))]
    current = [c for c in candidates if support(c) >= min_support]

print("Minimum support =", min_support, ", Minimum confidence =", min_confidence)
print("\nFrequent itemsets:")
for itemset, sup in sorted(frequent.items(), key=lambda x: (len(x[0]), sorted(x[0]))):
    print(" ", sorted(itemset), "support =", round(sup, 2))

# Generating association rules
print("\nAssociation rules:")
for itemset in frequent:
    if len(itemset) < 2:
        continue
    for r in range(1, len(itemset)):
        for antecedent in combinations(itemset, r):
            antecedent = frozenset(antecedent)
            consequent = itemset - antecedent
            confidence = frequent[itemset] / frequent[antecedent]
            lift = confidence / frequent[consequent]
            if confidence >= min_confidence:
                print(" ", sorted(antecedent), "->", sorted(consequent),
                      "| support =", round(frequent[itemset], 2),
                      "| confidence =", round(confidence, 2),
                      "| lift =", round(lift, 2))
