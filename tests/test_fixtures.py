import pytest

def test_needfiles(tmp_path):
    print("this is ==> ", tmp_path)

import os

CONTENT = "content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    print(p)
    print("this is ==> ", p.read_text())
    assert p.read_text() == CONTENT