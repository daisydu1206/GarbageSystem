from functools import wraps
from flask import g, redirect, url_for

def login_required(func):
    @wraps(func)

    def inner(*args, **kwargs):
        print(g.admin)
        if g.admin:
            print("true")
            return func(*args, **kwargs)
        else:
            print("false")
            return redirect(url_for("front.login"))
    return inner

