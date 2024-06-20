from pyecore.resources import ResourceSet, URI
import xml.etree.ElementTree as ET


def parse_operand(element):
    return element.value


def parse_operator(element):
    rodzaj = element.kind
    if rodzaj == 'Dodawanie':
        return '+'
    elif rodzaj == 'Odejmowanie':
        return '-'
    elif rodzaj == 'Mnożenie':
        return '\\cdot'
    elif rodzaj == 'Dzielenie':
        return '\\frac'
    elif rodzaj == 'Równy':
        return '='
    elif rodzaj == 'Nierówny':
        return '\\neq'
    elif rodzaj == 'Mniejszy':
        return '<'
    elif rodzaj == 'Większy':
        return '>'
    elif rodzaj == 'MniejszyRówny':
        return '\\leq'
    elif rodzaj == 'WiększyRówny':
        return '\\geq'
    else:
        raise ValueError(f"Nieznany operator: {rodzaj}")


def parse_pietro(element):
    rodzaj = element.kind
    if rodzaj == 'Ułamek':
        numerator = element.operands[0].value
        denominator = element.operands[1].value
        return f"\\frac{{{numerator}}}{{{denominator}}}"
    elif rodzaj == 'Potęga':
        base = element.operands[0].value
        exponent = element.operands[1].value
        return f"{{{base}}}^{{{exponent}}}"
    elif rodzaj == 'Liniowe':
        operand1 = element.operands[0].value
        operator = parse_operator(element.operators)
        operand2 = element.operands[1].value
        return f"{{{operand1}}}{{{operator}}}{{{operand2}}}"
    else:
        raise ValueError(f"Nieznany typ piętra: {rodzaj}")


def parse_rownanie(rownanie):
    latex_parts = [parse_pietro(pietro) for pietro in rownanie.floors]
    return ''.join(latex_parts)

# rset = ResourceSet()
# resource = rset.get_resource(URI('rownanie_1.xmi'))
# root = resource.contents[0]
tree = ET.parse('rownanie_1.xmi')
root = tree.getroot()
for project in root:
    for model in project:
        for child in model:
            if child.
            print(child.get(), child.attrib)
# print(root)
# latex_equation = parse_rownanie(root)
# print(latex_equation)
