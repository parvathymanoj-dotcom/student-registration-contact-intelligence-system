import os
import csv
from loader import load_contacts, save_clean_contacts
from analytics import show_analytics


# Load existing student records
contacts, rejected, total = load_contacts("contacts.csv", save_output=False)

if os.path.exists("students_clean.csv"):
    with open("students_clean.csv", "r", newline="", encoding="utf-8") as file:
        contacts = list(csv.DictReader(file))


def view_contacts():
    print("\n========== ALL STUDENT CONTACTS ==========")

    if not contacts:
        print("No student records found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print("\nStudent ID:", i)
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


def search_contact():
    print("\n1. Search by Name")
    print("2. Search by Phone")
    print("3. Search by Email")

    choice = input("Enter your choice: ").strip()
    keyword = input("Enter search value: ").strip().lower()

    found = False

    for contact in contacts:
        if choice == "1" and keyword in contact["name"].lower():
            found = True
        elif choice == "2" and keyword == contact["phone"]:
            found = True
        elif choice == "3" and keyword == contact["email"].lower():
            found = True
        else:
            continue

        print("\nName:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])

    if not found:
        print("No matching contact found.")


def register_contact():
    print("\n========== REGISTER NEW STUDENT ==========")

    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    from validator import validate_contact

    valid, reason = validate_contact(name, phone, email)

    if not valid:
        print("Registration failed:", reason)
        return

    for contact in contacts:
        if contact["phone"] == phone:
            print("Registration failed: Duplicate phone number.")
            return

        if contact["email"].lower() == email.lower():
            print("Registration failed: Duplicate email.")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_clean_contacts(contacts, "students_clean.csv")
    print("Student registered successfully!")


def update_contact():
    print("\n========== UPDATE STUDENT ==========")

    phone = input("Enter the phone number of the student: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:

            print("Current name:", contact["name"])
            new_name = input("Enter new name: ").strip()

            print("Current phone:", contact["phone"])
            new_phone = input("Enter new phone: ").strip()

            print("Current email:", contact["email"])
            new_email = input("Enter new email: ").strip()

            from validator import validate_contact

            valid, reason = validate_contact(
                new_name, new_phone, new_email
            )

            if not valid:
                print("Update failed:", reason)
                return

            for other in contacts:
                if other is not contact:
                    if other["phone"] == new_phone:
                        print("Update failed: Duplicate phone.")
                        return

                    if other["email"].lower() == new_email.lower():
                        print("Update failed: Duplicate email.")
                        return

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email

            save_clean_contacts(contacts, "students_clean.csv")
            print("Student details updated successfully!")
            return

    print("Student not found.")


def delete_contact():
    print("\n========== DELETE STUDENT ==========")

    phone = input("Enter phone number to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_clean_contacts(contacts, "students_clean.csv")
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main_menu():
    while True:
        print("\n========================================")
        print(" STUDENT REGISTRATION AND CONTACT SYSTEM")
        print("========================================")
        print("1. View all students")
        print("2. Search student")
        print("3. Register new student")
        print("4. Update student details")
        print("5. Delete student")
        print("6. View analytics")
        print("7. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_contacts()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            register_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            show_analytics(contacts, rejected, total)

        elif choice == "7":
            save_clean_contacts(contacts, "students_clean.csv")
            print("Data saved successfully.")
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()