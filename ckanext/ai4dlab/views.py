from flask import Blueprint, request
import requests
from datetime import datetime
from ckan.plugins import toolkit


ai4dlab = Blueprint(
    "ai4dlab", __name__)


def page():
    return create_notebook()

views_bp = Blueprint('views', __name__)
@views_bp.route('/dataset/download/reason', methods=['GET'])
def download_reason():
    r_parameter = request.args.get('r')
    return  toolkit.render('/package/snippets/download_dataset.html',{'data_url':r_parameter})

def dataset_discussion(name):
    return toolkit.render('/discussion/dataset_discussion.html', {'param': name})

ai4dlab.add_url_rule(
    "/dataset/discussion/<name>", view_func=dataset_discussion)

ai4dlab.add_url_rule(
    "/notebook/new", view_func=page)

ai4dlab.add_url_rule(
    "/dataset/download/reason", view_func=download_reason)



def get_blueprints():
    return [ai4dlab]


def create_notebook():
      
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

    token="41a62eff316bc12a4ffcb29a70d7c5e58c3aa828bfee2983"

    r = requests.put(api_url + '/' + data['name'], json=data, headers={"Authorization": f"token {token}"})

    if r.status_code == 201:
        notebook_info = r.json()
        notebook_url = notebook_info['path']
        return f"Notebook URL: <a href='http://localhost:8888/notebooks/{notebook_url}' target='_blank'>http://localhost:8888/notebooks/{notebook_url}</a>"
    else:
        return 'Error creating notebook:', r.status_code