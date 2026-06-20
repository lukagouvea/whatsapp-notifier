from src.config import load_config
from src.logger import get_logger
from src.database import get_contacts
from src.zapi_client import send_message

logger = get_logger()

def main():
    logger.info("Iniciando whatsapp-notifier...")

    try:
        load_config()
    except ValueError as e:
        logger.error(f"Erro de configuração: {e}")
        return

    try:
        contacts = get_contacts()
    except Exception:
        logger.error("Não foi possível buscar contatos. Encerrando.")
        return

    if not contacts:
        logger.info("Nenhum contato ativo encontrado. Encerrando.")
        return

    sucessos = 0
    for contact in contacts:
        name = contact["name"]
        phone = contact["phone"]
        message = f"Olá, {name} tudo bem com você?"

        ok = send_message(phone, message)
        if ok:
            sucessos += 1
        else:
            logger.error(f"Falha ao enviar para {name} ({phone})")

    logger.info(f"Sumário: {sucessos}/{len(contacts)} mensagens enviadas com sucesso")


if __name__ == "__main__":
    main()