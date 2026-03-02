import re
import datefinder

def extract_entities(text):

    result = {
        "Names": [],
        "Dates": [],
        "Amounts": [],
        "Organizations": []
    }

    # Extract Dates
    matches = datefinder.find_dates(text)

    for date in matches:
        result["Dates"].append(str(date.date()))


    # Extract Money
    money_pattern = r'\$\d+|\d+\s?USD'

    result["Amounts"] = re.findall(money_pattern, text)


    # Extract Names (Simple Pattern)
    name_pattern = r'[A-Z][a-z]+\s[A-Z][a-z]+'

    result["Names"] = re.findall(name_pattern, text)


    # Extract Organizations
    org_keywords = ["Ltd", "Pvt", "Company", "Corporation"]

    words = text.split()

    for i in range(len(words)):
        if words[i] in org_keywords:
            org = words[i-1] + " " + words[i]
            result["Organizations"].append(org)


    return result