import re

phone_number_finder = re.compile(r"\d{3}-\d{3}-\d{4}")

tests = [
    "555-555-5555",
    "My phone number is 123-456-7890, but only on Thursdays.",
    "I'm not giving you my phone number.",
]

for test in tests:
    match = phone_number_finder.search(test)
    if match:
        print(f"Found phone number: {match.group()!r}")
    else:
        print(f"No phone number found in {test!r}")
