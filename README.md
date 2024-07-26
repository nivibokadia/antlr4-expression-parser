WELCOME TO NIVI LANGUAGE.
Before running the files, make sure that antlr4 is installed.
pip install antlr4-python3-runtime                                                                       #installing runtime-antlr4
antlr4 -Dlanguage=Python3 Expression.g4                                                                  #generating lexer and parser
antlr4 -Dlanguage=Python3 -visitor Expression.g4 (if your visitor file is not generated)                 #generating lexer and parser
python compiler.py path\to\array.nivi test\array.il                                                      #compiling your .nivi file into an instruction list stored in il
python VM1.py path\to\array.il                                                                           #running your il file to gain final output
