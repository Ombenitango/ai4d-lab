def ai4dlab_hello():
    return "Hello, ai4dlab!"


def format_number(number):
    return "{:,}".format(number)

def get_counts():
    from ckan.model import Session, Group, Package
    # from ckan.logic.action.get import organization_list
    from ckan.logic import get_action
    context = {}
    data_dict = {}
    organization_list = get_action('organization_list')
    organizations = organization_list(context, data_dict)
    group_count = Session.query(Group).count()
    dataset_count = Session.query(Package).count()
    organization_count = len(organizations)
    return {
        'group_count': group_count,
        'dataset_count': dataset_count,
        'organization_count': organization_count,
    }

def get_helpers():
    return {
        "ai4dlab_hello": ai4dlab_hello,
        "format_number": format_number,
        "get_counts": get_counts,
    }