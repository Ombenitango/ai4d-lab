import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def ai4dlab_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "ai4dlab_get_sum": ai4dlab_get_sum,
    }
