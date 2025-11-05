from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Liest automatisch aus Environment-Variablen (oder .env)
    db_url: str
    debug_mode: bool = False

# App lädt Settings *nur* aus der Umgebung
settings = Settings()
db = connect(settings.db_url)