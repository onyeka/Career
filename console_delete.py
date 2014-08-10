__author__ = 'onyekaigabari'

from application.models import User
from application import db
for u in User.query.all():
  db.session.delete(u)
db.session.commit()