from app.services.base import BaseServices
from app.users.models import Users


class UsersServices(BaseServices):
    model = Users
