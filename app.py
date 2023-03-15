from flask import Flask
import config
from exts import db, mail, cache, avatars
from flask_migrate import Migrate
from models import admin, errorInfo, garbage, search, user, game
from routes.admin.front import admin_bp
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
cache.init_app(app)
avatars.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(admin_bp)

CORS(app, resources=r'/*')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
