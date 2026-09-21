import importlib.util
import os

import pytest

SPEC = importlib.util.spec_from_file_location(
    "sample4", os.path.join(os.path.dirname(__file__), "Sample-4.py")
)
sample4 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sample4)

is_valid_jumin = sample4.is_valid_jumin


def test_valid_jumin_passes():
    assert is_valid_jumin("900101-1234568") is True


def test_invalid_checksum_fails():
    assert is_valid_jumin("900101-1234567") is False


def test_all_zero_digits():
    assert is_valid_jumin("000000-0000000") is False


@pytest.mark.parametrize("jumin", ["", "abcdef-ghijklg"])
def test_malformed_input_raises(jumin):
    with pytest.raises((ValueError, IndexError)):
        is_valid_jumin(jumin)
