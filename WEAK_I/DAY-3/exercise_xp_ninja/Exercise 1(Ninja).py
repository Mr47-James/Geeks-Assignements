class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        log = f"{self.phone_number} called {other_phone.phone_number}"
        print(log)
        self.call_history.append(log)

    def show_call_history(self):
        print("[*] Call History:")
        if not self.call_history:
            print("   (empty)")
        for call in self.call_history:
            print("  ", call)

    def send_message(self, to_phone, content):
        message = {
            "to": to_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        to_phone.messages.append(message)

    def show_outgoing_messages(self):
        print("[*] Outgoing Messages:")
        found = False
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(msg)
                found = True
        if not found:
            print("   (none)")

    def show_incoming_messages(self):
        print("[*] Incoming Messages:")
        found = False
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(msg)
                found = True
        if not found:
            print("   (none)")

    def show_messages_from(self, other_number):
        print(f"[*] Messages from {other_number}:")
        found = False
        for msg in self.messages:
            if msg["from"] == other_number and msg["to"] == self.phone_number:
                print(msg)
                found = True
        if not found:
            print("   (none)")


p1 = Phone("111-111")
p2 = Phone("222-222")
p3 = Phone("333-333")

while True:
    print("\n--- PHONE MENU ---")
    print("1. Make a Call")
    print("2. Show Call History")
    print("3. Send Message")
    print("4. Show Outgoing Messages")
    print("5. Show Incoming Messages")
    print("6. Show Messages From Specific Number")
    print("0. Exit")
    mode = input("[?] Choose your mode: ")

    match mode:
        case "1":
            dest = input("[?] Enter destination (222-222 or 333-333): ")
            if dest == p2.phone_number:
                p1.call(p2)
            elif dest == p3.phone_number:
                p1.call(p3)
            else:
                print("[!] Unknown destination.")
        case "2":
            p1.show_call_history()
        case "3":
            dest = input("[?] Enter destination (222-222 or 333-333): ")
            msg = input("[+] Enter your message: ")
            if dest == p2.phone_number:
                p1.send_message(p2, msg)
            elif dest == p3.phone_number:
                p1.send_message(p3, msg)
            else:
                print("[!] Unknown destination.")
        case "4":
            p1.show_outgoing_messages()
        case "5":
            p1.show_incoming_messages()
        case "6":
            sender = input("[?] Enter sender number: ")
            p1.show_messages_from(sender)
        case "0":
            print("[*] Exiting... Returning '00'")
            print("00")
            break
        case _:
            print("[!] Invalid choice, try again.")
