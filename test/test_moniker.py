"""Moniker tests."""

import pytest
import random
from rtsim.base import Base
from rtsim.exceptions import StringError, StringLengthError
import string


def test_generic_moniker():
    """Test generic moniker."""
    base = Base("Generic")
    assert base.moniker == "Generic"


def test_moniker_not_string():
    """Test the case where a user does not input a string for the moniker."""
    with pytest.raises(StringError):
        Base(4)


def test_zero_length_moniker():
    """Test the case where a user inputs a zero length (empty) moniker."""
    with pytest.raises(StringLengthError):
        Base("")


def test_moniker_too_long():
    """Test the case where a user inputs a moniker that is > 140 characters."""
    with pytest.raises(StringLengthError):
        Base("".join(random.choices(string.ascii_letters, k=141)))  # noqa: S311
