# encoding : utf-8

unicode2utf8 = lambda x: x.encode('utf8') if isinstance(x,unicode) else x

def unicode2str_r(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.iteritems():
            new_dict[unicode2str_r(k)] = unicode2str_r(v)
        return new_dict
    elif isinstance(obj, list):
        new_list = [unicode2str_r(i) for i in obj]
        return new_list
    elif isinstance(obj, unicode):
        return str(obj)
    else:
        return obj