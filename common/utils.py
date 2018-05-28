def get_signed_number(number):
    if number >= 0:
        s = '+%s' % number
    else:
        s = '-%s' % abs(number)
    return {'s': s}
