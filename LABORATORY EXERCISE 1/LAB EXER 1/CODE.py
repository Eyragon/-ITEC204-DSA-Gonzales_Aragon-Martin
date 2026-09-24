# ==========================================
# IT AUTOMATION INCIDENT TICKET MANAGER
# Laboratory Exercise 1
# Linear Data Structure - List
# ==========================================


# ==========================================
# INITIAL SAMPLE INCIDENT TICKETS
# ==========================================

incident_tickets = [
    {
        "incident_id": "INC1392939",
        "bot": "BOT-Inventory",
        "description": "Failed to generate the daily report"
    },
    {
        "incident_id": "INC1392940",
        "bot": "BOT-Email",
        "description": "Failed to send the scheduled notification"
    },
    {
        "incident_id": "INC1392941",
        "bot": "BOT-DataSync",
        "description": "Encountered an error during data transfer"
    },
    {
        "incident_id": "INC1392942",
        "bot": "BOT-Invoice",
        "description": "Failed to process an invoice"
    },
    {
        "incident_id": "INC1392943",
        "bot": "BOT-Report",
        "description": "Failed to generate the weekly report"
    },
    {
        "incident_id": "INC1392944",
        "bot": "BOT-FileTransfer",
        "description": "Failed to upload the required file"
    },
    {
        "incident_id": "INC1392945",
        "bot": "BOT-DataEntry",
        "description": "Encountered an error while entering records"
    },
    {
        "incident_id": "INC1392946",
        "bot": "BOT-Backup",
        "description": "Failed to complete the scheduled backup"
    },
    {
        "incident_id": "INC1392947",
        "bot": "BOT-Validation",
        "description": "Failed to validate the submitted records"
    },
    {
        "incident_id": "INC1392948",
        "bot": "BOT-Notification",
        "description": "Faied to send the system alert"
    }
]


# ==========================================
# 1. ADD A NEW INCIDENT TICKET
# ==========================================

def add_ticket():
    print("\n--- ADD NEW INCIDENT TICKET ---")

    incident_id = input("Enter Incident ID: ")
    bot = input("Enter Bot: ")
    description = input("Enter Short Description: ")

    new_ticket = {
        "incident_id": incident_id,
        "bot": bot,
        "description": description
    }

    incident_tickets.append(new_ticket)

    print("\nIncident ticket added successfully!")


# ==========================================
# 2. DISPLAY ALL ACTIVE INCIDENT TICKETS
# ==========================================

def display_tickets():
    print("\n--- ACTIVE INCIDENT TICKETS ---")

    if len(incident_tickets) == 0:
        print("No active incident tickets.")
        return

    print("-" * 100)
    print(f"{'Incident ID':<15} {'Bot':<20} {'Short Description'}")
    print("-" * 100)

    for ticket in incident_tickets:
        print(
            f"{ticket['incident_id']:<15} "
            f"{ticket['bot']:<20} "
            f"{ticket['description']}"
        )

    print("-" * 100)


# ==========================================
# 3. SEARCH FOR A SPECIFIC INCIDENT TICKET
# ==========================================

def search_ticket():
    print("\n--- SEARCH INCIDENT TICKET ---")

    incident_id = input("Enter Incident ID to search: ")

    found = False

    for ticket in incident_tickets:
        if ticket["incident_id"].lower() == incident_id.lower():
            print("\nTicket found!")
            print("Incident ID:", ticket["incident_id"])
            print("Bot:", ticket["bot"])
            print("Short Description:", ticket["description"])

            found = True
            break

    if not found:
        print("\nIncident ticket not found.")


# ==========================================
# 4. REMOVE A RESOLVED INCIDENT TICKET
# ==========================================

def remove_ticket():
    print("\n--- REMOVE RESOLVED INCIDENT TICKET ---")

    incident_id = input("Enter Incident ID to remove: ")

    for ticket in incident_tickets:
        if ticket["incident_id"].lower() == incident_id.lower():
            incident_tickets.remove(ticket)

            print("\nIncident ticket removed successfully!")
            return

    print("\nIncident ticket not found.")


# ==========================================
# 5. COUNT ACTIVE INCIDENT TICKETS
# ==========================================

def count_tickets():
    print("\n--- COUNT ACTIVE INCIDENT TICKETS ---")

    total = len(incident_tickets)

    print("Total active incident tickets:", total)


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n==========================================")
        print(" IT AUTOMATION INCIDENT TICKET MANAGER")
        print("==========================================")

        print("1. Add a new incident ticket")
        print("2. Display all active incident tickets")
        print("3. Search for an incident ticket")
        print("4. Remove a resolved incident ticket")
        print("5. Display total active incident tickets")
        print("6. Exit")

        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_ticket()

        elif choice == "2":
            display_tickets()

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            remove_ticket()

        elif choice == "5":
            count_tickets()

        elif choice == "6":
            print("\nThank you for using the Incident Ticket Manager!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ==========================================
# RUN PROGRAM
# ==========================================

if __name__ == "__main__":
    main()