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

# class Notification:
#     def __init__(self, recipient, message):
#         self.recipient=recipient
#         self.message=message

#     def send(self):
#         return f"Sending to {self.recipient} {self.message}"
#     def get_log(self):
#         return f"[NOTIFICATION] {self.recipient}"

# # CHILD CLASS: EmailNotification(Notification)
# # - __init__(self, recipient, message, subject)
# # - Call parent's __init__ using super()
# # - Store subject as instance attribute
# # - Override send() -> returns "Sending EMAIL to {recipient}\nSubject: {subject}\nBody: {message}"
# # - Override get_log() -> call parent's get_log() and append " via EMAIL"
# class EmailNotification(Notification):
#     def __init__(self, recipient, message,subject):
#         super().__init__(recipient, message)
#         self.subject=subject

#     def send(self):
#         return f"Sending EMAIL to {self.recipient}\nSubject: {self.subject}\nBody: {self.message}"
#     def get_log(self):
#         return super().get_log() + f" via EMAIL"
# # CHILD CLASS: SMSNotification(Notification)
# # - __init__(self, recipient, message)
# # - Call parent's __init__ using super()
# # - Store character_count as instance attribute (length of message)
# # - Override send() -> returns "Sending SMS to {recipient}: {message} ({character_count} chars)"
# # - Override get_log() -> call parent's get_log() and append " via SMS"
# class SMSNotification(Notification):
#     def __init__(self, recipient, message):
#         super().__init__(recipient, message)
#         self.character_count=len(message)
#     def send(self):
#         return f"Sending SMS to {self.recipient}: {self.message} ({self.character_count} chars)"
#     def get_log(self):
#         return super().get_log()+" via SMS"
# # CHILD CLASS: PushNotification(Notification)
# # - __init__(self, recipient, message, device_token)
# # - Call parent's __init__ using super()
# # - Store device_token as instance attribute
# # - Override send() -> returns "Sending PUSH to device {device_token}: {message}"
# # - Override get_log() -> call parent's get_log() and append " via PUSH"
# class PushNotification(Notification):
#     def __init__(self, recipient, message,device_token):
#         super().__init__(recipient, message)
#         self.device_token=device_token
#     def send(self):
#         return f"Sending PUSH to device {self.device_token}: {self.message}"
#     def get_log(self):
#         return super().get_log()+" via Push"
# # Expected usage:
# base = Notification("user@email.com", "Hello!")
# print(base.send())     # Sending to user@email.com: Hello!
# print(base.get_log())  # [NOTIFICATION] user@email.com

# email = EmailNotification("user@email.com", "Welcome to our platform!", "Welcome")
# print(email.send())
# # Sending EMAIL to user@email.com
# # Subject: Welcome
# # Body: Welcome to our platform!
# print(email.get_log())  # [NOTIFICATION] user@email.com via EMAIL

# sms = SMSNotification("+1234567890", "Your code is 123456")
# print(sms.send())       # Sending SMS to +1234567890: Your code is 123456 (20 chars)
# print(sms.character_count)  # 20
# print(sms.get_log())    # [NOTIFICATION] +1234567890 via SMS

# push = PushNotification("user123", "New message!", "device_abc123")
# print(push.send())      # Sending PUSH to device device_abc123: New message!
# print(push.get_log())   # [NOTIFICATION] user123 via PUSH




# Day 1 Hour 3 one combined exercise

import json
from datetime import datetime

# CLASS: APIResponse (Base)
#
# __init__(self, data, message="Success"):
# - Store: data, message, timestamp=datetime.now().isoformat(), status_code=200
#
# Instance Methods:
# - to_dict() -> returns {"status_code": ..., "message": ..., "data": ..., "timestamp": ...}
# - to_json() -> returns JSON string of to_dict() with indent=2
# - is_success() -> returns True if status_code is between 200-299
class APIResponse:
    def __init__(self, data, message="Success"):
        self.data=data
        self.message=message
        self.timestamp=datetime.now().isoformat()
        self.status_code=200
    def to_dict(self):
        return{
            "status_code":self.status_code,
            "message":self.message,
            "data":self.data,
            "timestamp":self.timestamp
        }
    def to_json(self):
        return json.dumps(self.to_dict(),indent=2)
    def is_success(self):
        return 200<=self.status_code<300

# CLASS: SuccessResponse(APIResponse)
#
# __init__(self, data, message="Success"):
# - Call parent's __init__
# - Set status_code = 200
#
# Override:
# - to_dict() -> get parent's dict, add "success": True
class SuccessResponse(APIResponse):
    def __init__(self, data, message="Success"):
        super().__init__(data, message)
        self.status_code=200

    def to_dict(self):
         dic=super().to_dict()
         dic["success"]=True
         return dic

# CLASS: CreatedResponse(APIResponse)
#
# __init__(self, data, resource_id, message="Resource created"):
# - Call parent's __init__
# - Set status_code = 201
# - Store resource_id
#
# Override:
# - to_dict() -> get parent's dict, add "success": True and "resource_id": ...
class CreateResponse(APIResponse):
    def __init__(self, data, resource_id,message="Resource created"):
        super().__init__(data, message)
        self.resource_id=resource_id
        self.status_code=201
    def to_dict(self):
        dic=super().to_dict()
        dic["success"]=True
        dic["resource_id"]=self.resource_id
        return dic
# CLASS: ErrorResponse(APIResponse)
#
# __init__(self, message, error_code=None, status_code=400):
# - Call parent's __init__ with data=None and message
# - Override status_code with the passed value
# - Store error_code
#
# Override:
# - to_dict() -> get parent's dict, add "success": False and "error_code": ...
# - is_success() -> always returns False

class ErrorResponse(APIResponse):
    def __init__(self, message,error_code=None,status_code=400):
        super().__init__(None,message)
        self.status_code=status_code
        self.error_code=error_code
    def to_dict(self):
        dic=super().to_dict()
        dic["success"]=False
        dic["error_code"]=self.error_code
        return dic
    def is_success(self):
        return False

# CLASS: NotFoundResponse(ErrorResponse)
#
# __init__(self, resource_type, resource_id):
# - Call parent's __init__ with:
#   - message = "{resource_type} with id '{resource_id}' not found"
#   - error_code = "NOT_FOUND"
#   - status_code = 404
# - Store resource_type and resource_id
#
# Override:
# - to_dict() -> get parent's dict, add "resource_type": ... and "resource_id": ...
class NotFoundResponse(ErrorResponse):
    def __init__(self,resource_type,resource_id):
        super().__init__(message=f"{resource_type} with id '{resource_id}' not found", error_code="NOT_FOUND", status_code=404)
        self.resource_type=resource_type
        self.resource_id=resource_id
    def to_dict(self):
        dic=super().to_dict()
        dic["resource_type"]=self.resource_type
        dic["resource_id"]=self.resource_id
        return dic


# Expected usage:

# Success Response
success = SuccessResponse({"user": "john", "email": "john@email.com"})
print(success.status_code)    # 200
print(success.is_success())   # True
print(success.to_dict())
# {
#   'status_code': 200,
#   'message': 'Success',
#   'data': {'user': 'john', 'email': 'john@email.com'},
#   'timestamp': '2024-01-15T10:30:00',
#   'success': True
# }

# Created Response
created = CreateResponse({"name": "New Product"}, resource_id="prod_123")
print(created.status_code)    # 201
print(created.is_success())   # True
created_dict = created.to_dict()
print(created_dict["resource_id"])  # prod_123
print(created_dict["success"])      # True

# Error Response
error = ErrorResponse("Invalid email format", error_code="VALIDATION_ERROR")
print(error.status_code)      # 400
print(error.is_success())     # False
print(error.to_dict())
# {
#   'status_code': 400,
#   'message': 'Invalid email format',
#   'data': None,
#   'timestamp': '...',
#   'success': False,
#   'error_code': 'VALIDATION_ERROR'
# }

# Not Found Response
not_found = NotFoundResponse("User", "user_456")
print(not_found.status_code)   # 404
print(not_found.message)       # User with id 'user_456' not found
print(not_found.is_success())  # False
not_found_dict = not_found.to_dict()
print(not_found_dict["error_code"])     # NOT_FOUND
print(not_found_dict["resource_type"])  # User
print(not_found_dict["resource_id"])    # user_456

# JSON output
print(success.to_json())
# Pretty printed JSON

# Inheritance checks
print(isinstance(not_found, ErrorResponse))  # True
print(isinstance(not_found, APIResponse))    # True
print(isinstance(created, APIResponse))      # True