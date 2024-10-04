from os import name
from typing import Type


class User:
    def __init__(self, user_id: int, user_name: str) -> None:
        self.id = user_id
        self.name = user_name
    
    # Gets called when using the str method for an object 
    def __str__(self) -> str:
        return f"Id: {self.id}, Name: {self.name}"
    
    # Gets called when trying to pass an object to a "print" function
    def __repr__(self) -> str:
        return self.__str__()  

user_1 = User(1, "Robert")

print(user_1)
         