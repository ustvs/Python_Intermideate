"""
Task: Create a class Address, that would have the following attributes:
postcode, city, street, building_number

Create init method that would receive all the above values and save it in
class instance attributes

Create class object attribute address_list that would collect reference of each
created Address class instance

Create class methods:
# full_address - that would return a string representing the address in format:
    "postcode, city, street building", example: "40-028, Katowice, ul. Francuska 42"

# parce_address - that woild receive one parameter address_str in the above format
and split it a tuple (postcode, city, street, building_num), i.e string

"40-028, Katowice, ul. Francuska 42"

should be converted to

("40-028", "Katowice", "ul. Francuska", "42")

# search should receive one parameter search_str and search through address_list
for the instances of Address and return a list of those instances containing the
search_str
"""

class Address(object):
    address_list=[]
    
    def __init__(self, postcode, city, street, building_number):
        self.postcode = postcode
        self.city = city
        self.street = street
        self.building_number = building_number
        Address.address_list.append(self)

    def full_address(self):
        return f"{self.postcode}, {self.city}, {self.street}, {self.building_number}"
    
    def parce_address(self, str):
        str=str.replace(' ','')
        (self.postcode, self.city, self.street, self.building_number) = str.split(',')

    def search(str):
        res=[]
        for ad in Address.address_list:
            if str in (ad.city+ad.postcode+ad.street+ad.building_number):
                res.append(ad)
        return res


Office1=Address('52-300', "Wrocław", "Grabiszyńska", "11")
#print(Office1.full_address())
Office1.parce_address("52-301, Wroclaw-Fabryczna, Strzegomska, 12")
Office2=Address('50-200', "Krakow", "Krakowska", "12")
#print(Office1.full_address())

for r in Address.search("50"):
    print (r.full_address())
