from flask import Blueprint, request
import requests
from datetime import datetime
from ckan.plugins import toolkit
ai4dlab = Blueprint(
    "ai4dlab", __name__)


views_bp = Blueprint('views', __name__)

@views_bp.route('/dataset/download/reason', methods=['GET'])

def download_reason():
    r_parameter = request.args.get('r')
    return  toolkit.render('/package/snippets/download_dataset.html',{'data_url':r_parameter})

def dataset_discussion(name,dataset_id):
    from ckanext.ai4dlab.ai4dlab_models.comments import Comment
    comment = Comment()
    comments=comment.comment_list({'dataset_id': dataset_id})
    return toolkit.render('/discussion/dataset_discussion.html', {'param': name, 'dataset_id': dataset_id, 'comments': comments})

ai4dlab.add_url_rule(
    "/dataset/discussion/<name>/<dataset_id>", view_func=dataset_discussion)



ai4dlab.add_url_rule(
    "/dataset/download/reason", view_func=download_reason)

def add_comment():
    if not request.args:
        return "Action not allowed"
    else:
        from ckanext.ai4dlab.ai4dlab_models.comments import Comment
        text = request.args.get('comment')
        email = request.args.get('user_email')
        dataset_id = request.args.get('dataset_id')
        data = {
            'text': text,
            'user_email': email,
            'dataset_id': dataset_id,
            'created': datetime.now()
        }

        comment = Comment()
        comment.comment_create(data)
        return "Comment added"


ai4dlab.add_url_rule(
    "/discussion/new", view_func=add_comment)


@ai4dlab.route('/approve_comment/')
def approve_comment():
    user=toolkit.current_user.sysadmin
    if user:
        from ckanext.ai4dlab.ai4dlab_models.comments import Comment
        comment = Comment()
        comments=comment.get_comment_list()
        return toolkit.render('/discussion/approve_chat.html', {'comments': comments})
    else:
        return "<script>window.location.href='/user/login'</script>"


@ai4dlab.route('/approve_comment_action/')
def approve_comment_action():
    user=toolkit.current_user.sysadmin
    if user:
            from ckanext.ai4dlab.ai4dlab_models.comments import Comment
            comment = Comment()
            comment_id = request.args.get('comment_id')

            data = {
                'comment_id': comment_id,
                'status': 'approved'
            }
            comment.comment_update(data)
            return "Comment approved"
    else:
        return "<script>window.location.href='/user/login'</script>"


@ai4dlab.route('/reject_comment_action/')
def reject_comment_action():
    user=toolkit.current_user.sysadmin
    if user:
        from ckanext.ai4dlab.ai4dlab_models.comments import Comment
        comment = Comment()
        comment_id = request.args.get('comment_id')

        data = {
            'comment_id': comment_id,
            'status': 'pending'
        }
        comment.comment_update(data)
        return "Comment rejected"
    else:
        return "<script>window.location.href='/user/login'</script>"

@ai4dlab.route('/join_requests/')
def join_requests():
    from ckanext.ai4dlab.ai4dlab_models.join_org import JoinOrg
    join_org=JoinOrg()
    user=toolkit.current_user.sysadmin
    if user:
        return  toolkit.render('/join_requests.html',{'join_orgs':join_org.join_org_list(),'toolkit':toolkit.current_user.sysadmin})
    else:
        return "<script>window.location.href='/user/login'</script>"

@ai4dlab.route('/join_requests_count/')
def join_requests_count():
    user = toolkit.current_user.sysadmin
    if user:
        from ckanext.ai4dlab.ai4dlab_models.join_org import JoinOrg
        join_org = JoinOrg()
        count = join_org.join_org_count()
        return [count]
    else:
        return "<script>window.location.href='/user/login'</script>"

@ai4dlab.route('/get_new_comment/<dataset_id>')
def get_new_comment(dataset_id):
    from ckanext.ai4dlab.ai4dlab_models.comments import Comment
    comment = Comment()
    comments = comment.last_inserted_comment({'dataset_id': dataset_id})
    return comments

@ai4dlab.route('/join_organization/', methods=['GET'])
def join_organization():
    user=toolkit.current_user.email
    if user!="":
        from ckanext.ai4dlab.ai4dlab_models.join_org import JoinOrg
        user = request.args.get('user')
        org_id = request.args.get('org_id')    
        data = {
            'org_id': org_id,
            'user_email': user,
            'created': datetime.now()
        }
        join_org = JoinOrg()
        join_org.join_org_create(data)

        return "Request sent"
    else:
        return "<script>window.location.href='/user/login'</script>"

@ai4dlab.route('/notebooks/')
def get_users_notebooks():
    user=toolkit.current_user.email
    if user!="":
        return  toolkit.render('/notebook/notebook.html')
    else:
        return "<script>window.location.href='/user/login'</script>"

def get_blueprints():
    return [ai4dlab]

@ai4dlab.route("/notebook/new/",methods=['GET','POST'])
def create_notebook():
    user=toolkit.current_user.email
    if user!="":
        from ckanext.ai4dlab.ai4dlab_models.notebooks import Notebook
        dataset_id=request.args.get('dataset_id')
        user_email=request.args.get('user')

        current_datetime = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

        notebook_name = f'Notebook-{current_datetime}.ipynb'

        data = {
            'name': notebook_name,
            'kernel_name': 'python3',
            'path': '/home/ombeni/ckan/ai4dlab/notebooks',
            'content': {
                'cells': [
                    {
                        'cell_type': 'code',
                        'metadata': {},
                        'source': ['''
    !wget "http://localhost:5000/dataset/c08a769c-000e-4ef7-90e5-8a97819d299a/resource/a29a02e6-8093-4b8f-9fe2-58dc38375fbc/download/aaa.csv"

    import pandas as pd

    data =pd.read_csv("aaa.csv")

    data
                        
                        '''],
                        'outputs': []  
                    },
                    {
                        'cell_type': 'markdown',
                        'metadata': {},
                        'source': [''],
                        'outputs': []
                    }
                ],
                'metadata': {},
                'nbformat': 4,
                'nbformat_minor': 4
            }
        }

        api_url = 'http://localhost:8888/api/contents'

        token="90780fbefa86f87b22853c1115de20a2752c072f1f60e947"

        r = requests.put(api_url + '/' + data['name'], json=data, headers={"Authorization": f"token {token}"})

        if r.status_code == 201:
            notebook_info = r.json()
            notebook_url = notebook_info['path']

            final_url=f"http://localhost:8888/notebooks/{notebook_url}"
            notebook= Notebook()
            data={
                'url':final_url,
                'user_email':user_email,
                'dataset_id':dataset_id,
                'created':datetime.now()
            }
            notebook.notebook_create(data_dict=data)

            return  toolkit.render('/notebook/notebook.html',{'data_url':final_url})
        else:
            return 'Error creating notebook:', r.status_code
    else:
        return "<script>window.location.href='/user/login'</script>"