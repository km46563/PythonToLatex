import xml.etree.ElementTree as ET


def transformers(file_path: str):

    file_path = "rownanie_1.xmi"
    tree = ET.parse(file_path)
    root = tree.getroot()

    structure_dict = {}

    namespaces = {
        "Miasi_profile": "http:///schemas/Miasi_profile/0",
        "ecore": "http://www.eclipse.org/emf/2002/Ecore",
        "uml": "http://www.eclipse.org/uml2/2.0.0/UML",
        "xmi": "http://schema.omg.org/spec/XMI/2.1",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }

    packaged_element_tag = "uml:packagedElement"

    packaged_elements = root.findall(".//{*}packagedElement")

    for elem in packaged_elements:
        element_id = elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
        element_name = elem.get("name")
        element_type = elem.get("{http://schema.omg.org/spec/XMI/2.1}type")

        if element_name and element_name not in structure_dict:
            structure_dict[str(element_name)] = {"id": element_id, "params": {}}
        for attribute in elem.findall(".//*", namespaces):
            attribute_name = attribute.get("name")
            attribute_id = attribute.get("{http://schema.omg.org/spec/XMI/2.1}id")
            attribute_type = attribute.get("type")

            if (
                attribute_name or attribute_id or attribute_type
            ) and attribute_name in [
                "element1",
                "element2",
                "nawias",
                "typ",
                "wartość",
            ]:
                structure_dict[str(element_name)]["params"][
                    attribute_name
                ] = attribute_type
                for attribute_operation in attribute:
                    at_val = attribute_operation.get("value")
                    if at_val:
                        structure_dict[str(element_name)]["params"][
                            attribute_name
                        ] = at_val

    return structure_dict


if __name__ == "__main__":
    print(transformers("rownanie_1.xmi"))
