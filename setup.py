from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name                            = "candl-lexer",
    version                         = "0.0.1",
    author                          = "Bruce Collie",
    author_email                    = "brucecollie82@gmail.com",
    description                     = "Lexer for the CAnDL DSL",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/Baltoli/candl-lexer",
    packages                        = find_packages(),
    install_requires                = [
        "pygments"
    ],
    classifiers                     = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires                 = ">=3.6",
    entry_points                    =
    """
    [pygments.lexers]
    candl_lexer = candl_lexer.lexer:CandlLexer
    """,
)
