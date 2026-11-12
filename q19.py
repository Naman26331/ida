import random
from collections import Counter

random.seed(1)          # fixed seed so the results can be repeated

# Coin tossing
n = 1000
tosses = [random.choice(["Head", "Tail"]) for _ in range(n)]
count = Counter(tosses)
print("--- Coin tossing (", n, "tosses ) ---")
print("Heads:", count["Head"], ", Tails:", count["Tail"])
print("Experimental P(Head) =", count["Head"] / n)
print("Theoretical  P(Head) = 0.5")

# Dice rolling
m = 6000
rolls = [random.randint(1, 6) for _ in range(m)]
dice = Counter(rolls)
print("\n--- Dice rolling (", m, "rolls ) ---")
for face in range(1, 7):
    print("Face", face, ": count =", dice[face],
          ", experimental P =", round(dice[face] / m, 4),
          ", theoretical P =", round(1 / 6, 4))

# Sum of two dice
k = 6000
sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(k)]
print("\nExperimental P(sum = 7) =", round(sums.count(7) / k, 4))
print("Theoretical  P(sum = 7) =", round(6 / 36, 4))

# Law of large numbers
for trials in (10, 100, 10000):
    heads = sum(random.choice([0, 1]) for _ in range(trials))
    print("Trials =", trials, ", P(Head) =", heads / trials)
