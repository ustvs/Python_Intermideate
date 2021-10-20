"""
This is homework from basics Python course to refresh comprehensions

Lets we have 
1. variable amounts of type list storing float values representing cash in different currencies
2. variable rates of type dictionary storing currency rates to local curency where keys and carency names like "EUR", "USD", ... and values are rates
3. variable curency of type list storing curency name for each value in amounts list

for example
amounts = [20, 100, 45, 50]
curency = ["EUR", "USD", "PLN"]
rates = {
    "EUR": 4.2,
    "USD": 3.7, 
    "PLN": 1.0
}


create a dictionary comprehension that will generate a dictionary with values from amounts as keys and values should be same values converted to local currency
based on curency and rates variables. Also it should not contain items which converted amount greater 200PLN 

so for above variables result should be:
{
    20: 84.0, 
    45: 45.0, 
    50: 185.0
}

"""
amounts = [20, 100, 45, 50]
currency = ["EUR", "USD", "PLN", "GBP"]
rates = {
    "EUR": 4.2,
    "USD": 3.7, 
    "PLN": 1.0,
    "GBP": 4.83
}
frame={amounts[i]:amounts[i]*rates[currency[i]] for i in range(len(amounts)-1) if amounts[i]*rates[currency[i]] < 200 }
print(frame)