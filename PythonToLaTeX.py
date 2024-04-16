import antlr4
from PythonToLaTeXLexer import PythonToLaTeXLexer
from PythonToLaTeXParser import PythonToLaTeXParser


class PythonToLaTeXVisitor(antlr4.ParseTreeVisitor):
    def visitStart(self, ctx:PythonToLaTeXParser.StartContext):
        return self.visitExpression(ctx.expression())

    def visitExpression(self, ctx:PythonToLaTeXParser.ExpressionContext):
        if hasattr(ctx, 'op'):
            left = self.visitExpression(ctx.l)
            right = self.visitTerm(ctx.r)
            operator = ctx.op.text
            return f"{left} {operator} {right}"
        else:
            return self.visitTerm(ctx.term())

    def visitTerm(self, ctx: PythonToLaTeXParser.TermContext):
        if hasattr(ctx, 'op'):
            left = self.visitTerm(ctx.term())
            right = self.visitFactor(ctx.factor())
            operator = ctx.op.text
            return f"{left} {operator} {right}"
        else:
            return self.visitFactor(ctx.factor())

    def visitFactor(self, ctx: PythonToLaTeXParser.FactorContext):
        if hasattr(ctx, 'INT'):
            return ctx.INT().getText()
        elif hasattr(ctx, 'ID'):
            return ctx.ID().getText()
        elif ctx.expression():
            return f"({self.visitExpression(ctx.expression())})"
        else:
            raise ValueError("Unknown factor context")

def convert_to_latex(expression):
    lexer = PythonToLaTeXLexer(antlr4.InputStream(expression))
    stream = antlr4.CommonTokenStream(lexer)
    parser = PythonToLaTeXParser(stream)
    tree = parser.start()
    visitor = PythonToLaTeXVisitor()
    return visitor.visitStart(tree)


expression = "2 * (3 + 4) - 5 / 2"
latex = convert_to_latex(expression)
print(latex)
