import os

def _get_secret(secret_name: str, default: str = None) -> str:
    secret_path = f"/run/secrets/{secret_name}"
    
    if os.path.exists(secret_path):
        with open(secret_path, "r") as secret_file:
            return secret_file.read().strip()
    
    return os.getenv(secret_name.upper(), default)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "devops_db")
DB_USER = os.getenv("DB_USER", "postgres")

DB_PASSWORD = _get_secret("db_pass", "default_db_password")
