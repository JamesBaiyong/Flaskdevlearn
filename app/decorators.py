<<<<<<< HEAD
from functools import warps
=======
from functools import wraps
>>>>>>> 11e_0.1
from flask import abort
from flask_login import current_user
from .models import Permission

def permission_required(permission):
	def decorator(f):
<<<<<<< HEAD
		@wraps(f):
		def decorated_function(**args,**kwargs):
=======
		@wraps(f)
		def decorated_function(*args, **kwargs):
>>>>>>> 11e_0.1
			if not current_user.can(permission):
				abort(403)
			return f(*args,**kwargs)
		return decorated_function
	return decorator

def admin_required(f):
<<<<<<< HEAD
	return permission_required(Permission,ADMINSITRATOR)(f)
=======
	return permission_required(Permission.ADMINISTER)(f)
>>>>>>> 11e_0.1


