from tasks import Task
from utils import to_snake

class CreatePermissions(Task):
    type = "startup"

    def execute(*args, **kwargs):
        MODELS = kwargs.get("MODELS")
        db = kwargs.get("db")
        permission_types = ('create', 'read', 'update', 'delete')
        for model in MODELS:
            model_name = to_snake(model.__name__)
            if db.has('permission'):
                if db.has('permission', column='model', value=model_name):
                    continue

            for permission_type in permission_types:
                permission = MODELS.Permission(type=permission_type, model=model_name)
                db.add(permission)
