import random
huszonegy = []
for i in range(21):
    huszonegy.append(random.randint(0,15))
print(huszonegy)

i = 0
while i < len(huszonegy) and huszonegy[i] != 0:
    i += 1
if i < len(huszonegy):
    print(f"Volt pihenőnap: {i + 1}")
else:
    print("Nem volt pihi")
