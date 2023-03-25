from dotenv import load_dotenv
import os

load_dotenv()

env_name = os.getenv("ENV_NAME", "local")
app_host = os.getenv("APP_HOST", "0.0.0.0")
app_port = os.getenv("APP_PORT", 8000)
app_port1 = os.getenv("APP_PORT1", 8001)
db_url = os.getenv("DB_URL", "")
base_url = os.getenv("BASE_URL", "")


postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
postgres_port = os.getenv("POSTGRES_PORT")
postgres_host = os.getenv("POSTGRES_HOST")
postgres_url = f"postgresql+asyncpg://{postgres_user}:{postgres_password}@db:{postgres_port}\
/{postgres_db}"

parse_url = os.getenv("PARSE_URL")
