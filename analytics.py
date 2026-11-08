def show_analytics(contacts, rejected, total):
    print("\n========== STUDENT ANALYTICS ==========")

    print("Total records processed:", total)
    print("Accepted records:", len(contacts))
    print("Rejected records:", len(rejected))

    if total > 0:
        rate = (len(contacts) / total) * 100
        print("Acceptance rate: {:.2f}%".format(rate))

    # Count rejection reasons
    reasons = {}

    for item in rejected:
        reason = item[3]
        reasons[reason] = reasons.get(reason, 0) + 1

    print("\nRejection Reasons:")
    for reason, count in reasons.items():
        print(reason, ":", count)

    # Phone number prefix distribution
    prefixes = {"6": 0, "7": 0, "8": 0, "9": 0}

    for contact in contacts:
        prefix = contact["phone"][0]
        prefixes[prefix] += 1

    print("\nPhone Number Prefix Distribution:")
    for prefix, count in prefixes.items():
        print(prefix, ":", count)

    # Email domain distribution
    domains = {}

    for contact in contacts:
        domain = contact["email"].split("@")[1].lower()
        domains[domain] = domains.get(domain, 0) + 1

    print("\nEmail Domain Distribution:")
    for domain, count in domains.items():
        print(domain, ":", count)

    # Simple ASCII summary
    print("\nAcceptance Summary:")
    print("Accepted :", "#" * len(contacts), len(contacts))
    print("Rejected :", "#" * len(rejected), len(rejected))