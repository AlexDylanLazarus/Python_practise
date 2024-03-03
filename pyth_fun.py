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
