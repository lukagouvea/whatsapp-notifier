import requests
from src.config import load_config
from src.logger import get_logger

logger = get_logger()

def send_message(phone: str, text: str) -> bool:
    config = load_config()

    url = (
        f"https://api.z-api.io/instances/{config['zapi_instance']}"
        f"/token/{config['zapi_token']}/send-text"
    )

    headers = {
        "Content-Type": "application/json",
        "Client-Token": config["zapi_client_token"],
    }

    payload = {
        "phone": phone,
        "message": text,
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        logger.info(f"Mensagem enviada para {phone}")
        return True

    except requests.exceptions.Timeout:
        logger.error(f"Timeout ao enviar para {phone}")
        return False

    except requests.exceptions.HTTPError as e:
        logger.error(f"Erro HTTP ao enviar para {phone}: {e.response.status_code} {e.response.text}")
        return False

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de rede ao enviar para {phone}: {e}")
        return False