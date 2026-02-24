from models import Task


def to_dict(obj: object):
    return obj.__dict__


def to_object(dt: dict):
    return Task(name=dt["name"], description=dt["description"], status=dt["status"], id=dt["id"], createdAt=dt["createdAt"], updatedAt=dt["updatedAt"])