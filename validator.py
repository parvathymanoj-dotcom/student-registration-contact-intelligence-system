def validate_name(name):
    if name.strip() == "":
        return False, "Name is missing"
    return True, "Valid"


def validate_phone(phone):
    phone = phone.strip()

    if len(phone) != 10:
        return False, "Phone number must contain 10 digits"

    if not phone.isdigit():
        return False, "Phone number must contain only digits"

    if not phone.startswith(("6", "7", "8", "9")):
        return False, "Phone number must start with 6, 7, 8 or 9"

    return True, "Valid"


def validate_email(email):
    email = email.strip()

    if " " in email:
        return False, "Email must not contain spaces"

    if email.count("@") != 1:
        return False, "Email must contain exactly one @ symbol"

    local, domain = email.split("@")

    if local == "":
        return False, "Email username is missing"

    if "." not in domain:
        return False, "Email domain must contain a dot"

    if domain.startswith(".") or domain.endswith("."):
        return False, "Invalid email domain"

    return True, "Valid"


def validate_contact(name, phone, email):
    valid, reason = validate_name(name)
    if not valid:
        return False, reason

    valid, reason = validate_phone(phone)
    if not valid:
        return False, reason

    valid, reason = validate_email(email)
    if not valid:
        return False, reason

    return True, "Valid contact"