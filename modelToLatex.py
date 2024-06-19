from pyecore.resources import ResourceSet, URI

def parse_atom(element):
    return element.wartość


def parse_operacja(element):
    typ = element.typ
    element1 = parse_operand(element.element1)
    element2 = parse_operand(element.element2)
    if typ == 'dodawanie':
        return f"{{{element1}}}+{{{element2}}}"
    elif typ == 'odejmowanie':
        return f"{{{element1}}}-{{{element2}}}"
    elif typ == 'mnożenie':
        return f"{{{element1}}}\\cdot{{{element2}}}"
    elif typ == 'dzielenie' or typ == 'ułamek':
        return f"$\\frac{{{element1}}}{{{element2}}}$"
    elif typ == 'równy':
        return f"{{{element1}}}={{{element2}}}"
    elif typ == 'nierówny':
        return f"{{{element1}}}\\neq{{{element2}}}"
    elif typ == 'mniejszy':
        return f"{{{element1}}}<{{{element2}}}"
    elif typ == 'większy':
        return f"{{{element1}}}>{{{element2}}}"
    elif typ == 'mniejszyRówny':
        return f"{{{element1}}}\\leq{{{element2}}}"
    elif typ == 'większyRówny':
        return f"{{{element1}}}\\geq{{{element2}}}"
    elif typ == 'potęga':
        return f"{{{element1}}}^{{{element2}}}"
    elif typ == 'pierwiastek':
        if element2 == '2':
            return f"\\sqrt{{{element1}}}"
        else:
            return f"\\sqrt[{element2}]{{{element1}}}"
    else:
        raise ValueError(f"Nieznany operator: {typ}")


def parse_operand(element):
    if element.operacja == 'True':
        return parse_operacja(element)
    else:
        return parse_atom(element)


# Ładowanie pliku XMI
def load_xmi(file_path):
    rset = ResourceSet()
    resource = rset.get_resource(URI(file_path))
    root = resource.contents[0]
    return root

# Przetwarzanie równania z pliku XMI
def parse_rownanie(equation_instance):
    latex_equation = parse_operacja(equation_instance)
    return latex_equation

# Przykład użycia
file_path = 'rownanie.xmi'
equation_instance = load_xmi(file_path)
latex_equation = parse_rownanie(equation_instance)
print(latex_equation)