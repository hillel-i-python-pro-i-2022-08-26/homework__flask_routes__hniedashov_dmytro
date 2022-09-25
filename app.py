from application import create_app
import os

env = os.getenv("ENVIRONMENT", "dev")
app = create_app(env)

if __name__ == "__main__":
    app.run(debug=env == "dev")
