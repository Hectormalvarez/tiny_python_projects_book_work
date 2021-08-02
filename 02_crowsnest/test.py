#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

PRG = "./crowsnest.py"
consonant_words = [
    "brigantine",
    "clipper",
    "dreadnought",
    "frigate",
    "galleon",
    "haddock",
    "junk",
    "ketch",
    "longboat",
    "mullet",
    "narwhal",
    "porpoise",
    "quay",
    "regatta",
    "submarine",
    "tanker",
    "vessel",
    "whale",
    "xebec",
    "yatch",
    "zebrafish",
]
vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound"]
TEMPLATE = "Ahoy, Captain, {} {} off the larboard bow!"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rear_view, out = getstatusoutput(f"{PRG} {flag}")
        assert rear_view == 0
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f"{PRG} {word}")
        assert out.strip() == TEMPLATE.format("a", word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f"{PRG} {word.upper()}")
        assert out.strip() == f"Ahoy, Captain, A {word.upper()} off the larboard bow!"


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f"{PRG} {word}")
        assert out.strip() == TEMPLATE.format("an", word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f"{PRG} {word.upper()}")
        assert out.strip() == f"Ahoy, Captain, AN {word.upper()} off the larboard bow!"


# --------------------------------------------------
def test_starboard():
    """check for starboard"""

    out = getoutput(f"{PRG} Boat --starboard")
    assert out.strip() == "Ahoy, Captain, A Boat off the starboard bow!"
