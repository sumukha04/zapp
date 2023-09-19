import re
def validate_pan(pan_number):
    return bool(re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan_number))
pan1 = "ABCDE1234F"
print(f"Is {pan1} a valid PAN number? {validate_pan(pan1)}")