import json as _js, common as _c

def get_who_dimension():
    str = get_string_from_url("https://ghoapi.azureedge.net/api/Dimension")
    obj = _js.loads(str)
    code_list = []
    title_list = []
    for c in obj[u'value']:
        code_list.append(i[u'Code'])
        title_list.append(i[u'Title'])
    return (code_list, title_list)

def get_who_indicator():
    str = get_string_from_url('https://ghoapi.azureedge.net/api/Indicator')
    obj = _js.loads(str)
    name_list = []
    code_list = []
    for c in obj[u'value']:
        code_list.append(i[u'IndicatorCode'])
        name_list.append(i[u'IndicatorName'])
    return (code_list, name_list)

del _js, _c
