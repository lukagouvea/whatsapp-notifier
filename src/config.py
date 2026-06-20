import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_VARS = [
    "SUPABASE_URL",
    "SUPABASE_KEY",
    "ZAPI_INSTANCE",
    "ZAPI_TOKEN",
    "ZAPI_CLIENT_TOKEN",
]

def load_config() -> dict:
    missing = [var for var in REQUIRED_VARS if not os.getenv(var)]
    if missing:
        raise ValueError(f"Variáveis de ambiente ausentes: {', '.join(missing)}")

    return {
        "supabase_url":       os.getenv("SUPABASE_URL"),
        "supabase_key":       os.getenv("SUPABASE_KEY"),
        "zapi_instance":      os.getenv("ZAPI_INSTANCE"),
        "zapi_token":         os.getenv("ZAPI_TOKEN"),
        "zapi_client_token":  os.getenv("ZAPI_CLIENT_TOKEN"),
    }