from collections import defaultdict
nums = [1,1,1,2,2,3]
freq = defaultdict(int)
for e in nums:
    freq[e] += 1
for e in freq.items():
    print(e)
