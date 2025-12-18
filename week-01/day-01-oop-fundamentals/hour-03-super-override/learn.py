# In this example we have coded inheritance with methods inheritance

from datetime import datetime
import uuid


class BaseRepository:
    """
    Base repository with common CRUD operations.
    Child repositories inherit these and add entity-specific methods.
    """
    
    def __init__(self):
        self.data = {}  # In-memory storage (would be DB in real app)
    
    def generate_id(self):
        """Generate a unique ID."""
        return str(uuid.uuid4())[:8]
    
    def get_all(self):
        """Get all records."""
        return list(self.data.values())
    
    def get_by_id(self, id):
        """Get a record by ID."""
        # return self.data[id]
        # or
        # return self.data.get(id)
    
    def delete(self, id):
        """Delete a record by ID."""
        if id in self.data:
            del self.data[id]
            return True
        return False
    
    def count(self):
        """Get total count of records."""
        return len(self.data)


class UserRepository(BaseRepository):
    """Repository for User entities."""
    
    def create(self, username, email):
        """Create a new user."""
        user_id = self.generate_id()
        user = {
            "id": user_id,
            "username": username,
            "email": email,
            "created_at": datetime.now().isoformat(),
            "type": "user"
        }
        self.data[user_id] = user
        return user
    
    def get_by_email(self, email):
        """Find user by email - User-specific method."""
        for user in self.data.values():
            if user["email"] == email:
                return user
        return None
    
    def get_by_username(self, username):
        """Find user by username - User-specific method."""
        for user in self.data.values():
            if user["username"] == username:
                return user
        return None


class ProductRepository(BaseRepository):
    """Repository for Product entities."""
    
    def create(self, name, price, category):
        """Create a new product."""
        product_id = self.generate_id()
        product = {
            "id": product_id,
            "name": name,
            "price": price,
            "category": category,
            "created_at": datetime.now().isoformat(),
            "type": "product"
        }
        self.data[product_id] = product
        return product
    
    def get_by_category(self, category):
        """Find products by category - Product-specific method."""
        return [p for p in self.data.values() if p["category"] == category]
    
    def get_price_range(self, min_price, max_price):
        """Find products in price range - Product-specific method."""
        return [
            p for p in self.data.values()
            if min_price <= p["price"] <= max_price
        ]


# Usage demonstration
print("=" * 60)
print("User Repository")
print("=" * 60)

user_repo = UserRepository()

# Create users (using inherited generate_id and custom create)
user1 = user_repo.create("john_doe", "john@email.com")
user2 = user_repo.create("jane_smith", "jane@email.com")

print(f"Created: {user1}")
print(f"Total users: {user_repo.count()}")  # Inherited method

# Use inherited method
all_users = user_repo.get_all()  # Inherited from BaseRepository
print(f"All users: {len(all_users)}")

# Use custom method
found = user_repo.get_by_email("john@email.com")
print(f"Found by email: {found['username']}")

print("\n" + "=" * 60)
print("Product Repository")
print("=" * 60)

product_repo = ProductRepository()

# Create products
product_repo.create("Laptop", 999.99, "Electronics")
product_repo.create("Mouse", 29.99, "Electronics")
product_repo.create("Desk", 199.99, "Furniture")
product_repo.create("Chair", 149.99, "Furniture")

print(f"Total products: {product_repo.count()}")  # Inherited method

# Use custom method
electronics = product_repo.get_by_category("Electronics")
print(f"Electronics: {[p['name'] for p in electronics]}")

affordable = product_repo.get_price_range(0, 200)
print(f"Under $200: {[p['name'] for p in affordable]}")