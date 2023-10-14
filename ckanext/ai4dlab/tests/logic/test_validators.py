"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.ai4dlab.logic import validators


def test_ai4dlab_reauired_with_valid_value():
    assert validators.ai4dlab_required("value") == "value"


def test_ai4dlab_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.ai4dlab_required(None)
