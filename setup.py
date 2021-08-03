from setuptools import setup, find_packages

setup(
  name          = 'candl_lexer',
  packages      = find_packages(),
  entry_points  =
  """
  [pygments.lexers]
  candl_lexer = candl_lexer.lexer:CandlLexer
  """,
)
