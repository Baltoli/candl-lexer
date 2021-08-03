from pygments.lexer import RegexLexer
from pygments.token import *

class CandlLexer(RegexLexer):
    name = 'CAnDL'
    aliases = []
    filenames = ['*.candl', '*.idl']

    keywords = [
        'include',
        'foreach',
        'forany',
        'for',
        'if not otherwise specified',
        'if',
        'then',
        'else',
        'endif',
        'collect',
        'opcode',
        'function_name',
        'Constraint',
        'End',
    ]

    tokens = {
        'root': [
            (r'{', String, 'string'),
            (r'\d+', Literal),
            (r'(' + '|'.join(keywords) + r')', Keyword),
            (r'∧|∨|=', Operator),
            (r'[\[\]\(\)\.]', Punctuation),
            (r'\s+', Whitespace),
            (r'[a-zA-Z][a-zA-Z0-9]*', Name),
        ],
        
        'string': [
            (r'[^}]+', String),
            (r'}', String, '#pop'),
        ],
    }
