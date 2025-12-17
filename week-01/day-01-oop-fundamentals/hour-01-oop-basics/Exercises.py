#Day 1 Hour 1 Exercise 1
#  Your Book class should:
# 1. Accept title, author, and pages in __init__
# 2. Store all three as instance attributes




class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
# Expected usage:
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Clean Code", "Robert Martin", 464)

print(book1.title)   # Python Crash Course
print(book1.author)  # Eric Matthes
print(book1.pages)   # 544

print(book2.title)   # Clean Code



#Day 2 Hour 2 Exercise 2


# Your Product class should:
# 1. Accept: name (required), price (required), quantity (default=0), category (default="General")
# 2. Store all as instance attributes
class Product:
    def __init__(self,name,price,quantity=0,category="General"):
        if not name:
            raise ValueError("Name is required")
        else:
            self.name=name
        if price is None or price<0:
            raise ValueError("Price is requireed")
        else:
            self.price=price
        self.quantity=quantity
        self.category=category
# Expected usage:
product1 = Product("Laptop", 999.99)
print(product1.name)      # Laptop
print(product1.price)     # 999.99
print(product1.quantity)  # 0
print(product1.category)  # General

product2 = Product("Mouse", 29.99, quantity=50, category="Electronics")
print(product2.quantity)  # 50
print(product2.category)  # Electronics


#Day 1 Hour 1 Exercise 3
# Your Rectangle class should:
# 1. Accept width and height in __init__
# 2. Store width, height, area, and perimeter as instance attributes
# 3. Calculate area = width * height
# 4. Calculate perimeter = 2 * (width + height)

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.area = width*height
        self.perimeter = 2*(width+height)

# Expected usage:
rect1 = Rectangle(5, 10)
print(rect1.width)      # 5
print(rect1.height)     # 10
print(rect1.area)       # 50
print(rect1.perimeter)  # 30

rect2 = Rectangle(3, 3)
print(rect2.area)       # 9
print(rect2.perimeter)  # 12


# Day 1 Hour 1 Exercise 4

# Your BankAccount class should:
# 1. Accept: account_holder (required), initial_balance (default=0)
# 2. Validate: account_holder must not be empty
# 3. Validate: initial_balance cannot be negative
# 4. Raise ValueError with descriptive message if validation fails
# 5. Store account_holder and balance as instance attributes

class BankAccount:
    def __init__(self,account_holder,initial_balance=0):
        if not account_holder:
            raise ValueError("Account holder is requird")
        else:
            self.account_holder=account_holder
        if  initial_balance<0:
            raise ValueError("Balance can never be negative")
        else:
            self.initial_balance=initial_balance

# Expected usage:

acc1 = BankAccount("John Doe", 1000)
print(acc1.account_holder)  # John Doe
print(acc1.initial_balance)         # 1000

acc2 = BankAccount("Jane Smith")
print(acc2.initial_balance)         # 0
# These should raise ValueError:
# acc2=BankAccount("", 100)           # Error: Account holder name cannot be empty
# BankAccount("John", -500)      # Error: Initial balance cannot be negative


#Day 1 Hour 1 Exercise 5
# Your Employee class should:
# 1. Accept: first_name, last_name, department, salary
# 2. Auto-generate employee_id in format "EMP-001", "EMP-002", etc.
#    (Hint: use a counter that tracks how many employees were created)
# 3. Auto-generate email in format: first_name.last_name@company.com (lowercase)
# 4. Store all attributes including auto-generated ones
# Write your Employee class here

class Employee:
    employee_count = 0
    # Your code here
    def __init__(self,first_name,last_name,department,salary):
        Employee.employee_count += 1
        self.first_name=first_name
        self.last_name=last_name
        self.department=department
        self.salary=salary
        self.email=f"{first_name.lower()}.{last_name.lower()}@company.com"
        self.employee_id=f"EMP-{Employee.employee_count:03d}"
# Expected usage:
emp1 = Employee("John", "Doe", "Engineering", 75000)
print(emp1.employee_id)   # EMP-001
print(emp1.first_name)    # John
print(emp1.last_name)     # Doe
print(emp1.email)         # john.doe@company.com
print(emp1.department)    # Engineering
print(emp1.salary)        # 75000

emp2 = Employee("Jane", "Smith", "Marketing", 65000)
print(emp2.employee_id)   # EMP-002
print(emp2.email)         # jane.smith@company.com

emp3 = Employee("Bob", "Wilson", "Sales", 55000)
print(emp3.employee_id)   # EMP-003

# Day 1 Hour 1 Exercise 6

# Your ShoppingCart class should:
# 1. Accept: customer_name (required)
# 2. Initialize an empty list called 'items'
# 3. Initialize total_value as 0
# 4. DON'T use mutable default argument (remember the gotcha!)

class ShoppingCart:
    def __init__(self,customer_name):
        if not customer_name:
            raise ValueError("Customer Name is required")
        else:
            self.customer_name=customer_name
        self.items=[]
        self.total_value=0

# Expected usage:
cart1 = ShoppingCart("John")
print(cart1.customer_name)  # John
print(cart1.items)          # []
print(cart1.total_value)    # 0

cart2 = ShoppingCart("Jane")
print(cart2.items)          # [] (should be separate from cart1!)

# Modify cart1
cart1.items.append({"name": "Laptop", "price": 999})
cart1.total_value = 999
cart1.total_value=1000

# cart2 should NOT be affected
print(len(cart1.items))     # 1
print(len(cart2.items))     # 0 (not affected!)


#Day 1 Hour 1 Exercise 7

# Your BlogPost class should:
# 1. Accept: title (required), content (required), author (required)
# 2. Accept: tags (default=None, should become empty list)
# 3. Accept: published (default=False)
# 4. Validate: title must be at least 5 characters
# 5. Validate: content must be at least 10 characters
# 6. Auto-generate: post_id (use uuid.uuid4(), take first 8 characters)
# 7. Auto-generate: created_at (use datetime.now())
# 8. Auto-generate: slug from title (lowercase, spaces replaced with dashes)
#    Example: "My First Post" -> "my-first-post"
# 9. Calculate: word_count from content (split by spaces and count)
from datetime import datetime
import uuid
class BlogPost:
    def __init__(self,title,content,author,tags=None,published=False):
        # Basic validation process
        if len(title)<5:
            raise ValueError("Title length must be atleast 5 characters")
        else:
            self.title=title
        if len(content)<10:
            raise ValueError("Content length must be atleast 10 characters")
        else:
            self.content=content
        if not author:
            raise ValueError("Author is required")
        self.author=author
        if not tags:
             self.tags=[]
        else:
            self.tags=tags
        self.published=published
        self.post_id=self._generate_id()
        self.created_at=datetime.now()
        self.slug=title.replace(" ","-").lower()
        self.word_count=len(content.split(" "))

    def _generate_id(self):
        return str(uuid.uuid4())[:8]
# Expected usage:
post1 = BlogPost(
    title="My First Blog Post",
    content="This is the content of my very first blog post on this platform.",
    author="john_doe"
)

print(post1.post_id)      # Something like: a1b2c3d4
print(post1.title)        # My First Blog Post
print(post1.slug)         # my-first-blog-post
print(post1.author)       # john_doe
print(post1.word_count)   # 12 (count words in content)
print(post1.tags)         # []
print(post1.published)    # False
print(type(post1.created_at))  # <class 'datetime.datetime'>

post2 = BlogPost(
    title="Python Tips and Tricks",
    content="Here are some useful Python tips that every developer should know.",
    author="jane_smith",
    tags=["python", "programming", "tips"],
    published=True
)

print(post2.slug)         # python-tips-and-tricks
print(post2.tags)         # ['python', 'programming', 'tips']
print(post2.published)    # True

# These should raise ValueError:
# BlogPost("Hi", "Valid content here", "author")  # Title too short
# BlogPost("Valid Title", "Short", "author")      # Content too short