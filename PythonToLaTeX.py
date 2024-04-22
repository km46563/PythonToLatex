import antlr4
import sys

from PythonToLaTeXLexer import PythonToLaTeXLexer
from PythonToLaTeXParser import PythonToLaTeXParser


class PythonToLaTeXVisitor(antlr4.ParseTreeVisitor):
    def visitStart(self, ctx:PythonToLaTeXParser.StartContext):
        return self.visitStat(ctx.stat())

    def visitStat(self, ctx:PythonToLaTeXParser.StatContext):
        if hasattr(ctx, 'op'):
            print("numerator laduje do visitStat")
            numerator = self.visitStat(ctx.numerator())
            print("denominator laduje do visitStat")
            denominator = self.visitStat(ctx.denominator())
            print("pobieram operator")
            operator = str(ctx.op.text)
            print("operator: ", operator)
            if operator == "//":
                print("koniec jako ułamek")
                return f"\\frac'{{{numerator}}}{{{denominator}}}"
            elif operator == "^":
                print("koniec jako potęga")
                return f"{numerator}^{denominator}"
            else:
                return ValueError("Unknown operation")

        else:
            print(dir(ctx))
            return self.visitExpression(ctx.expression())

    def visitExpression(self, ctx:PythonToLaTeXParser.ExpressionContext):
        if hasattr(ctx, 'op'):
            left = self.visitExpression(ctx.l)
            right = self.visitExpression(ctx.r)
            operator = str(ctx.op.text)
            print(f"{left}{operator}{right}")
        else:
            print(self.visitFactor(ctx.factor()))

    # def visitTerm(self, ctx: PythonToLaTeXParser.TermContext):
    #     if hasattr(ctx, 'op'):
    #         left = self.visitTerm(ctx.l)
    #         right = self.visitFactor(ctx.l)
    #         operator = ctx.op.text
    #         return f"{left} {operator} {right}"
    #     else:
    #         return self.visitFactor(ctx.factor())

    def visitFactor(self, ctx: PythonToLaTeXParser.FactorContext):
        if hasattr(ctx, 'INT'):
            return ctx.INT().getText()
        elif hasattr(ctx, 'ID'):
            return ctx.ID().getText()
        elif ctx.stat():
            return f"({self.visitStat(ctx.expression())})"
        else:
            raise ValueError("Unknown factor context")

def convert_to_latex(expression):
    lexer = PythonToLaTeXLexer(antlr4.InputStream(expression))
    stream = antlr4.CommonTokenStream(lexer)
    parser = PythonToLaTeXParser(stream)
    tree = parser.start()
    visitor = PythonToLaTeXVisitor()
    return visitor.visitStart(tree)


expression = "[2 + 2 - 3] //[3]"
latex = convert_to_latex(expression)
print(latex)
