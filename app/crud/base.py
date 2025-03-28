from app.db import db


def db_add(object):
    db.session.add(object)
    db.session.commit()
    return object


def db_delete(object):
    db.session.delete(object)
    db.session.commit()


def db_bulk_add(objects: list):
    db.session.bulk_save_objects(objects)
    db.session.commit()
