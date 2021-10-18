word = input()
vowels_current_value = 0

for char in word:
    if char == "a":
        vowels_current_value += 1
    elif char == 'e':
        vowels_current_value += 2
    elif char == 'i':
        vowels_current_value += 3
    elif char == 'o':
        vowels_current_value += 4
    elif char == 'u':
        vowels_current_value += 5

print(vowels_current_value)
