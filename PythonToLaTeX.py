import antlr4
import sys
import logging
from PythonToLaTeXLexer import PythonToLaTeXLexer
from PythonToLaTeXParser import PythonToLaTeXParser

logging.basicConfig(format='%(asctime)-2s,%(levelname)-2s [%(filename)s:%(lineno)d] in func %(funcName)-2s ->  %(message)s',
                    filename='latex_lexer.log', level=logging.DEBUG, filemode="w")


class PythonToLaTeXVisitor(antlr4.ParseTreeVisitor):
    def __init__(self, parser, token_stream, lexer):
        self.parser = parser
        self.tokens_stream = token_stream
        self.lexer = lexer

    def visitStart(self, ctx:PythonToLaTeXParser.StartContext):
        logging.debug(f"contain ctx object with those elements: {ctx.__dir__()}")
        logging.info(f"ctx contain text in 'ctx.getText()' :  {ctx.getText()}")
        logging.info(f"ctx has {ctx.getChildCount()} children: with {[x for x in range(ctx.getChildCount())]} index ")
        logging.debug(f"they can be called by 'ctx.getChild(i)' where 'i' is the child index and have those elements {ctx.getChild(0).__dir__()}")
        logging.info(f"the '0' contain this text: '{ctx.getChild(0).getText()}' and 'EOF' contain text: '{ctx.getChild(ctx.getChildCount()-1).getText()}'")
        for i in range(ctx.getChildCount()-1):   # we want to skip <EOF>
            child = ctx.getChild(i)
            rule_index = child.getRuleIndex()
            child_name = self.parser.ruleNames[rule_index]
            logging.info(f"founded child name {child_name}")
            if child_name == "stat":
                return f"{self.visitStat(child)}"
        return None

    def visitStat(self, ctx: PythonToLaTeXParser.StatContext):
        logging.debug(f"Stat children: {ctx.__dir__()}")
        if hasattr(ctx, 'expression'):
            return self.visitExpression(ctx.expression())
        else:
            logging.debug(f"op elements: {ctx.op.__dir__()}")
            if ctx.op.text == "//":
                logging.info(f"found operator '//'")
                return r"\frac{"+self.visitStat(ctx.numerator)+r"}{"+self.visitStat(ctx.denominator)+r"}"
            if ctx.op.text == "^":
                logging.info(f"found operator '^'")
                return r"{"+self.visitStat(ctx.numerator)+r"}^{"+self.visitStat(ctx.denominator)+r"}"

    def visitExpression(self, ctx: PythonToLaTeXParser.ExpressionContext):
        # print(ctx.__dir__())
        if hasattr(ctx, 'factor'):
            return ctx.factor().getText()
        else:
            return f"{self.visitExpression(ctx.l)}{ctx.op.text}{self.visitExpression(ctx.r)}"

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
    # print(stream.__dir__())
    parser = PythonToLaTeXParser(stream)
    # print(parser.__dir__())
    tree = parser.start()
    visitor = PythonToLaTeXVisitor(parser, stream, lexer)
    return visitor.visitStart(tree)

if __name__ == '__main__':
    logging.info("============ Start program ============")
    expression = "[[[2 + 2 - 3] // [3]]//[2+2]]^[[2]//[3]]"
    logging.info(f"Entered expresion: {expression}")
    latex = convert_to_latex(expression)
    print(latex)