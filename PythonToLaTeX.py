import antlr4
from PythonToLaTeXLexer import PythonToLaTeXLexer
from PythonToLaTeXParser import PythonToLaTeXParser


class PythonToLaTeXVisitor(antlr4.ParseTreeVisitor):
    def visitStart(self, ctx:PythonToLaTeXParser.StartContext):
        return self.visitExpression(ctx.expression())

    def visitExpression(self, ctx:PythonToLaTeXParser.ExpressionContext):
        if ctx.getChildCount() > 1 and ctx.getChild(1).getText() in ['+', '-']:
            left = self.visitExpression(ctx.expression())
            right = self.visitTerm(ctx.term())
            operator = ctx.getChild(1).getText()
            return f"{left} {operator} {right}"
        else:
            return self.visitTerm(ctx.term())

    def visitTerm(self, ctx: PythonToLaTeXParser.TermContext):
        if ctx.getChildCount() > 1 and ctx.getChild(1).getText() in ['*', '/']:
            left = self.visitTerm(ctx.term())
            right = self.visitFactor(ctx.factor())
            operator = ctx.getChild(1).getText()
            return f"{left} {operator} {right}"
        else:
            return self.visitFactor(ctx.factor())

    def visitFactor(self, ctx: PythonToLaTeXParser.FactorContext):
        if ctx.INT():
            return ctx.INT().getText()
        elif ctx.expression():
            return f"({self.visitExpression(ctx.expression())})"
        else:
            return None

def convert_to_latex(expression):
    lexer = PythonToLaTeXLexer(antlr4.InputStream(expression))
    stream = antlr4.CommonTokenStream(lexer)
    parser = PythonToLaTeXParser(stream)
    tree = parser.start()
    visitor = PythonToLaTeXVisitor()
    return visitor.visitStart(tree)


expression = "2 + 3 * 4"
latex = convert_to_latex(expression)
print(latex)
