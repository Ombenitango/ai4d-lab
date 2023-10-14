from ckan.plugins import toolkit
from ckan.lib.base import BaseController
class YourController(BaseController):
    
    def discussion_test(self, action, id):
        return toolkit.render('your_template.html', {'param': 'value'})
