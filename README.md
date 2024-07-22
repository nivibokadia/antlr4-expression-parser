Before running the files, make sure that antlr4 is installed.
antlr4 Expression.g4
python compiler.py test\input.txt test\bytecode.txt
python VM1.py test\bytecode.txt
