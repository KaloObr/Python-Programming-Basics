dogs_count = int(input())
other_animals_count = int(input())

price_for_dog_food = 2.50
price_for_other_animals_food = 4

result = dogs_count * price_for_dog_food + other_animals_count * price_for_other_animals_food
print(f"{result:.2f} lv.")