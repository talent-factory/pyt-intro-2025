"""
Tests für strings.py
Testet String-Operationen
"""

import sys
from pathlib import Path

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    try:
        import strings

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul2
@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("Hello", " World", "Hello World"),
        ("Python", "!", "Python!"),
        ("Max", " Muster", "Max Muster"),
    ],
)
def test_string_konkatenation(
    s1: int | float | str | bool,
    s2: int | float | str | bool,
    expected: int | float | str | bool,
) -> None:
    """Test: String-Konkatenation funktioniert."""
    result = s1 + s2
    assert result == expected


@pytest.mark.modul2
@pytest.mark.parametrize(
    "char,n,expected",
    [
        ("*", 5, "*****"),
        ("=", 10, "=========="),
        ("-", 3, "---"),
    ],
)
def test_string_multiplikation(
    char: int | float | str | bool,
    n: int | float | str | bool,
    expected: int | float | str | bool,
) -> None:
    """Test: String-Multiplikation funktioniert."""
    result = char * n
    assert result == expected


@pytest.mark.modul2
@pytest.mark.parametrize(
    "text,expected_length",
    [
        ("Python", 6),
        ("Hello World", 11),
        ("", 0),
    ],
)
def test_string_laenge(
    text: int | float | str | bool, expected_length: int | float | str | bool
) -> None:
    """Test: len() gibt korrekte Länge zurück."""
    assert len(text) == expected_length


@pytest.mark.modul2
@pytest.mark.parametrize(
    "text,index,expected_char",
    [
        ("Python", 0, "P"),
        ("Python", 1, "y"),
        ("Python", -1, "n"),
        ("Python", -2, "o"),
    ],
)
def test_string_indexierung(
    text: int | float | str | bool,
    index: int | float | str | bool,
    expected_char: int | float | str | bool,
) -> None:
    """Test: String-Indexierung funktioniert."""
    assert text[index] == expected_char


@pytest.mark.modul2
@pytest.mark.parametrize(
    "text,start,end,expected",
    [
        ("Python", 0, 2, "Py"),
        ("Python", 2, 4, "th"),
        ("Python Programmierung", 0, 6, "Python"),
        ("Python Programmierung", 7, None, "Programmierung"),
    ],
)
def test_string_slicing(
    text: int | float | str | bool,
    start: int | float | str | bool,
    end: int | float | str | bool,
    expected: int | float | str | bool,
) -> None:
    """Test: String-Slicing funktioniert."""
    if end is None:
        result = text[start:]
    else:
        result = text[start:end]
    assert result == expected


@pytest.mark.modul2
@pytest.mark.parametrize(
    "text,expected_upper,expected_lower",
    [
        ("Hello", "HELLO", "hello"),
        ("Python", "PYTHON", "python"),
        ("MiXeD", "MIXED", "mixed"),
    ],
)
def test_string_case_methoden(
    text: int | float | str | bool,
    expected_upper: int | float | str | bool,
    expected_lower: int | float | str | bool,
) -> None:
    """Test: upper() und lower() funktionieren."""
    assert text.upper() == expected_upper
    assert text.lower() == expected_lower


@pytest.mark.modul2
def test_string_strip() -> None:
    """Test: strip() entfernt Leerzeichen."""
    text = "  Hello  "
    assert text.strip() == "Hello"
    assert text.lstrip() == "Hello  "
    assert text.rstrip() == "  Hello"


@pytest.mark.modul2
def test_string_replace() -> None:
    """Test: replace() ersetzt Teilstrings."""
    text = "Hello World"
    result = text.replace("World", "Python")
    assert result == "Hello Python"


@pytest.mark.modul2
def test_string_split() -> None:
    """Test: split() teilt Strings auf."""
    text = "Python ist toll"
    words = text.split()
    assert words == ["Python", "ist", "toll"]
    assert len(words) == 3


@pytest.mark.modul2
@pytest.mark.parametrize(
    "text,prefix,expected",
    [
        ("Python", "Py", True),
        ("Python", "py", False),
        ("Hello", "He", True),
    ],
)
def test_string_startswith(
    text: int | float | str | bool,
    prefix: int | float | str | bool,
    expected: int | float | str | bool,
) -> None:
    """Test: startswith() prüft Präfix."""
    assert text.startswith(prefix) == expected


@pytest.mark.modul2
@pytest.mark.parametrize(
    "text,suffix,expected",
    [
        ("Python", "on", True),
        ("Python", "On", False),
        ("test.py", ".py", True),
    ],
)
def test_string_endswith(
    text: int | float | str | bool,
    suffix: int | float | str | bool,
    expected: int | float | str | bool,
) -> None:
    """Test: endswith() prüft Suffix."""
    assert text.endswith(suffix) == expected


@pytest.mark.modul2
def test_string_join() -> None:
    """Test: join() verbindet Strings."""
    words = ["Python", "ist", "toll"]
    result = " ".join(words)
    assert result == "Python ist toll"

    result = "-".join(words)
    assert result == "Python-ist-toll"


@pytest.mark.modul2
def test_string_unveraenderlich() -> None:
    """Test: Strings sind unveränderlich."""
    name = "anna"
    name.upper()  # Ändert nicht den Original-String
    assert name == "anna"

    name = name.upper()  # Neue Zuweisung erforderlich
    assert name == "ANNA"
