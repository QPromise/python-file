from xml.etree.ElementTree import Element, tostring

def dict_to_xml(rt, dt):
    elem = Element(rt)
    for key, val in dt.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return tostring(elem)

print(dict_to_xml('user', {'name' : 'Justin', 'age' : 40}))