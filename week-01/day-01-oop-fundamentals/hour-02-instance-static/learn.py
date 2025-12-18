# print("Learning class and instance variable and static")

# # Differentiation b/w class and instance variable
# class DatabaseConnections:
#     # These four variables are class variables and they are same and available for each object
#     port=3000
#     host="localhost"
#     total=0
#     max=10
#     def __init__(self,db):
#         if DatabaseConnections.total>=DatabaseConnections.max:
#             raise ValueError("Maximum Database Connections reached")
#         # These are instance variables and specified for each variable
#         self.db=db
#         self.isConnected=True
#         DatabaseConnections.total+=1
#     def _disconnect(self):
#         if self.isConnected:
#             self.isConnected=False
#             DatabaseConnections.total-=1

# conn1=DatabaseConnections("userdb")
# conn1=DatabaseConnections("userdb")

# # Best way to access and change class variable is using class name instead of instance
# # Accessing by instance is ok by changing by instance will create another variable
# print(DatabaseConnections.total)
# print(conn1.isConnected)

# conn1._disconnect()
# print(DatabaseConnections.total)
# print(conn1.isConnected)



# # Tracking instance variable
# class ApiRequests:
#     total_requests=0
#     request_by_method={
#         "GET":0,
#         "POST":0,
#         "PUT":0,
#         "DELETE":0
#     }
#     def __init__(self,method,path):
#         self.method=method
#         self.path=path

#         # Tracking instance variables
    
#         ApiRequests.total_requests+=1
#         ApiRequests.request_by_method[self.method]+=1
        

# req1=ApiRequests("GET","/api/users")
# req2=ApiRequests("POST","/api/users")
# req3=ApiRequests("PUT","/api/users")
# req4=ApiRequests("DELETE","/api/users")

# print(ApiRequests.total_requests)
# print(ApiRequests.request_by_method)


# Class Methods
# These methods are used to access/modify class variables

# class User:
#     total_users=0
#     def __init__(self,name):
#         self.name=name
#         User.total_users+=1
#     @classmethod
#     def get_total(cls):
#         return cls.total_users
    
# user1=User("Shoaib")
# user2=User("Javaid")
# print(user1.name)
# print(User.get_total())

# import hashlib
# passwo="shoaiblangah19"
# print(hashlib.sha256(passwo.encode()).hexdigest())


# A complete example for creating backend type password class using static methods meaningully
import random
import hashlib,string
class PasswordUtils:
    @staticmethod
    def hash_Pass(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_pass(password,hashed):
        return PasswordUtils.hash_Pass(password)==hashed
    
    @staticmethod
    def generate_pass(lenght):
        letters=string.ascii_letters
        digits=string.digits
        punctuations= string.punctuation
        chars=letters+digits+punctuations
        passwo=''
        for _ in range(lenght):
            passwo += random.choice(chars)
        return passwo
    
myPassword="Abcd123@#"
hashed=PasswordUtils.hash_Pass(myPassword)
isValid=PasswordUtils.verify_pass(myPassword,hashed)
print(isValid)