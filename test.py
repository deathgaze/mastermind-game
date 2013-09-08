guess =  '1234'
secret = '4214'

hits = []
for i in range(0, len(secret) - 1):
    if guess[i] == secret[i]:
        hits.append(i)
        print(guess[i].__index__)
        
print(hits)       
# hits is now an array of indicies to d
# Now we have a list of hits -- these cannot be matched by misses
#for char in guess:
#   if char in secret and char not in hits: