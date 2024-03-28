import antlr4
from PythonToLaTeXLexer import PythonToLaTeXLexer
from PythonToLaTeXParser import PythonToLaTeXParser


class PythonToLaTeXVisitor(antlr4.ParseTreeVisitor):
    def visitStart(self, ctx):
        return self.visit(ctx.expression())

    def visitAdd_expression(self, ctx):
        latex = self.visit(ctx.mul_expression(0))
        for i in range(1, len(ctx.mul_expression())):
            if ctx.getChild(i).getText() == "+":
                latex += "+" + self.visit(ctx.mul_expression(i))
            else:
                latex += "-" + self.visit(ctx.mul_expression(i))
        return latex

    def visitMul_expression(self, ctx):
        latex = self.visit(ctx.atom_expression(0))
        for i in range(1, len(ctx.atom_expression())):
            if ctx.getChild(i).getText() == "*":
                latex += "\\cdot" + self.visit(ctx.atom_expression(i))
            else:
                latex += (
                    "\\frac{" + latex + "}{" + self.visit(ctx.atom_expression(i)) + "}"
                )
        return latex

    def visitAtom_expression(self, ctx):
        if ctx.getChild(0).getText() == "(":
            return "(" + self.visit(ctx.expression()) + ")"
        else:
            return ctx.getText()


def convert_to_latex(expression):
    lexer = PythonToLaTeXLexer(antlr4.InputStream(expression))
    stream = antlr4.CommonTokenStream(lexer)
    parser = PythonToLaTeXParser(stream)
    tree = parser.start()
    visitor = PythonToLaTeXVisitor()
    return visitor.visit(tree)


#expression = "2 + 2"
#latex = convert_to_latex(expression)
#print(latex)
