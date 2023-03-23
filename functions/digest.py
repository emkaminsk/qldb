from amazon.ion.simpleion import dumps, loads

def value_holder_to_string(value_holder):
    """
    Returns the string representation of a given `value_holder`.
    :type value_holder: dict
    :param value_holder: The `value_holder` to convert to string.
    :rtype: str
    :return: The string representation of the supplied `value_holder`.
    """
    ret_val = dumps(loads(value_holder), binary=False, indent='  ', omit_version_marker=True)
    val = '{{ IonText: {}}}'.format(ret_val)
    return val

def digest_response_to_string(digest_response):
    """
    Returns the string representation of a given `digest_response`.
    :type digest_response: dict
    :param digest_response: The `digest_response` to convert to string.
    :rtype: str
    :return: The string representation of the supplied `digest_response`.
    """
    string = ''
    if digest_response.get('Digest') is not None:
        string += 'Digest: ' + str(digest_response['Digest']) + ', '

    if digest_response.get('DigestTipAddress', {}).get('IonText') is not None:
        string += 'DigestTipAddress: ' + value_holder_to_string(digest_response['DigestTipAddress']['IonText'])

    return '{' + string + '}'