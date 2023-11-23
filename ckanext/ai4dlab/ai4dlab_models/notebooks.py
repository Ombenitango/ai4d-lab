from sqlalchemy import Column, types
from ckan.plugins import toolkit
from ckan.model import Session
import datetime

class Notebook(toolkit.BaseModel):
    from ckan.model.types import make_uuid
    __tablename__ = 'notebooks'
    notebook_id = Column(types.UnicodeText, primary_key=True, default=make_uuid)
    url = Column(types.UnicodeText, nullable=False)
    user_email = Column(types.UnicodeText, nullable=False)
    created = Column(types.DateTime, nullable=False, default=datetime.datetime.now)
    dataset_id = Column(types.UnicodeText, nullable=False)


    def notebook_create(context, data_dict):
        notebook = Notebook(
            url=data_dict['url'],
            user_email=data_dict['user_email'],
            dataset_id=data_dict['dataset_id'],
            created=data_dict['created']
        )
        Session.add(notebook)
        Session.commit()
        return notebook
    
    # def notebook_update(context, data_dict):
    #     comment = Session.query(Comment).filter(Comment.id == data_dict['comment_id']).first()
    #     if comment and comment.email == data_dict['user_email']:
    #         comment.text = data_dict['text']
    #         Session.commit()
    #         return comment
    #     else:
    #         raise "You can not edit this comment"

    # def notebook_delete(context, data_dict):
    #     comment = Session.query(Comment).filter(Comment.id == data_dict['comment_id']).first()
    #     if comment and comment.email == data_dict['user_email']:
    #         Session.delete(comment)
    #         Session.commit()
            
    #     else:
    #         raise "You can not delete this comment"

    # def notebook_list(context, data_dict):
    #     dataset_id = data_dict.get('dataset_id')
    #     comments = Session.query(Comment).filter(Comment.dataset_id == dataset_id).all()
    #     return [{'comment_id': comment.comment_id, 'comment': comment.text, 'user_email': comment.user_email,'dataset_id':comment.dataset_id} for comment in comments]