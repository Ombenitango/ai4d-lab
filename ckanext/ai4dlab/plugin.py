import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# import ckanext.ai4dlab.cli as cli

import ckanext.ai4dlab.views as views
# from ckanext.ai4dlab.logic import (
#     action, auth, validators
# )


class Ai4DlabPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "ai4dlab")
        # new.........nealwek..


    # IAuthFunctions
    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    def get_blueprint(self):
        return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands() #

    # ITemplateHelpers

    def get_helpers(self):
        import ckanext.ai4dlab.helpers as helpers
        return {
            "ai4dlab_hello": helpers.ai4dlab_hello,
            "format_number": helpers.format_number,
            "get_counts": helpers.get_counts,
        }
        

   

    # def get_validators(self):
    #     return validators.get_validators()

    
