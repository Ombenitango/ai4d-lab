import ckan.plugins.toolkit as tk
import ckanext.ai4dlab.logic.schema as schema


@tk.side_effect_free
def ai4dlab_get_sum(context, data_dict):
    tk.check_access(
        "ai4dlab_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.ai4dlab_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'ai4dlab_get_sum': ai4dlab_get_sum,
    }
