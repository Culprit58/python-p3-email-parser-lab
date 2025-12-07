import re

class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        # Regular expression for valid email
        # - Starts with letters or numbers
        # - Optional dots or underscores
        # - @
        # - Domain letters/numbers
        # - .TLD letters
        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+"

        # Find all matches
        emails = re.findall(email_pattern, self.text)

        # Return sorted list
        return sorted(emails)
