full_dot = '●'
empty_dot = '○'

def create_character(name, strn, intel, charisma):
    print(name)
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    print(not isinstance(strn, int))
    print(not isinstance(intel, int))
    print(not isinstance(charisma, int))
    if (not isinstance(strn, int)) or (not isinstance(intel, int)) or (not isinstance(charisma, int)):
        print('why not')
        return 'All stats should be integers'
    if (strn < 1) or intel < 1 or charisma < 1 :
        return 'All stats should be no less than 1'
    if strn > 4 or intel > 4 or charisma > 4 :
        return 'All stats should be no more than 4'
    stats_sum = strn + intel + charisma
    if stats_sum != 7 :
        return 'The character should start with 7 points'

    result = f"{name}\nSTR {full_dot*strn}{empty_dot*(10-strn)}\nINT {full_dot*intel}{empty_dot*(10-intel)}\nCHA {full_dot*charisma}{empty_dot*(10-charisma)}"
    return result

create_character('ren', 4, 2, 1)