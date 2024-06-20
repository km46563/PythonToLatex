from transformers import transformers


class Operand:
    def __init__(self, input_value, data_tree):
        self.data_tree = data_tree
        self.input_value = input_value
        self.name = None
        self.value = None
        self.nawias = None
        self.typ = None
        self.element1 = None
        self.element2 = None
        self.output = None

    def update_params(self):
        if "name" in self.input_value.keys():
            self.name = self.input_value["name"]

        if "wartość" in self.input_value["params"].keys():
            self.value = self.input_value["params"]["wartość"]

        if "typ" in self.input_value["params"].keys():
            self.typ = self.input_value["params"]["typ"]

        if "nawias" in self.input_value["params"].keys():
            self.nawias = self.input_value["params"]["nawias"]

        if "element1" in self.input_value["params"].keys():
            operand_input = self.data_tree.pop(self.input_value["params"]["element1"])
            self.element1 = Operand(operand_input, self.data_tree)
            self.element1.update_params()

        if "element2" in self.input_value["params"].keys():
            operand_input = self.data_tree.pop(self.input_value["params"]["element2"])
            self.element2 = Operand(operand_input, self.data_tree)
            self.element2.update_params()

        self.write_output()

    def write_output(self):
        if self.value:
            self.output = f"{self.value}"
        elif "Operacja" in self.name:
            if self.typ == 'dodawanie':
                self.output = f'{self.element1.output} + {self.element2.output}'
            elif self.typ == 'odejmowanie':
                self.output = f'{self.element1.output} - {self.element2.output}'
            elif self.typ == 'mnożenie':
                self.output = f'{self.element1.output} \\cdot {self.element2.output}'
            elif self.typ == 'dzielenie':
                self.output = f'{self.element1.output} : {self.element2.output}'
            elif self.typ == 'równy':
                self.output = f'{self.element1.output} = {self.element2.output}'
            elif self.typ == 'nierówny':
                self.output = f'{self.element1.output} \\neq {self.element2.output}'
            elif self.typ == 'mniejszy':
                self.output = f'{self.element1.output} < {self.element2.output}'
            elif self.typ == 'większy':
                self.output = f'{self.element1.output} > {self.element2.output}'
            elif self.typ == 'potęga':
                self.output = f'{self.element1.output}^{self.element2.output}'
            elif self.typ == 'pierwiastek':
                self.output = f'\\sqrt[{self.element1.output}]{{{self.element2.output}}}'
            elif self.typ == 'ułamek':
                self.output = f"\\frac{{{self.element1.output}}}{{{self.element2.output}}}"
            elif self.typ == 'mniejszyRówny':
                self.output = f'{self.element1.output} \\leq {self.element2.output}'
            elif self.typ == 'większyRówny':
                self.output = f'{self.element1.output} \\geq {self.element2.output}'
            else:
                raise ValueError(f"Nieznany operator: {self.typ}")

        if self.nawias == "True":
            self.output = f"\\left({self.output}\\right)"


if __name__ == "__main__":
    OptimusPrime = transformers("rownanie_2.xmi")
    for key in OptimusPrime.keys():
        if OptimusPrime[key]["name"]=="Operacja_1":
            values = OptimusPrime.pop(key)
            root = Operand(values, OptimusPrime)
            root.update_params()
            print(root.output)

