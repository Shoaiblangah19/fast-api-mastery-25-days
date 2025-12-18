# Day 1 Hour 3 Exercise 1

# # PARENT CLASS: Person
# # - __init__(self, name, age, email)
# # - Store all as instance attributes
# # - Method: get_info() -> returns "Name: {name}, Age: {age}"

# # CHILD CLASS: Student(Person)
# # - __init__(self, name, age, email, student_id, grade)
# # - Call parent's __init__ using super()
# # - Store student_id and grade as instance attributes
# # - Method: study(subject) -> returns "{name} is studying {subject}"

# # CHILD CLASS: Teacher(Person)
# # - __init__(self, name, age, email, employee_id, subject)
# # - Call parent's __init__ using super()
# # - Store employee_id and subject as instance attributes
# # - Method: teach() -> returns "{name} is teaching {subject}"
# class Person:
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age}"
    
# class Student(Person):
#     def __init__(self, name, age, email,student_id,grade):
#         super().__init__(name, age, email)
#         self.student_id=student_id
#         self.grade=grade
#     def study(self,subject):
#         return f"{self.name} is studying {subject}"
# class Teacher(Person):
#     def __init__(self, name, age, email,employee_id,subject):
#         super().__init__(name, age, email)
#         self.employee_id=employee_id
#         self.subject=subject
#     def teach(self):
#         return f"{self.name} is teaching {self.subject}"
# # Expected usage:
# person = Person("John", 30, "john@email.com")
# print(person.get_info())  # Name: John, Age: 30

# student = Student("Alice", 20, "alice@email.com", "STU001", "A")
# print(student.get_info())     # Name: Alice, Age: 20 (inherited)
# print(student.name)           # Alice (inherited)
# print(student.student_id)     # STU001
# print(student.grade)          # A
# print(student.study("Math"))  # Alice is studying Math

# teacher = Teacher("Mr. Smith", 45, "smith@email.com", "TCH001", "Physics")
# print(teacher.get_info())     # Name: Mr. Smith, Age: 45 (inherited)
# print(teacher.subject)        # Physics
# print(teacher.teach())        # Mr. Smith is teaching Physics

# # Check inheritance
# print(isinstance(student, Person))  # True
# print(isinstance(teacher, Person))  # True


# Day 1 Hour 3 Exercise 2

# PARENT CLASS: Notification
# - __init__(self, recipient, message)
# - Store both as instance attributes
# - Method: send() -> returns "Sending to {recipient}: {message}"
# - Method: get_log() -> returns "[NOTIFICATION] {recipient}"

# CHILD CLASS: EmailNotification(Notification)
# - __init__(self, recipient, message, subject)
# - Call parent's __init__ using super()
# - Store subject as instance attribute
# - Override send() -> returns "Sending EMAIL to {recipient}\nSubject: {subject}\nBody: {message}"
# - Override get_log() -> call parent's get_log() and append " via EMAIL"

# CHILD CLASS: SMSNotification(Notification)
# - __init__(self, recipient, message)
# - Call parent's __init__ using super()
# - Store character_count as instance attribute (length of message)
# - Override send() -> returns "Sending SMS to {recipient}: {message} ({character_count} chars)"
# - Override get_log() -> call parent's get_log() and append " via SMS"

# CHILD CLASS: PushNotification(Notification)
# - __init__(self, recipient, message, device_token)
# - Call parent's __init__ using super()
# - Store device_token as instance attribute
# - Override send() -> returns "Sending PUSH to device {device_token}: {message}"
# - Override get_log() -> call parent's get_log() and append " via PUSH"

class Notification:
    def __init__(self, recipient, message):
        self.recipient=recipient
        self.message=message

    def send(self):
        return f"Sending to {self.recipient} {self.message}"
    def get_log(self):
        return f"[NOTIFICATION] {self.recipient}"

# CHILD CLASS: EmailNotification(Notification)
# - __init__(self, recipient, message, subject)
# - Call parent's __init__ using super()
# - Store subject as instance attribute
# - Override send() -> returns "Sending EMAIL to {recipient}\nSubject: {subject}\nBody: {message}"
# - Override get_log() -> call parent's get_log() and append " via EMAIL"
class EmailNotification(Notification):
    def __init__(self, recipient, message,subject):
        super().__init__(recipient, message)
        self.subject=subject

    def send(self):
        return f"Sending EMAIL to {self.recipient}\nSubject: {self.subject}\nBody: {self.message}"
    def get_log(self):
        return super().get_log() + f" via EMAIL"
# CHILD CLASS: SMSNotification(Notification)
# - __init__(self, recipient, message)
# - Call parent's __init__ using super()
# - Store character_count as instance attribute (length of message)
# - Override send() -> returns "Sending SMS to {recipient}: {message} ({character_count} chars)"
# - Override get_log() -> call parent's get_log() and append " via SMS"
class SMSNotification(Notification):
    def __init__(self, recipient, message):
        super().__init__(recipient, message)
        self.character_count=len(message)
    def send(self):
        return f"Sending SMS to {self.recipient}: {self.message} ({self.character_count} chars)"
    def get_log(self):
        return super().get_log()+" via SMS"
# CHILD CLASS: PushNotification(Notification)
# - __init__(self, recipient, message, device_token)
# - Call parent's __init__ using super()
# - Store device_token as instance attribute
# - Override send() -> returns "Sending PUSH to device {device_token}: {message}"
# - Override get_log() -> call parent's get_log() and append " via PUSH"
class PushNotification(Notification):
    def __init__(self, recipient, message,device_token):
        super().__init__(recipient, message)
        self.device_token=device_token
    def send(self):
        return f"Sending PUSH to device {self.device_token}: {self.message}"
    def get_log(self):
        return super().get_log()+" via Push"
# Expected usage:
base = Notification("user@email.com", "Hello!")
print(base.send())     # Sending to user@email.com: Hello!
print(base.get_log())  # [NOTIFICATION] user@email.com

email = EmailNotification("user@email.com", "Welcome to our platform!", "Welcome")
print(email.send())
# Sending EMAIL to user@email.com
# Subject: Welcome
# Body: Welcome to our platform!
print(email.get_log())  # [NOTIFICATION] user@email.com via EMAIL

sms = SMSNotification("+1234567890", "Your code is 123456")
print(sms.send())       # Sending SMS to +1234567890: Your code is 123456 (20 chars)
print(sms.character_count)  # 20
print(sms.get_log())    # [NOTIFICATION] +1234567890 via SMS

push = PushNotification("user123", "New message!", "device_abc123")
print(push.send())      # Sending PUSH to device device_abc123: New message!
print(push.get_log())   # [NOTIFICATION] user123 via PUSH