from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser

def main():
    # Load the test program from a file (e.g., 'test_program.txt')
    with open('test_program.txt', 'r') as file:
        input_string = file.read()

    input_stream = InputStream(input_string)

    # Lexer step
    lexer = MyLangLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Parser step
    parser = MyLangParser(stream)
    tree = parser.program()  # Adjust 'program' to your grammar's starting rule

    print("The parse tree:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
