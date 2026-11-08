import csv
from validator import validate_contact


def load_contacts(filename, save_output=True):
    contacts = []
    rejected = []
    phone_set = set()
    email_set = set()
    total = 0

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1

            name = row["name"].strip()
            phone = row["phone"].strip()
            email = row["email"].strip()

            valid, reason = validate_contact(name, phone, email)

            if not valid:
                rejected.append((name, phone, email, reason))
                continue

            if phone in phone_set:
                rejected.append((name, phone, email, "Duplicate phone number"))
                continue

            if email.lower() in email_set:
                rejected.append((name, phone, email, "Duplicate email"))
                continue

            phone_set.add(phone)
            email_set.add(email.lower())

            contacts.append({
                "name": name,
                "phone": phone,
                "email": email
            })

    if save_output:
        save_clean_contacts(contacts, "students_clean.csv")
    print("\n========== LOADING REPORT ==========")
    print("Total records:", total)
    print("Accepted records:", len(contacts))
    print("Rejected records:", len(rejected))

    print("\nRejection Details:")
    for item in rejected:
        print(item[0], "-", item[3])

    return contacts, rejected, total


def save_clean_contacts(contacts, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(contacts)