# Q1 Setup Code
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]


sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)

for i, student in enumerate(sorted_students, start=1):
    student["rank"] = i

for student in sorted_students:
    print(
        f"Name: {student['name']}, Grade: {student['grade']}, Rank: {student['rank']}"
    )

# Q2
# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.

merged_list = []
for employee in employees:
    for salary in salaries:
        if employee["id"] == salary["id"]:
            merged_dict = {**employee, **salary}
            merged_list.append(merged_dict)

print(merged_list)

# Q3
# Setup Code
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.


for product in products:
    if product["category"] == "Electronics" and product["price"] < 500:
        filtered_prods = []
        filtered_prods.append(product)
        print(filtered_prods)

# Q4
# Setup Code
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.

product_quantities = {}

for order in orders:
    for item in order["items"]:
        product = item["product"]
        quantity = item["quantity"]
        if product in product_quantities:
            product_quantities[product] += quantity
        else:
            product_quantities[product] = quantity

print(product_quantities)

# Q5
# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.
category_totals = {}

for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print(category_totals)


# Q6
# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.
total_sales = {}

for sale in sales:
    salesperson = sale["salesperson"]
    amount = sale["amount"]
    if salesperson in total_sales:
        total_sales[salesperson] += amount
    else:
        total_sales[salesperson] = amount
print(total_sales)

# Q7
# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.
sorted_spells = sorted(spells, key=lambda x: x[1], reverse=True)
print(sorted_spells)

# Q8
# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.

transformed_ingredients = map(lambda x: x + ": 3 grams", ingredients)
print(list(transformed_ingredients))

# Q9
# Setup Code
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.

filtered_books = filter(lambda book: book["pages"] > 120, books)
print(list(map(lambda x: x["title"], filtered_books)))


# Q10
class WizardDuel:
    def __init__(self, wizard1, wizard2):
        self.wizard1 = wizard1
        self.wizard2 = wizard2

    def cast_spell(self, wizard, spell_power):
        wizard.health -= spell_power

    def determine_winner(self):
        if self.wizard1.health > self.wizard2.health:
            return self.wizard1
        elif self.wizard2.health > self.wizard1.health:
            return self.wizard2
        else:
            return None


class Wizard:
    def __init__(self, name, health):
        self.name = name
        self.health = health


harry = Wizard("Harry", 15)
draco = Wizard("Draco", 15)

duel = WizardDuel(harry, draco)
duel.cast_spell(harry, 5)
duel.cast_spell(draco, 8)

winner = duel.determine_winner()

if winner:
    print(
        f"After a duel between {winner.name} and {draco.name}, {winner.name} wins with {winner.health} health points left."
    )
else:
    print("It's a tie!")


# Q11
class PotionError(Exception):
    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.message = "is not a valid ingredient for the Love Potion."
        super().__init__(self.message)

    def __str__(self):
        return f"'{self.ingredient}' {self.message}"


def potion_making():
    try:
        love_potion = ["Wolfsbane", "Dragon Scale"]
        enter_ingredient = input("enter ingredient")
        for item in love_potion:
            if enter_ingredient != item:
                raise PotionError(enter_ingredient)
            else:
                print("created love potion")
    except PotionError as e:
        print(e)


potion_making()
