from flask_restful import HTTPException

class InternalServerError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class AlreadyExistsError(HTTPException):
    pass


class UpdatingError(HTTPException):
    pass


class DeletingError(HTTPException):
    pass


class NotExistsError(HTTPException):
    pass


class EmailAlreadyExistsError(HTTPException):
    pass


class UnauthorizedError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "AlreadyExistsError": {
         "message": "Given name already exists",
         "status": 400
     },
     "UpdatingError": {
         "message": "Updating by other user is forbidden",
         "status": 403
     },
     "DeletingError": {
         "message": "Deleting by other user is forbidden",
         "status": 403
     },
     "NotExistsError": {
         "message": "Given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}
