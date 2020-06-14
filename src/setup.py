from setuptools import setup, find_packages

setup (
  name='ccllexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  ccllexer = ccllexer.lexer:CCLLexer
  """,
)