import re


def validate_dob(dob):
    dob_pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if re.match(dob_pattern, dob):
        return True
    else:
        return False


def validate_player_tournament(id_list, input_id):
    try:
        for id in input_id:
            int(id)
            check_id = [id for id in input_id if int(id) not in id_list]
        if check_id:
            return False, "Please enter existing ids"
        if len(list(set(check_id))) != len(check_id):
            return False, "please do not duplicate ids"
        if len(list(set(input_id))) != len(input_id):
            return False, "please do not duplicate ids"
        return True, 0
    except:
        return False, "Please enter number"
    

    
def int_input(inputs):
    try :
        if inputs == "back":
            return True
        int(inputs)
        return True
    except:
        return False