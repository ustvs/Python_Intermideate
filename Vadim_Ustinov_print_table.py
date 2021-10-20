"""
1. Please apply propper formatting to the below code to prettify printed table the following way:

|  N  |     Product Name     | Amount |   Price   |
| 001 | Laptop               |     20 |   2500.47 |
| 002 | Mouse                |     50 |     50.35 |
| 003 | Keyboard             |     10 |    100.00 |
| 004 | Monitor              |     15 |    500.99 |
| 005 | Headphones           |    200 |    300.00 |
| 006 | Coffee Machine       |      4 |    499.97 |
| 007 | Ext. Speakers        |     90 |    700.00 |

2. convert printed data to a list of dictionaries with keys "Product Name", "Amount", "Price"
Print this data but this time using loop
"""

#1. 
format="| {:>03d} | {:<20} | {:>6d} | {:>9.2f} |"
format_top="| {:^3} | {:^20} | {:^6} | {:^9} |"
print(format_top.format("N","Product Name", "Amount", "Price"))
print(format.format(1, "Laptop", 20, 2500.47))
print(format.format(2, "Mouse", 50, 50.35))
print(format.format(3, "Keyboard", 10, 100))
print(format.format(4, "Monitor", 15, 500.99))
print(format.format(5, "Headphones", 200, 300))
print(format.format(6, "Coffee Machine", 4, 499.97))
print(format.format(7, "Ext. Speakers", 90, 700))

# 2. convert printed data to a list of dictionaries with keys "Product Name", "Amount", "Price"
# Print this data but this time using loop

frame=[
    dict([
        ('Number',1),
        ('Product Name', 'Laptop'),
        ('Amount', 20),
        ('Price',2500.47)
    ]),
    dict([
        ('Number',2),
        ('Product Name', 'Mouse'),
        ('Amount', 50),
        ('Price',50.35)
    ]),
    dict([
        ('Number',3),
        ('Product Name', 'Keyboard'),
        ('Amount', 10),
        ('Price',100)
    ]),
    dict([
        ('Number',4),
        ('Product Name', 'Monitor'),
        ('Amount', 15),
        ('Price',500.99)
    ]),
    dict([
        ('Number',5),
        ('Product Name', 'Headphones'),
        ('Amount', 200),
        ('Price',300)
    ]),
    dict([
        ('Number',6),
        ('Product Name', 'Coffee Machine'),
        ('Amount', 4),
        ('Price',499.97)
    ]),
    dict([
        ('Number',7),
        ('Product Name', 'Ext. Speakers'),
        ('Amount', 90),
        ('Price',700)
    ])
]
print("\n")
print(format_top.format("N","Product Name", "Amount", "Price"))
for item in frame:
        print(format.format(item['Number'], item['Product Name'], item['Amount'], item['Price']))