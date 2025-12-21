from datetime import datetime
import uuid
class BankAccount:
    def __init__(self,holder_name, email, initial_deposit, pin):
        if initial_deposit < 100:
           raise ValueError("Initial deposit must be at least $100")
        else:
            self.__balance=initial_deposit
        self._holder_name=holder_name.title()
        self._email=email.lower()
        self._is_frozen=False
        self.__pin=pin
        self.__account_number=str(uuid.uuid4())[:8]
        self.__created_at=datetime.now()
        self.__transaction_history=[
            {
                "type": "debit", "amount": initial_deposit, "description": "It's initial deposit", "timestamp": datetime.now(), "balance_after": initial_deposit
            }
        ]

    @property
    def account_number(self):
        return self.__account_number
    @property
    def balance(self):
        return self.__balance
    @property
    def transaction_count(self):
        return len(self.__transaction_history)
    @property
    def created_at(self):
        return self.__created_at
    @property
    def holder_name(self):
        return self._holder_name
    @property
    def email(self):
        return self._email
    @property
    def is_frozen(self):
        return self._is_frozen
    @property
    def pin(self):
        raise AttributeError("Security: PIN is write-only for security")
    @balance.setter
    def balance(self,val):
        raise AttributeError("Cannot set balance directly!")
    @holder_name.setter
    def holder_name(self,value):
        if len(value)<2:
            raise ValueError("Length must be atleast 2")
        self._holder_name=value.title()
    @email.setter
    def email(self,val):
        if "@" not in val or "." not in val:
            raise ValueError("Invalid email")
        self._email=val.lower()
    @is_frozen.setter
    def is_frozen(self,val):
        if not isinstance(val,bool):
            raise ValueError("Should be boolean value")
        self._is_frozen=val
    @pin.setter
    def pin(self,val):
        if not isinstance(val,str):
            raise ValueError("Pin must be digits")
        elif  len(val)!=4:
            raise ValueError("Pin must be atleast 4 digits")
        elif not val.isdigit():
            raise ValueError("Pin must be digits")
        else:
            self.__pin=val
    def verify_pin(self,pin):
        return self.__pin==pin
    # ============ COMPUTED PROPERTIES ============
# - display_balance -> returns formatted: "$1,234.56"
# - account_summary -> returns: "ACC12345678 | John Doe | $1,234.56"
# - account_age_days -> returns days since account creation
    @property
    def display_balance(self):
        return f"${self.__balance}"
    @property
    def account_summary(self):
        return f"{self.__account_number} | {self._holder_name} | ${self.__balance}"
    @property
    def account_age_days(self):
        return (datetime.now() - self.__created_at).days
    def deposit(self,amount, description="Deposit"):
        if self._is_frozen:
            raise ValueError("Account is frozen")
        elif amount <=0:
            raise ValueError("Invalid Amount")
        else:
            self.__balance+=amount
            record={
                "type": "credit", "amount": amount, "description": description, "timestamp": datetime.now(), "balance_after": self.__balance
            }
            self.__transaction_history.append(record)
            return self.__balance
    def withdraw(self,amount, pin, description="Withdrawal"):
        if not self.verify_pin(pin):
            raise ValueError("Incorrect Pin")
        elif self._is_frozen:
            raise ValueError("Account is frozen")
        elif amount>self.balance or amount<0:
            raise ValueError("Insufficient funds")
        else:
            self.__balance-=amount
            current={"type": "debit", "amount": amount, "description": description, "timestamp": datetime.now(), "balance_after": self.__balance}
            self.__transaction_history.append(current)
        return self.__balance
    def get_statement(self,last_n=5):
        return self.__transaction_history[-last_n:]
    # - to_dict():
#   - Return dict with: account_number, holder_name, email, balance, is_frozen, created_at, transaction_count
#   - NEVER include pin or transaction_history!
    def to_dict(self):
        return{
            "account_number":self.__account_number,
            "holder_name":self._holder_name,
            "email":self._email,
            "balance":self.__balance,
            "is_frozen":self._is_frozen,
            "created_at":self.__created_at,
            "transaction_count":len(self.__transaction_history)
        }
# ============ PRIVATE ATTRIBUTES (use __) ============
# - __account_number (auto-generated: "ACC" + 8 random digits)
# - __pin (stored as string, never exposed)
# - __balance (never accessed directly)
# - __created_at (datetime.now())
# - __transaction_history (list of dicts)
#
# ============ PROTECTED ATTRIBUTES (use _) ============
# - _holder_name
# - _email
# - _is_frozen (default: False)
#
# ============ CONSTRUCTOR ============
# __init__(self, holder_name, email, initial_deposit, pin):
# - Validate and set all attributes using property setters where applicable
# - pin must be exactly 4 digits (validate!)
# - initial_deposit must be >= 100 (minimum opening balance)
# - Add initial deposit to transaction history
#
# ============ READ-ONLY PROPERTIES ============
# - account_number -> returns __account_number
# - created_at -> returns __created_at
# - balance -> returns __balance (read-only, can't set directly)
# - transaction_count -> returns length of __transaction_history
#
# ============ READ-WRITE PROPERTIES (with validation) ============
# - holder_name:
#   - Getter: returns _holder_name
#   - Setter: must be at least 2 characters, title case it
#
# - email:
#   - Getter: returns _email
#   - Setter: must contain "@" and ".", lowercase it
#
# - is_frozen:
#   - Getter: returns _is_frozen
#   - Setter: accepts boolean only
#
# ============ WRITE-ONLY PROPERTY ============
# - pin:
#   - Getter: raise AttributeError("PIN is write-only for security")
#   - Setter: must be exactly 4 digits (string), store it
#
# ============ COMPUTED PROPERTIES ============
# - display_balance -> returns formatted: "$1,234.56"
# - account_summary -> returns: "ACC12345678 | John Doe | $1,234.56"
# - account_age_days -> returns days since account creation
#
# ============ METHODS ============
# - verify_pin(pin) -> returns True if pin matches, False otherwise
#
# - deposit(amount, description="Deposit"):
#   - Raise error if account is frozen
#   - Raise error if amount <= 0
#   - Add to balance
#   - Record transaction: {"type": "credit", "amount": amount, "description": description, "timestamp": ..., "balance_after": ...}
#   - Return new balance
#
# - withdraw(amount, pin, description="Withdrawal"):
#   - Raise error if account is frozen
#   - Raise error if pin is incorrect
#   - Raise error if amount <= 0
#   - Raise error if amount > balance (insufficient funds)
#   - Subtract from balance
#   - Record transaction: {"type": "debit", "amount": amount, "description": description, "timestamp": ..., "balance_after": ...}
#   - Return new balance
#
# - get_statement(last_n=5):
#   - Return last N transactions (most recent first)
#
# - to_dict():
#   - Return dict with: account_number, holder_name, email, balance, is_frozen, created_at, transaction_count
#   - NEVER include pin or transaction_history!


# ============ EXPECTED USAGE ============

# Create account
account = BankAccount(
    holder_name="john doe",
    email="JOHN@EMAIL.COM",
    initial_deposit=500,
    pin="1234"
)

# Read-only properties
print(account.account_number)    # ACC12345678 (random)
print(account.balance)           # 500
print(account.transaction_count) # 1 (initial deposit)

# Computed properties
print(account.display_balance)   # $500.00
print(account.account_summary)   # ACC12345678 | John Doe | $500.00

# Holder name was title-cased
print(account.holder_name)       # John Doe

# Email was lowercased
print(account.email)             # john@email.com

# Cannot read PIN
try:
    print(account.pin)
except AttributeError as e:
    print(f"Security: {e}")  # Security: PIN is write-only for security

# But can verify PIN
print(account.verify_pin("1234"))  # True
print(account.verify_pin("0000"))  # False

# Cannot set balance directly
try:
    account.balance = 999999
except AttributeError:
    print("Cannot set balance directly!")

# Deposit money
new_balance = account.deposit(250, "Birthday gift")
print(f"After deposit: ${new_balance}")  # After deposit: $750

# Withdraw money (requires correct PIN)
new_balance = account.withdraw(100, "1234", "ATM withdrawal")
print(f"After withdrawal: ${new_balance}")  # After withdrawal: $650

# Wrong PIN
try:
    account.withdraw(50, "0000")
except ValueError as e:
    print(f"Error: {e}")  # Error: Incorrect PIN

# Insufficient funds
try:
    account.withdraw(1000, "1234")
except ValueError as e:
    print(f"Error: {e}")  # Error: Insufficient funds

# Get transaction statement
print("\nTransaction History:")
for tx in account.get_statement(last_n=3):
    print(f"  {tx['type'].upper()}: ${tx['amount']} - {tx['description']}")

# Freeze account
account.is_frozen = True
try:
    account.deposit(100)
except ValueError as e:
    print(f"Error: {e}")  # Error: Account is frozen

# Unfreeze and update details
account.is_frozen = False
account.holder_name = "john smith"
account.email = "john.smith@email.com"
print(account.holder_name)  # John Smith
print(account.email)        # john.smith@email.com

# Change PIN
account.pin = "5678"
print(account.verify_pin("5678"))  # True
print(account.verify_pin("1234"))  # False (old PIN no longer works)

# Validation errors
try:
    account.holder_name = "A"  # Too short
except ValueError as e:
    print(f"Error: {e}")

try:
    account.email = "invalid-email"  # No @ or .
except ValueError as e:
    print(f"Error: {e}")

try:
    account.pin = "12"  # Not 4 digits
except ValueError as e:
    print(f"Error: {e}")

try:
    account.pin = "abcd"  # Not digits
except ValueError as e:
    print(f"Error: {e}")

# Final summary
print("\n" + "=" * 50)
print("Account Summary:")
print(account.to_dict())

# Validation on creation
try:
    bad_account = BankAccount("Test", "test@email.com", 50, "1234")  # initial_deposit too low
except ValueError as e:
    print(f"Creation error: {e}")  # Creation error: Initial deposit must be at least $100