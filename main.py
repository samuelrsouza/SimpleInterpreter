from interpreter import Interpreter
from lexer import Lexer
from parser_ import *

while True:
    try:
        text = input("calc: ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpreter = Interpreter
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)
