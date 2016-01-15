from enum import Enum

class Response(Enum):
#     OK = 200
#     Created = 200
#     Unauthorized = 200
#     Bad_Request = 200
#     No_Content = 200

    OK = 200
    Created = 201
    Unauthorized = 401
    Bad_Request = 400
    No_Content = 204