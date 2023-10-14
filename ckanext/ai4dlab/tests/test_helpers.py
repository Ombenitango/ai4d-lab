"""Tests for helpers.py."""

import ckanext.ai4dlab.helpers as helpers


def test_ai4dlab_hello():
    assert helpers.ai4dlab_hello() == "Hello, ai4dlab!"
