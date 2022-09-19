from app.crud.user import user
from app.schemas.user import CreateUser, UpdateUser
from app.services.base_impl import BaseService


class UserService(BaseService[CreateUser, UpdateUser]):
    ...


user_service = UserService(queries=user)
