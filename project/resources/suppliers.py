from flask import request, Response
from flask_restful import Resource
from project.database.models.suppliers import Supplier
from flask_jwt_extended import jwt_required
from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from project.resources.errors import *

class supplierApi(Resource):
  @jwt_required()
  def get(self):
    suppliers = Supplier.objects().to_json()
    return Response(suppliers, mimetype="application/json", status=200)

  @jwt_required()
  def post(self):
    try:
      body = request.get_json()
      supplier = Supplier(**body)
      supplier.save()
      id = supplier.id
      return {'id': str(id)}, 200
    except (FieldDoesNotExist, ValidationError):
      raise SchemaValidationError
    except NotUniqueError:
      raise AlreadyExistsError
    except Exception:
      raise InternalServerError
  
class supplierByIdApi(Resource):
    @jwt_required()
    def put(self, id):
      try:
        supplier = Supplier.objects.get(id=id)
        body = request.get_json()
        supplier.update(**body)
        return '', 200
      except InvalidQueryError:
        raise SchemaValidationError
      except DoesNotExist:
        raise UpdatingError
      except Exception:
        raise InternalServerError
  
    @jwt_required()
    def delete(self, id):
      try:
        supplier = Supplier.objects.get(id=id)
        supplier.delete()
        return '', 200
      except DoesNotExist:
        raise DeletingError
      except Exception:
        raise InternalServerError
    
    @jwt_required()
    def get(self, id):
      try:
        suppliers = Supplier.objects.get(id=id).to_json()
        return Response(suppliers, mimetype="application/json", status=200)
      except DoesNotExist:
        raise NotExistsError
      except Exception:
        raise InternalServerError
