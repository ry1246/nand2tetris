from const import *
from jack_tokenizer import JackTokenizer


class CompilationEngine():
    def __init__(self, filepath):
        self.wf = open(filepath[:-5] + ".myImpl.xml", 'w')
        self.tokenizer = JackTokenizer(filepath)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.wf.close()

    def compile(self):
        self.compile_class()

    def compile_class(self):
        self.write_element_start('class')
        self.compile_keyword([Tokens.CLASS])
        self.compile_class_name()
        self.compile_symbol(Tokens.LEFT_CURLY_BRACKET)

        