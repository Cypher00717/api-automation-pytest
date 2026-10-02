def sanitize_payload(payload):
    if not isinstance(payload, dict):
        return payload

    sanitized = payload.copy()

    if "password" in sanitized:
        sanitized["password"] = "***"

    return sanitized


def sanitize_response(body):
    if not isinstance(body, dict):
        return body

    sanitized = body.copy()

    if "token" in sanitized:
        sanitized["token"] = "***"

    return sanitized