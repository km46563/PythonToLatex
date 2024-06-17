import antlr4
import logging
from PythonToLaTeXLexer import PythonToLaTeXLexer
from PythonToLaTeXParser import PythonToLaTeXParser


# there is possibility to run "DEBUG" mode by changing between 'level=logging.INFO' and 'level=logging.DEBUG'
logging.basicConfig(format='%(asctime)-2s,%(levelname)-2s [%(filename)s:%(lineno)d] in func %(funcName)-2s ->  %(message)s',
                    filename='latex_lexer.log', level=logging.INFO, filemode="w")


class PythonToLaTeXVisitor(antlr4.ParseTreeVisitor):
    def __init__(self, parser, token_stream, lexer):
        logging.info(f"Create an instance of 'PythonToLaTeXVisitor'")
        self.parser = parser
        self.tokens_stream = token_stream
        self.lexer = lexer

    def visitStart(self, ctx: PythonToLaTeXParser.StartContext):
        logging.info(f"Start 'visitStart'")
        logging.debug(f"contain ctx object with those elements: {ctx.__dir__()}")
        logging.info(f"ctx contain text in 'ctx.getText()' :  {ctx.getText()}")
        logging.info(f"ctx has {ctx.getChildCount()} children: with {[x for x in range(ctx.getChildCount())]} index ")
        logging.debug(f"they can be called by 'ctx.getChild(i)' where 'i' is the child index and have those elements {ctx.getChild(0).__dir__()}")
        logging.info(f"The '0' contain this text: '{ctx.getChild(0).getText()}' and 'EOF' contain text: '{ctx.getChild(ctx.getChildCount()-1).getText()}'")
        for i in range(ctx.getChildCount()-1):   # we want to skip <EOF> so we didn't look at the last child ;)
            child = ctx.getChild(i)
            rule_index = child.getRuleIndex()
            child_name = self.parser.ruleNames[rule_index]
            logging.info(f"found child name '{child_name}'")
            if child_name == "equation":
                logging.info(f"Going deeper in the tree by calling 'visitEquation' with found child")
                return f"{self.visitEquation(child)}"
        logging.info(f"The program did not find any matching part of the equation")
        logging.info(f"!!! Returning Empty result !!!")
        return ""

    def visitEquation(self, ctx: PythonToLaTeXParser.EquationContext):
        logging.info(f"Start 'visitEquation'")
        logging.debug(f"Equation children: {ctx.__dir__()}")
        if hasattr(ctx, "stat"):
            logging.info(f"Found 'Stat' named child: '{ctx.getText()}'")
            logging.info(f"This means that there are no longer any of equal or inequality signs in this branch")
            logging.info(f"In this case time to go deeper by calling 'visitStat' with found child")
            return self.visitStat(ctx.stat())
        else:
            logging.info(f"Found equation operator '{ctx.op.text}'")
            if ctx.op.text == "!=":
                logging.info(f"UnEqual sign in LaTeX is written as '\\neq'")
                logging.info(f"ctx object has {ctx.getChildCount()} children")
                logging.debug(f"ctx has available objects: {ctx.__dir__()}")
                if ctx.getChildCount() > 2:
                    logging.info(f"More than two children means there are a left and a right side of the equation")
                    return self.visitEquation(ctx.l)+r"\neq"+self.visitEquation(ctx.r)
                else:
                    logging.info(f"Two or less children means there is only a left side and the equation ends with equal sign")
                    return self.visitEquation(ctx.l)+r"\neq"
            elif ctx.op.text == "=":
                logging.info(f"Equal sign in LaTeX is written as '='")
                logging.info(f"ctx object has {ctx.getChildCount()} children")
                logging.debug(f"ctx has available objects: {ctx.__dir__()}")
                if ctx.getChildCount() > 2:
                    logging.info(f"More than two children means there are a left and a right side of the equation")
                    return self.visitEquation(ctx.l)+r"="+self.visitEquation(ctx.r)
                else:
                    logging.info(f"Two or less children means there is only a left side and the equation ends with equal sign")
                    return self.visitEquation(ctx.l)+r"="
            elif ctx.op.text == ">":
                logging.info(f"Greater sign in LaTeX is written as '>'")
                logging.info(f"ctx object has {ctx.getChildCount()} children")
                logging.debug(f"ctx has available objects: {ctx.__dir__()}")
                if ctx.getChildCount() > 2:
                    logging.info(f"More than two children means there are a left and a right side of the equation")
                    return self.visitEquation(ctx.l)+r">"+self.visitEquation(ctx.r)
                else:
                    logging.info(f"One children means there is only a left side and the equation ends with equal sign")
                    return self.visitEquation(ctx.l)+r">"
            elif ctx.op.text == ">=":
                logging.info(f"Greater or equal sign in LaTeX is written as '\\geq'")
                logging.info(f"ctx object has {ctx.getChildCount()} children")
                logging.debug(f"ctx has available objects: {ctx.__dir__()}")
                if ctx.getChildCount() > 2:
                    logging.info(f"More than two children means there are a left and a right side of the equation")
                    return self.visitEquation(ctx.l)+r"\geq"+self.visitEquation(ctx.r)
                else:
                    logging.info(f"Two or less children means there is only a left side and the equation ends with equal sign")
                    return self.visitEquation(ctx.l)+r"\geq"
            elif ctx.op.text == "<":
                logging.info(f"Lesser sign in LaTeX is written as '<'")
                logging.info(f"ctx object has {ctx.getChildCount()} children")
                logging.debug(f"ctx has available objects: {ctx.__dir__()}")
                if ctx.getChildCount() > 2:
                    logging.info(f"More than two children means there are a left and a right side of the equation")
                    return self.visitEquation(ctx.l)+r"<"+self.visitEquation(ctx.r)
                else:
                    logging.info(f"Two or less children means there is only a left side and the equation ends with equal sign")
                    return self.visitEquation(ctx.l)+r"<"
            elif ctx.op.text == "<=":
                logging.info(f"Lesser or equal sign in LaTeX is written as '\\le'")
                logging.info(f"ctx object has {ctx.getChildCount()} children")
                logging.debug(f"ctx has available objects: {ctx.__dir__()}")
                if ctx.getChildCount() > 2:
                    logging.info(f"More than two children means there are a left and a right side of the equation")
                    return self.visitEquation(ctx.l)+r"\le"+self.visitEquation(ctx.r)
                else:
                    logging.info(f"Two or less children means there is only a left side and the equation ends with equal sign")
                    return self.visitEquation(ctx.l)+r"\le"
            else:
                logging.info(f"The program did not find any matching part of the equation")
                logging.info(f"!!! Returning Empty result !!!")
                return ""

    def visitStat(self, ctx: PythonToLaTeXParser.StatContext):
        logging.info(f"Start 'visitStat'")
        logging.debug(f"Stat children: {ctx.__dir__()}")
        if hasattr(ctx, 'expression'):
            logging.info(f"Found 'expression' named child: '{ctx.getText()}'")
            logging.info(f"This means that there are no longer any of bracket or equation floor in this branch")
            logging.info(f"In this case time to go deeper by calling 'visitExpression' with found child")
            return self.visitExpression(ctx.expression())
        elif hasattr(ctx, "florOp"):
            logging.info(f"Found 'florOp' named element, that means there are more than one equation floor!")
            logging.debug(f"op elements: {ctx.florOp.__dir__()}")
            if ctx.florOp.text == "//":
                logging.info(f"Found operator '//', adding '\\frac{{}}{{}}' from LaTeX language")
                logging.info(f"ctx object has {ctx.getChildCount()} children")
                if ctx.getChildCount() <= 7:
                    logging.info(f"less or equal than 7 children means there is not operations with fractions")
                    return r"\frac{" + self.visitStat(ctx.numerator) + r"}{" + self.visitStat(ctx.denominator) + r"}"
                else:
                    logging.info(f"more than sever children means there is operations with brackets!")
                    return r"\frac{" + self.visitStat(ctx.numerator) + r"}{" + self.visitStat(ctx.denominator) + r"}" +\
                        ctx.simplOp.text + self.visitStat(ctx.rest)
            if ctx.florOp.text == "^":
                logging.info(f"Found operator '^', using it as a power operation from LaTeX")
                if ctx.getChildCount() <= 7:
                    logging.info(f"less or equal than seven children means there is not operations with powers")
                    return r"{" + self.visitStat(ctx.numerator) + r"}^{" + self.visitStat(ctx.denominator) + r"}"
                else:
                    logging.info(f"more than seven children means there is operations with brackets!")
                    return r"{" + self.visitStat(ctx.numerator) + r"}^{" + self.visitStat(ctx.denominator) + r"}" + \
                        ctx.simplOp.text + self.visitStat(ctx.rest)

        elif hasattr(ctx, "LPAREN") and hasattr(ctx, "RPAREN"):
            logging.info(f"Found 'LPAREN' nad RPAREN named element, that means adding brackets is required")
            logging.debug(f"The ctx text: {ctx.getText()}")
            logging.debug(f"ctx object has {ctx.getChildCount()} children")
            if ctx.getChildCount() <= 3:
                logging.info(f"less or equal than tree children means there is not operations with brackets!")
                return r"\left(" + self.visitStat(ctx.stat()) + r"\right)"
            else:
                logging.info(f"more than tree children means there is operations with brackets!")
                logging.debug(f"ctx has {ctx.getChildCount()} children: with {[x for x in range(ctx.getChildCount())]} index")
                logging.debug(f"We are interest in child number '1' because it contain expression between brackets")
                return r"\left(" + self.visitStat(ctx.getChild(1)) + r"\right)" + ctx.simplOp.text + self.visitStat(ctx.rest)
        else:
            logging.info(f"The program did not find any matching part of the equation")
            logging.info(f"!!! Returning Empty result !!!")
            return ""


    def visitExpression(self, ctx: PythonToLaTeXParser.ExpressionContext):
        logging.info(f"Start 'visitExpression'")

        if hasattr(ctx, 'factor'):
            logging.info(f"Found 'factor' named child: '{ctx.getText()}'")
            logging.info(f"This means that there are no longer any of expressions operation in this branch")
            logging.info(f"In this case time to go deeper by calling 'visitFactor' with found child")
            return self.visitFactor(ctx.factor())
        else:
            logging.info(f"Found some expressions operation: '{ctx.op.text}' between '{ctx.l.getText()}' and '{ctx.r.getText()}'")
            return f"{self.visitExpression(ctx.l)}{ctx.op.text}{self.visitExpression(ctx.r)}"

    def visitFactor(self, ctx: PythonToLaTeXParser.FactorContext):
        logging.info(f"Start 'visitFactor'")
        if hasattr(ctx, 'INT'):
            logging.info(f"Found 'INT' named child: '{ctx.getText()}'")
            logging.info("starting climbing the branch up")
            return ctx.INT().getText()
        elif hasattr(ctx, 'ID'):
            logging.info(f"Found 'ID' named child: '{ctx.getText()}'")
            logging.info("starting climbing the branch up")
            return ctx.ID().getText()
        else:
            raise ValueError("Unknown factor context")


def convert_to_latex(expression):
    logging.info("============ Start program ============")
    logging.info(f"Entered expresion: {expression}")
    logging.info("------- Load Lexer -------")
    lexer = PythonToLaTeXLexer(antlr4.InputStream(expression))
    stream = antlr4.CommonTokenStream(lexer)
    logging.info("done")
    logging.info("------- Load Parser -------")
    parser = PythonToLaTeXParser(stream)
    tree = parser.start()
    logging.info("done")
    logging.info("------- Run Visitor -------")
    visitor = PythonToLaTeXVisitor(parser, stream, lexer)
    result = visitor.visitStart(tree)
    logging.info("done")
    logging.info(f"------- result of 'PythonToLaTeX' -------")
    logging.info(f"'{result}'")
    return result

if __name__ == '__main__':
    expression = "([2*2]//[a]+1)+2="
    latex = convert_to_latex(expression)
    print(latex)