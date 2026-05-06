import importlib
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import books


@pytest.fixture
def book_app_module(tmp_path, monkeypatch):
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(books, "DATA_FILE", str(temp_file))

    import book_app

    return importlib.reload(book_app)


def test_main_dispatches_list_command(book_app_module, monkeypatch):
    calls: list[str] = []

    def fake_handle_list() -> None:
        calls.append("list")

    monkeypatch.setattr(book_app_module, "handle_list", fake_handle_list)
    monkeypatch.setattr(sys, "argv", ["book_app.py", "list"])

    book_app_module.main()

    assert calls == ["list"]


def test_main_shows_help_for_unknown_command(book_app_module, monkeypatch, capsys):
    calls: list[str] = []

    def fake_show_help() -> None:
        calls.append("help")

    monkeypatch.setattr(book_app_module, "show_help", fake_show_help)
    monkeypatch.setattr(sys, "argv", ["book_app.py", "unknown"])

    book_app_module.main()

    captured = capsys.readouterr()
    assert "Unknown command." in captured.out
    assert calls == ["help"]
