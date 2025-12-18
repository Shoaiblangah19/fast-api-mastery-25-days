# # Hour 2 Exercise 1

# # Your Product class should:
# # 1. Have a CLASS variable 'total_products' starting at 0
# # 2. Have a CLASS variable 'store_name' set to "My Store"
# # 3. Accept 'name' and 'price' in __init__
# # 4. Increment total_products each time a product is created
# class Product:
#     total_products=0
#     store_name="My Store"
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Product.total_products+=1
#     pass
# # Expected usage:
# print(Product.total_products)  # 0
# print(Product.store_name)      # My Store

# p1 = Product("Laptop", 999.99)
# print(Product.total_products)  # 1

# p2 = Product("Mouse", 29.99)
# p3 = Product("Keyboard", 79.99)
# print(Product.total_products)  # 3

# # Each product has its own name and price
# print(p1.name)   # Laptop
# print(p2.name)   # Mouse
# print(p3.price)  # 79.99

# # All products share store_name
# print(p1.store_name)  # My Store
# print(p2.store_name)  # My Store



# # Hour 2 Exercise 2

# # Your APIClient class should:
# # 1. CLASS variables: base_url = "https://api.example.com", timeout = 30, max_retries = 3
# # 2. CLASS variable: active_clients = 0 (tracks how many clients exist)
# # 3. Accept 'api_key' in __init__ (instance variable)
# # 4. Increment active_clients when created

# class APIClient:
#     base_url = "https://api.example.com"
#     timeout=30
#     max_retries=3
#     active_clients = 0
#     def __init__(self,api_key):
#         self.api_key=api_key

#         # Tracking active clients
#         APIClient.active_clients+=1
#     pass

# # Expected usage:
# print(APIClient.base_url)       # https://api.example.com
# print(APIClient.timeout)        # 30
# print(APIClient.active_clients) # 0

# client1 = APIClient("key-123-abc")
# client2 = APIClient("key-456-def")

# print(APIClient.active_clients)  # 2
# print(client1.api_key)           # key-123-abc
# print(client2.api_key)           # key-456-def

# # Both share the same base_url
# print(client1.base_url)  # https://api.example.com
# print(client2.base_url)  # https://api.example.com


# Hour 2 Exercise 3

# Your Validators class should have these STATIC methods:
# 1. is_valid_email(email) - returns True if email contains "@" and "."
# 2. is_valid_password(password) - returns True if:
#    - At least 8 characters
#    - Contains at least one digit
# 3. is_valid_username(username) - returns True if:
#    - Between 3 and 20 characters
#    - Only contains letters, numbers, and underscores
#    - Hint: use str.isalnum() or check each character
# 4. is_valid_age(age) - returns True if age is an integer between 0 and 150

# import re
# class Validators:
#     @staticmethod
#     def is_valid_email(email):
#         return "@" in email and "." in email
#     @staticmethod
#     def is_valid_password(password):
#         if len(password)<8:
#             return False
#         for c in password:
#             if c.isdigit():
#                 return True
            
#         return False
#     @staticmethod
#     def is_valid_username(username):
#         if len(username)<3 or len(username)>20:
#             return False
#         if  re.search(r"\W",username) is None:
#             return True
#         return False
#     @staticmethod
#     def is_valid_age(age):
#         if not isinstance(age,int):
#             return False
#         if age<0 or age>150:
#             return False
#         return True

# # Expected usage (NO instance needed):
# print(Validators.is_valid_email("test@example.com"))  # True
# print(Validators.is_valid_email("invalid-email"))     # False

# print(Validators.is_valid_password("pass123word"))    # True
# print(Validators.is_valid_password("short1"))         # False (too short)
# print(Validators.is_valid_password("nodigitshere"))   # False (no digit)

# print(Validators.is_valid_username("john_doe"))       # True
# print(Validators.is_valid_username("ab"))             # False (too short)
# print(Validators.is_valid_username("invalid-name"))   # False (contains hyphen)

# print(Validators.is_valid_age(25))    # True
# print(Validators.is_valid_age(-5))    # False
# print(Validators.is_valid_age(200))   # False
# print(Validators.is_valid_age("25"))  # False (not an integer)



# # Hour 2 Exercise 4

# # Your User class should:
# # 1. __init__ accepts: username, email, age
# # 2. Store all as instance attributes
# # 
# # Add these CLASS METHODS:
# # 3. from_dict(data) - creates User from dictionary
# # 4. from_string(data_string) - creates User from "username,email,age" format
# # 5. create_anonymous() - creates User with username="anonymous", 
# #                         email="anonymous@example.com", age=0

# class User:
#     def __init__(self,username,email,age):
#         self.username=username
#         self.email=email
#         self.age=age
#     @classmethod 
#     def from_dict(cls,data):
#         return cls(data["username"],data["email"],data["age"])
#     @classmethod
#     def from_string(cls,data_string):
#         usersList=data_string.split(",")
#         return cls(usersList[0].strip(),usersList[1].strip(),int(usersList[2].strip()))
#     @classmethod
#     def create_anonymous(cls):
#         return cls("anonymous","anonymous@example.com",0)

# # Expected usage:
# # Regular creation
# user1 = User("john_doe", "john@email.com", 25)
# print(user1.username)  # john_doe

# # From dictionary
# user_data = {"username": "jane_smith", "email": "jane@email.com", "age": 30}
# user2 = User.from_dict(user_data)
# print(user2.username)  # jane_smith
# print(user2.email)     # jane@email.com

# # From string
# user3 = User.from_string("bob_wilson,bob@email.com,35")
# print(user3.username)  # bob_wilson
# print(user3.age)       # 35 (should be an integer, not string!)

# # Anonymous user
# user4 = User.create_anonymous()
# print(user4.username)  # anonymous
# print(user4.email)     # anonymous@example.com
# print(user4.age)       # 0


# Hour 2 Exercise 5


# Your Order class should have:
#
# CLASS VARIABLES:
# - total_orders = 0
# - total_revenue = 0.0
# - orders_by_status = {"pending": 0, "shipped": 0, "delivered": 0, "cancelled": 0}
#
# INSTANCE VARIABLES (via __init__):
# - order_id (auto-generated: "ORD-001", "ORD-002", etc.)
# - customer_name
# - amount
# - status (default: "pending")
#
# Update class statistics when order is created!
#
# CLASS METHODS:
# - get_statistics() - returns dict with total_orders, total_revenue, orders_by_status
# - reset_statistics() - resets all class variables to initial values
#
# INSTANCE METHOD:
# - update_status(new_status) - updates status and adjusts orders_by_status counts

# class Order:
#     # CLASS VARIABLES:
#     total_orders = 0
#     total_revenue = 0.0
#     orders_by_status = {"pending": 0, "shipped": 0, "delivered": 0, "cancelled": 0}
    
#     def __init__(self,customer_name,amount,status="pending"):
#          self.customer_name=customer_name
#          self.amount=amount
#          self.status=status
#          self.order_id=f"ORD-{Order.total_orders+1                                                :03d}"

#         #  Tracking class variables
#          Order.total_orders+=1
#          Order.orders_by_status[status]+=1
#          Order.total_revenue+=amount
    
#     @classmethod
#     def get_statistics(cls):
#          return {
#               "total_orders":cls.total_orders,
#               "total_revenue":cls.total_revenue,
#               "orders_by_status":cls.orders_by_status
#          }
#     @classmethod
#     def reset_statistics(cls):
#          cls.total_orders=0
#          cls.total_revenue=0
#          cls.orders_by_status={"pending": 0, "shipped": 0, "delivered": 0, "cancelled": 0}
    
#     def update_status(self,new_status):
#          Order.orders_by_status[self.status]-=1
#          Order.orders_by_status[new_status]+=1
#          self.status=new_status

# # Expected usage:
# print(Order.get_statistics())
# # {'total_orders': 0, 'total_revenue': 0.0, 'orders_by_status': {...}}

# order1 = Order("John Doe", 150.00)
# order2 = Order("Jane Smith", 250.00)
# order3 = Order("Bob Wilson", 100.00)

# print(order1.order_id)  # ORD-001
# print(order2.order_id)  # ORD-002
# print(order3.order_id)  # ORD-003

# stats = Order.get_statistics()
# print(stats["total_orders"])   # 3
# print(stats["total_revenue"])  # 500.0
# print(stats["orders_by_status"]["pending"])  # 3

# # Update status
# order1.update_status("shipped")
# order2.update_status("delivered")

# stats = Order.get_statistics()
# print(stats["orders_by_status"]["pending"])    # 1
# print(stats["orders_by_status"]["shipped"])    # 1
# print(stats["orders_by_status"]["delivered"])  # 1

# # Reset for testing
# Order.reset_statistics()
# print(Order.total_orders)  # 0


# Hour 2 Exercise 6

# # Your Temperature class should:
# #
# # __init__ accepts: value, unit (default="C")
# # - unit can be "C" (Celsius), "F" (Fahrenheit), or "K" (Kelvin)
# # - Validate that unit is one of these, raise ValueError if not
# #
# # STATIC METHODS (conversion formulas):
# # - celsius_to_fahrenheit(c) -> returns (c * 9/5) + 32
# # - fahrenheit_to_celsius(f) -> returns (f - 32) * 5/9
# # - celsius_to_kelvin(c) -> returns c + 273.15
# # - kelvin_to_celsius(k) -> returns k - 273.15
# #
# # INSTANCE METHODS:
# # - to_celsius() -> returns value converted to Celsius
# # - to_fahrenheit() -> returns value converted to Fahrenheit  
# # - to_kelvin() -> returns value converted to Kelvin
# #
# # CLASS METHOD:
# # - from_fahrenheit(value) -> creates Temperature with that value converted to Celsius
# # - from_kelvin(value) -> creates Temperature with that value converted to Celsius


# class Temperature:
#     def __init__(self,value,unit="C"):
#         if not (unit =="C" or unit == "F" or unit=="K"):
#             raise ValueError("Invalid unit")
#         self.value=value
#         self.unit=unit
#     @classmethod
#     def from_fahrenheit(cls,value):
#         return cls(Temperature.fahrenheit_to_celsius(value),"C")
#     @classmethod
#     def from_kelvin(cls,value):
#         return cls(Temperature.kelvin_to_celsius(value),"C")
#     def to_celsius(self):
#         if self.unit == "F":
#             return Temperature.fahrenheit_to_celsius(self.value)
#         elif self.unit == "C":
#             return self.value
#         else:
#             return Temperature.kelvin_to_celsius(self.value)
#     def to_fahrenheit(self):
#         if self.unit=="F":
#             return self.value
#         if self.unit=="C":
#             return Temperature.celsius_to_fahrenheit(self.value)
#         return Temperature.celsius_to_fahrenheit(Temperature.kelvin_to_celsius(self.value))
#     def to_kelvin(self):
#         if self.unit=="C":
#             return Temperature.celsius_to_kelvin(self.value)
#         return Temperature.celsius_to_kelvin(Temperature.fahrenheit_to_celsius(self.value))
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return (c * (9/5)) + 32
#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f-32) * (5/9)
#     @staticmethod
#     def celsius_to_kelvin(c):
#         return c+273.15
#     @staticmethod
#     def kelvin_to_celsius(k):
#         return k-273.15
    

# # Expected usage:

# # Static methods work without instance
# print(Temperature.celsius_to_fahrenheit(0))    # 32.0
# print(Temperature.celsius_to_fahrenheit(100))  # 212.0
# print(Temperature.fahrenheit_to_celsius(32))   # 0.0
# print(Temperature.celsius_to_kelvin(0))        # 273.15

# # Create temperature in Celsius
# temp1 = Temperature(25, "C")
# print(temp1.to_fahrenheit())  # 77.0
# print(temp1.to_kelvin())      # 298.15
# print(temp1.to_celsius())     # 25

# # Create temperature in Fahrenheit
# temp2 = Temperature(98.6, "F")
# print(temp2.to_celsius())     # 37.0 (approximately)

# # Create temperature in Kelvin
# temp3 = Temperature(300, "K")
# print(temp3.to_celsius())     # 26.85 (approximately)

# # Factory methods
# temp4 = Temperature.from_fahrenheit(212)
# print(temp4.value)  # 100.0
# print(temp4.unit)   # C

# temp5 = Temperature.from_kelvin(373.15)
# print(temp5.value)  # 100.0
# print(temp5.unit)   # C

# Hour 2 Exercise 7

# Your Article class should have:
#
# ============ CLASS VARIABLES ============
# - VALID_CATEGORIES = ["tech", "lifestyle", "travel", "food", "other"]
# - total_articles = 0
# - total_views = 0
# - articles_by_category = {"tech": 0, "lifestyle": 0, "travel": 0, "food": 0, "other": 0}
#
# ============ INSTANCE VARIABLES ============
# - article_id (auto-generated: first 8 chars of uuid4)
# - title
# - content
# - author
# - category (default: "other", must be valid)
# - views (default: 0)
# - is_published (default: False)
# - created_at (auto-generated: datetime.now())
#
# ============ STATIC METHODS ============
# - generate_slug(title) -> lowercase, spaces replaced with hyphens
#   Example: "My First Post" -> "my-first-post"
# - estimate_reading_time(content) -> words / 200, rounded up to nearest integer
#   Example: 400 words -> 2 minutes, 250 words -> 2 minutes, 150 words -> 1 minute
#
# ============ CLASS METHODS ============
# - from_dict(data) -> create Article from dictionary
# - get_statistics() -> return dict with total_articles, total_views, articles_by_category
# - reset_statistics() -> reset all counters
#
# ============ INSTANCE METHODS ============
# - add_view() -> increment this article's views AND class total_views
# - publish() -> set is_published to True
# - to_dict() -> convert article to dictionary
# - get_slug() -> return slug for this article's title

# Expected usage:
import math,uuid,re
from datetime import datetime
class Article:
    # ============ CLASS VARIABLES ============
    VALID_CATEGORIES = ["tech", "lifestyle", "travel", "food", "other"]
    total_articles = 0
    total_views = 0
    articles_by_category = {"tech": 0, "lifestyle": 0, "travel": 0, "food": 0, "other": 0}
    def __init__(self,title,content,author,category="other",views=0,is_published=False):
        if not category in Article.VALID_CATEGORIES:
            raise ValueError("Invalid Categroy")
        self.category=category
        Article.articles_by_category[self.category]+=1
        Article.total_articles+=1
        self.created_at=datetime.now()
        self.article_id=str(uuid.uuid4())[:8]
        self.title=title
        self.content=content
        self.author=author
        self.views=views
        self.is_published=is_published
    # Class Methods
    @classmethod
    def from_dict(cls,data):
        return cls(data["title"],data["content"],data["author"],data["category"])
    @classmethod
    def get_statistics(cls):
        return {
            "total_articles":cls.total_articles,
            "total_views":cls.total_views,
            "articles_by_category":cls.articles_by_category
        }
    @classmethod 
    def reset_statistics(cls):
        cls.total_articles=0
        cls.total_views=0
        cls.articles_by_category={"tech": 0, "lifestyle": 0, "travel": 0, "food": 0, "other": 0}
    # Instance Methods
    def add_view(self):
        self.views+=1
        Article.total_views+=1
    def publish(self):
        self.is_published=True
    def to_dict(self):
        return {
            "article_id":self.article_id,
            "title":self.title,
            "content":self.content,
            "author":self.author,
            "category":self.category,
            "views":self.views,
            "is_published":self.is_published,
            "created_at":self.created_at
        }
    def get_slug(self):
        return Article.generate_slug(self.title)
    # Static Methods
    @staticmethod
    def generate_slug(title):
        return (title.replace(" ","-")).lower()
    @staticmethod
    def estimate_reading_time(content):
        words=len(re.findall(r"\w+",content))
        return math.ceil(words/200)
# Create articles
article1 = Article(
    title="Getting Started with Python",
    content="Python is a great programming language. " * 50,  # ~300 words
    author="john_doe",
    category="tech"
)

article2 = Article(
    title="Best Travel Destinations",
    content="Here are some amazing places to visit. " * 100,  # ~600 words
    author="jane_smith",
    category="travel"
)

# Check auto-generated fields
print(len(article1.article_id))  # 8
print(article1.views)            # 0
print(article1.is_published)     # False

# Static methods
print(Article.generate_slug("My Amazing Blog Post"))  # my-amazing-blog-post
print(Article.estimate_reading_time("word " * 400))   # 2

# Instance methods
article1.add_view()
article1.add_view()
article1.add_view()
print(article1.views)         # 3
print(Article.total_views)    # 3

article2.add_view()
print(Article.total_views)    # 4

article1.publish()
print(article1.is_published)  # True

print(article1.get_slug())    # getting-started-with-python

# Statistics
stats = Article.get_statistics()
print(stats["total_articles"])              # 2
print(stats["articles_by_category"]["tech"])    # 1
print(stats["articles_by_category"]["travel"])  # 1

# Factory method
data = {
    "title": "Delicious Recipes",
    "content": "Here are some recipes. " * 25,
    "author": "chef_bob",
    "category": "food"
}
article3 = Article.from_dict(data)
print(article3.title)     # Delicious Recipes
print(article3.category)  # food

# to_dict
article_dict = article1.to_dict()
print(article_dict["title"])       # Getting Started with Python
print(article_dict["author"])      # john_doe
print("article_id" in article_dict)  # True
print("created_at" in article_dict)  # True