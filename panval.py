import re

# Click on Edit and place your email ID to validate
email = "my.ownsite@our-earth.org"
pan = "BNZAA12N4B"
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

vaidPAn = re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]$", pan)

# Example Usage
#pan_number1 = "BNZAA1234B"
#pan_number2 = "abcde1234f"
#pan_number3 = "BNZAA1234B5"

print("Valid email address." if valid else "Invalid email address.")
print("Valid pan no." if vaidPAn else "Invalid pan no.")
