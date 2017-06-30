import lsystemLexer
from lgrammar.lsystemParser import lsystemParser
import lgrammarVisitor
import antlr4

def parse(text):
    my_lexer = lsystemLexer.lsystemLexer(antlr4.InputStream(text))
    my_parser = lsystemParser(antlr4.CommonTokenStream(my_lexer))
    return lgrammarVisitor.lgrammarVisitor().visit(my_parser.code())

