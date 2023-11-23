from sqlalchemy import Column, types
from ckan.plugins import toolkit
from ckan.model import Session
import datetime

class Comment(toolkit.BaseModel):
    from ckan.model.types import make_uuid
    __tablename__ = 'comments'
    comment_id = Column(types.UnicodeText, primary_key=True, default=make_uuid)
    text = Column(types.UnicodeText, nullable=False)
    user_email = Column(types.UnicodeText, nullable=False)
    created = Column(types.DateTime, nullable=False, default=datetime.datetime.now)
    dataset_id = Column(types.UnicodeText, nullable=False)
    status = Column(types.UnicodeText, nullable=False,default='pending')


    def comment_create(context, data_dict):
        comment = Comment(
            text=data_dict['text'],
            user_email=data_dict['user_email'],
            dataset_id=data_dict['dataset_id'],
            created=data_dict['created']
        )
        Session.add(comment)
        Session.commit()
        return comment
    
    def comment_update(context, data_dict):
        comment = Session.query(Comment).filter(Comment.comment_id == data_dict['comment_id']).first()
        comment.status = data_dict['status']
        Session.commit()
        return comment
    


    def comment_delete(context, data_dict):
        comment = Session.query(Comment).filter(Comment.id == data_dict['comment_id']).first()
        if comment and comment.email == data_dict['user_email']:
            Session.delete(comment)
            Session.commit()
            
        else:
            raise "You can not delete this comment"

    def comment_list(context, data_dict):
        dataset_id = data_dict.get('dataset_id')
        comments = Session.query(Comment).filter(Comment.dataset_id == dataset_id,Comment.status == "approved").all()
        return [{'comment_id': comment.comment_id, 'comment': comment.text, 'user_email': comment.user_email,'dataset_id':comment.dataset_id} for comment in comments]
    
    def get_comment_list(context):
        comments = Session.query(Comment).filter(Comment.status == "pending").all()
        return [{'comment_id': comment.comment_id, 'comment': comment.text, 'user_email': comment.user_email,'dataset_id':comment.dataset_id} for comment in comments]
    

    
    def last_inserted_comment(context, data_dict):
        from sqlalchemy import desc
        dataset_id = data_dict.get('dataset_id')

        last_comment = (
            Session.query(Comment)
            .filter(Comment.dataset_id == dataset_id)
            .order_by(desc(Comment.comment_id))
            .first()
        )
        
        if last_comment:
            return {
                'comment_id': last_comment.comment_id,
                'comment': last_comment.text,
                'user_email': last_comment.user_email,
                'dataset_id': last_comment.dataset_id
            }
        else:
            return None
