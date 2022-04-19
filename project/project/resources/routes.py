from .stock import StockApi, StockByIdApi
from .auth import SignupApi, LoginApi
from .user import UserApi, UsersApi
from .suppliers import supplierApi, supplierByIdApi

def initialize_routes(api):
    api.add_resource(StockApi, '/stock')
    api.add_resource(StockByIdApi, '/stock/<id>')

    api.add_resource(supplierApi, '/supplier')
    api.add_resource(supplierByIdApi, '/supplier/<id>')

    api.add_resource(UsersApi, '/user')
    api.add_resource(UserApi, '/user/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
