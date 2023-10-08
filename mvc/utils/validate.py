import re

def validate_dob(dob):
    dob_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    if re.match(dob_pattern, dob):
        return True
    else:
        return False