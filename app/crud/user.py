from app.crud.base_impl import CRUDBase
from app.models.user import User
from app.schemas.user import CreateUser, UpdateUser


class CRUDUser(CRUDBase[User, CreateUser, UpdateUser]):
    ...


user = CRUDUser(User)
