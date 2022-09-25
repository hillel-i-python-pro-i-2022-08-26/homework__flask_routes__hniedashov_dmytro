from application.main import create_app
from application import api_blueprint
import os

env = os.getenv("ENVIRONMENT", "dev")
app = create_app(env)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=env == "dev")
