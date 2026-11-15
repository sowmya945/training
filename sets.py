pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
print(pasta_ingredients)        # garlic appears only once
print(len(pasta_ingredients))   # 5, not 6

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print(pasta_ingredients)
# {'olive oil', 'parmesan', 'tomato', 'garlic', 'pasta'}

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
print("All ingredients:", all_ingredients)
print("Common:", common)  # {'garlic', 'tomato'}


only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)
print("Only in Pasta:", only_pasta)
# {'olive oil', 'parmesan', 'pasta'}
print("Not shared:", unique_to_each)
# {'olive oil', 'spices', 'onion', 'chicken', 'pasta', 'parmesan', 'rice'}


