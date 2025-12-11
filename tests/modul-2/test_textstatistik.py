"""
Tests für textstatistik.py
Testet Textanalyse-Funktionen
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    with patch("builtins.input", return_value="Test"):
        try:
            import textstatistik

            assert True
        except Exception as e:
            pytest.skip(f"Interaktives Modul: {e}")


@pytest.mark.modul2
def test_analysiere_text_funktion_existiert() -> None:
    """Test: analysiere_text Funktion existiert."""
    with patch("builtins.input", return_value="Test"):
        import textstatistik

        assert hasattr(textstatistik, "analysiere_text")


@pytest.mark.modul2
@pytest.mark.parametrize(
    "text,expected_zeichen,expected_woerter",
    [
        ("Hallo Welt", 10, 2),
        ("Python ist toll", 15, 3),
        ("Test", 4, 1),
    ],
)
def test_text_grundstatistiken(
    text: int | float | str | bool,
    expected_zeichen: int | float | str | bool,
    expected_woerter: int | float | str | bool,
) -> None:
    """Test: Grundlegende Textstatistiken."""
    with patch("builtins.input", return_value="Test"):
        import importlib

        import textstatistik

        importlib.reload(textstatistik)

        stats = textstatistik.analysiere_text(text)

        assert stats["zeichen"] == expected_zeichen
        assert stats["woerter"] == expected_woerter


@pytest.mark.modul2
def test_zeichen_ohne_leerzeichen() -> None:
    """Test: Zeichen ohne Leerzeichen zählen."""
    with patch("builtins.input", return_value="Test"):
        import importlib

        import textstatistik

        importlib.reload(textstatistik)

        text = "Hallo Welt"
        stats = textstatistik.analysiere_text(text)

        assert stats["zeichen_ohne_leer"] == 9  # 10 - 1 Leerzeichen


@pytest.mark.modul2
def test_saetze_zaehlen() -> None:
    """Test: Sätze zählen."""
    with patch("builtins.input", return_value="Test"):
        import importlib

        import textstatistik

        importlib.reload(textstatistik)

        text = "Hallo! Wie geht es? Gut."
        stats = textstatistik.analysiere_text(text)

        assert stats["saetze"] == 3


@pytest.mark.modul2
def test_gross_und_kleinbuchstaben() -> None:
    """Test: Gross- und Kleinbuchstaben zählen."""
    with patch("builtins.input", return_value="Test"):
        import importlib

        import textstatistik

        importlib.reload(textstatistik)

        text = "Hello World"
        stats = textstatistik.analysiere_text(text)

        assert stats["gross"] == 2  # H, W
        assert stats["klein"] == 8  # e,l,l,o,o,r,l,d


@pytest.mark.modul2
def test_zahlen_im_text() -> None:
    """Test: Zahlen im Text zählen."""
    with patch("builtins.input", return_value="Test"):
        import importlib

        import textstatistik

        importlib.reload(textstatistik)

        text = "Test123"
        stats = textstatistik.analysiere_text(text)

        assert stats["zahlen"] == 3


@pytest.mark.modul2
def test_durchschnittliche_wortlaenge() -> None:
    """Test: Durchschnittliche Wortlänge."""
    with patch("builtins.input", return_value="Test"):
        import importlib

        import textstatistik

        importlib.reload(textstatistik)

        text = "Hallo Welt"  # 10 Zeichen, 2 Wörter
        stats = textstatistik.analysiere_text(text)

        # Zeichen pro Wort
        assert abs(stats["zeichen_pro_wort"] - 5.0) < 0.1


@pytest.mark.modul2
def test_leerer_text() -> None:
    """Test: Leerer Text wird korrekt behandelt."""
    with patch("builtins.input", return_value="Test"):
        import importlib

        import textstatistik

        importlib.reload(textstatistik)

        text = ""
        stats = textstatistik.analysiere_text(text)

        assert stats["zeichen"] == 0
        assert stats["woerter"] == 0
