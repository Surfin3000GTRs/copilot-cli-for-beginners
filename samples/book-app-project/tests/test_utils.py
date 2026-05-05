import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from books import Book
from utils import print_books


def test_print_books_shows_empty_message(capsys):
    print_books([])

    captured = capsys.readouterr()

    assert captured.out == "No books found.\n"


def test_print_books_uses_shared_cli_format(capsys):
    books = [
        Book(title="1984", author="George Orwell", year=1949, read=False),
        Book(title="Dune", author="Frank Herbert", year=1965, read=True),
    ]

    print_books(books)

    captured = capsys.readouterr()

    assert captured.out == (
        "\nYour Book Collection:\n\n"
        "1. [ ] 1984 by George Orwell (1949)\n"
        "2. [✓] Dune by Frank Herbert (1965)\n\n"
    )
