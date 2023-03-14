from flask import Flask
import config
from exts import db, mail, cache, csrf, avatars
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
cache.init_app(app)
csrf.init_app(app)
avatars.init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
