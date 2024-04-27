import antlr4
import sys

from PythonToLaTeXLexer import PythonToLaTeXLexer
from PythonToLaTeXParser import PythonToLaTeXParser
from PythonToLaTeXListener import PythonToLaTeXListener


# class PythonToLaTeXVisitor(antlr4.ParseTreeVisitor):
    # def visitStart(self, ctx:PythonToLaTeXParser.StartContext):
    #     print(self.visitTest_1(ctx.getChild(0)))
    # def visitTest_1(self, ctx:PythonToLaTeXParser.Test_1Context):
    #     print(ctx.getText())
    # def factor

    # def visitStat(self, ctx:PythonToLaTeXParser.StatContext):
    #     if ctx.getChildCount() == 3:
    #         print("dupa 3")
    #     if ctx.getChildCount() == 2:
    #         print("dupa 3")
    #     if ctx.getChildCount() == 1:
    #         print("dupa 3")
    #     if ctx.getChildCount() == 0:
    #         print("dupa 3")
            ######
        # if hasattr(ctx, 'op'):
        #     print("numerator laduje do visitStat")
        #     numerator = self.visitStat(ctx.numerator())
        #     print("denominator laduje do visitStat")
        #     denominator = self.visitStat(ctx.denominator())
        #     print("pobieram operator")
        #     operator = str(ctx.op.text)
        #     print("operator: ", operator)
        #     if operator == "//":
        #         print("koniec jako ułamek")
        #         return f"\\frac'{{{numerator}}}{{{denominator}}}"
        #     elif operator == "^":
        #         print("koniec jako potęga")
        #         return f"{numerator}^{denominator}"
        #     else:
        #         return ValueError("Unknown operation")

        # else:
        #     print(dir(ctx))
        #     return self.visitExpression(ctx.expression())

    # def visitExpression(self, ctx:PythonToLaTeXParser.ExpressionContext):
    #     if hasattr(ctx, 'op'):
    #         left = self.visitExpression(ctx.l)
    #         right = self.visitExpression(ctx.r)
    #         operator = str(ctx.op.text)
    #         print(f"{left}{operator}{right}")
    #     else:
    #         print(self.visitFactor(ctx.factor()))

    # def visitTerm(self, ctx: PythonToLaTeXParser.TermContext):
    #     if hasattr(ctx, 'op'):
    #         left = self.visitTerm(ctx.l)
    #         right = self.visitFactor(ctx.l)
    #         operator = ctx.op.text
    #         return f"{left} {operator} {right}"
    #     else:
    #         return self.visitFactor(ctx.factor())

    # def visitFactor(self, ctx: PythonToLaTeXParser.FactorContext):
    #     if hasattr(ctx, 'INT'):
    #         return ctx.INT().getText()
    #     elif hasattr(ctx, 'ID'):
    #         return ctx.ID().getText()
    #     elif ctx.stat():
    #         return f"({self.visitStat(ctx.expression())})"
    #     else:
    #         raise ValueError("Unknown factor context")
class MyListener(PythonToLaTeXListener):
    def enterEquationFloor(self, ctx):
        numerator = ctx.numerator.getText()
        denominator = ctx.denominator.getText()
        op = ctx.op.text
        print(f"Numerator: {numerator}, Denominator: {denominator}, Operation: {op}")
    def enterExprStatic(self, ctx):
        print("Static Expression:", ctx.getText())

    def enterAddOp(self, ctx):
        print("Addition Operation:", ctx.getText())

    def enterSubOp(self, ctx):
        print("Subtraction Operation:", ctx.getText())

    def enterDivOp(self, ctx):
        print("Division Operation:", ctx.getText())

    def enterMulOp(self, ctx):
        print("Multiplication Operation:", ctx.getText())

    def enterPowOp(self, ctx):
        print("Power Operation:", ctx.getText())

def convert_to_latex(expression):
    lexer = PythonToLaTeXLexer(antlr4.InputStream(expression))
    tokens = antlr4.CommonTokenStream(lexer)
    parser = PythonToLaTeXParser(tokens)
    parser.addParseListener(MyListener())
    parser.start()
    # tree = parser.start()
    # visitor = MyListener()
    # if parser.getNumberOfSyntaxErrors() > 0:
    #     print("syntax errors")
    # return visitor.exitStart(tree)


expression = "[2 + 3] // [4]"
convert_to_latex(expression)
# print(latex)
