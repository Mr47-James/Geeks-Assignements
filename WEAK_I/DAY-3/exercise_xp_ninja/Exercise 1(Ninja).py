class Phone:
    def __init__(self, phone_number, call_history, messages):
        self.pn = phone_number
        self.call_history = []
        self.messages = []
    def call(self, other_phone):
        print(f"[*] Caller ID: {other_phone}")
        self.call_history.append(other_phone)
    def show_call_history(self):
        print(f"[*] Printing Call-History:\n{', '.join(self.call_history)}")
    def send_message(self):
        XMT = input("[+] Put in your Message Destinator ID: ")
        XMF = input("[+] Put in your ID: ")
        XMC = input("[+} Put in your Message: ")
        self.messages = list(self.XMH.keys())
        Last_Message = self.messages[-1]
        for i in Last_Message:
            if i.isdigit():
                num += i
        if num:
            Prefix = int(num)
            Prefix += 1
            key = f"Message{num}"
        XMH[key]["to"] = XMT 
        XMH[key]["from"] = XMF
        XMH[key]["content"] = XMC
        return XMH
    def show_outgoing_messages(self):
        print(f"[*] Printing Outgoing Messages:\n{'\n'.join(self.messages[-1])}")
    #def show_incoming_messages(self):
Mode = intput(f"1. Call\n2. Call-History\n3. Send-Message\n4. Outgoing-Messages\n[?] Choose you mode: ")
match Mode
    case "1":
        DID = input("[?] Your Destination Id:")
        
        
        
            
            
