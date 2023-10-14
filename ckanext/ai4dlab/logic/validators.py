import ckan.plugins.toolkit as tk


def ai4dlab_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "ai4dlab_required": ai4dlab_required,
    }
