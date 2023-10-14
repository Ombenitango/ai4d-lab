"""Tests for views.py."""

import pytest

import ckanext.ai4dlab.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "ai4dlab")
@pytest.mark.usefixtures("with_plugins")
def test_ai4dlab_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("ai4dlab.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, ai4dlab!"
