from supabase import create_client, Client
from src.config import load_config
from src.logger import get_logger

logger = get_logger()

def get_client() -> Client:
    config = load_config()
    return create_client(config["supabase_url"], config["supabase_key"])

def get_contacts() -> list[dict]:
    try:
        client = get_client()
        response = (
            client
            .table("contacts")
            .select("name, phone")
            .eq("active", True)
            .limit(3)
            .execute()
        )
        contacts = response.data
        logger.info(f"{len(contacts)} contato(s) encontrado(s) no banco")
        return contacts

    except Exception as e:
        logger.error(f"Erro ao buscar contatos no Supabase: {e}")
        raise