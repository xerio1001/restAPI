from flask import request, Response
from flask_restful import Resource
from project.database.models.user import Stock
from flask_jwt_extended import jwt_required
from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from project.resources.errors import *

class StockApi(Resource):
  @jwt_required()
  def get(self):
    stocks = Stock.objects().to_json()
    return Response(stocks, mimetype="application/json", status=200)

  @jwt_required()
  def post(self):
    try:
      body = request.get_json()
      stock = Stock(**body)
      stock.save()
      id = stock.id
      return {'id': str(id)}, 200
    except (FieldDoesNotExist, ValidationError):
      raise SchemaValidationError
    except NotUniqueError:
      raise AlreadyExistsError
    except Exception:
      raise InternalServerError
  
class StockByIdApi(Resource):
    @jwt_required()
    def put(self, id):
      try:
        stock = Stock.objects.get(id=id)
        body = request.get_json()
        stock.update(**body)
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
        stock = Stock.objects.get(id=id)
        stock.delete()
        return '', 200
      except DoesNotExist:
        raise DeletingError
      except Exception:
        raise InternalServerError
    
    @jwt_required()
    def get(self, barcode):
      try:
        stocks = Stock.objects.get(barcode=barcode).to_json()
        return Response(stocks, mimetype="application/json", status=200)
      except DoesNotExist:
        raise NotExistsError
      except Exception:
        raise InternalServerError
