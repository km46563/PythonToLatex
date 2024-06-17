import xml.etree.ElementTree as ET


def parse_operand(element):
    return element.text


def parse_operator(element):
    rodzaj = element.attrib['rodzaj']
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
    rodzaj = element.attrib['rodzaj']
    if rodzaj == 'Ułamek':
        numerator = element.find('operand').text
        denominator = element.find('operand[2]').text
        return f"\\frac{{{numerator}}}{{{denominator}}}"
    elif rodzaj == 'Potęga':
        base = element.find('operand').text
        exponent = element.find('operand[2]').text
        return f"{{{base}}}^{{{exponent}}}"
    elif rodzaj == 'Liniowe':
        operand1 = element.find('operand').text
        operator = parse_operator(element.find('operator'))
        operand2 = element.find('operand[2]').text
        return f"{{{operand1}}}{{{operator}}}{{{operand2}}}"
    else:
        raise ValueError(f"Nieznany typ piętra: {rodzaj}")


def parse_rownanie(xml_string):
    root = ET.fromstring(xml_string)
    if root.tag != 'rownanie':
        raise ValueError("Korzeniem musi być element 'rownanie'!")

    latex_parts = [parse_pietro(child) for child in root]
    return ''.join(latex_parts)


xml_string = """
<rownanie>
    <pietro rodzaj="Ułamek">
        <operand>1</operand>
        <operator rodzaj="Dzielenie"/>
        <operand>2</operand>
    </pietro>
    <pietro rodzaj="Liniowe">
        <operand>x</operand>
        <operator rodzaj="Dodawanie"/>
        <operand>y</operand>
    </pietro>
</rownanie>
"""

latex_equation = parse_rownanie(xml_string)
print(latex_equation)
