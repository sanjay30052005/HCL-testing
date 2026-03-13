
import re

text = "2025-11-30 Report Generated"

if re.match(r"\d{4}-\d{2}-\d{2}", text):
    print("String starts with a valid date")
else:
    print("No date at start")
