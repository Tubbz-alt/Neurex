import random
m = []

characters = [chr(i) for i in range(32, 123)]
# characters.append(' ')
hash_map_values = []

for i in range(100):
    a = random.randint(2**18, 2**19)
    hash_map_values.append(int(bin(a)[2:]))

print(hash_map_values)

random.shuffle(characters)
random.shuffle(hash_map_values)

hash_map = dict(zip(characters,hash_map_values))

print(hash_map)

with open('encrypt_1_seed.txt','w') as f:
    f.write(str(hash_map))

characters.sort()

uniq = []
for j in hash_map.values():
    uniq.append(len(str(j)))

print(set(uniq))


    
print(len(hash_map))
l = []
for i in hash_map.keys():
    l.append(i)

print(sorted(l))
