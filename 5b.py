with open('casanova.txt', 'r') as file:
    text=file.read()
    import re
    phone_numbers=re.findall(r'\+91\d{10}', text)
    email_addresses=re.findall(r'\b[A-Za-z0-9.-%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    print("ph no found", phone_numbers)
    print("email found", email_addresses)