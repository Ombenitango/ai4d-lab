from sqlalchemy import Column, types,desc
from ckan.plugins import toolkit
from ckan.model import Session
import datetime
class JoinOrg(toolkit.BaseModel):
    from ckan.model.types import make_uuid
    __tablename__ = 'join_orgs'
    join_org_id=Column(types.UnicodeText,primary_key=True,default=make_uuid)
    org_id = Column(types.UnicodeText, nullable=False)
    user_email = Column(types.UnicodeText, nullable=False)
    created = Column(types.DateTime, nullable=False, default=datetime.datetime.now)
    status = Column(types.UnicodeText, nullable=False,default='pending')


    def join_org_create(context, data_dict):

        join_org = JoinOrg(
            org_id=data_dict['org_id'],
            user_email=data_dict['user_email'],
            created=data_dict['created']
        )
        Session.add(join_org)
        Session.commit()
        
    
    # def join_org_update(context, data_dict):
    #     comment = Session.query(JoinOrg).filter(JoinOrg.org_id == data_dict['org_id']).first()
    #     if comment and comment.email == data_dict['user_email']:
    #         comment.text = data_dict['text']
    #         Session.commit()
    #         return comment
    #     else:
    #         raise "You can not edit this"

    def join_org_delete(context, data_dict):
        join = Session.query(JoinOrg).filter(JoinOrg.org_id == data_dict['org_id']).first()
        if join and join.user_email == data_dict['user_email']:
            Session.delete(join)
            Session.commit()
            
        else:
            raise "You can not delete"

    def join_org_list(context):
        join_reqs = Session.query(JoinOrg).filter(JoinOrg.status == 'pending').order_by(desc(JoinOrg.created)).all()
        return [{'join_org_id': join_req.join_org_id, 'org_id': join_req.org_id, 'user_email': join_req.user_email,'created':join_req.created} for join_req in join_reqs]

    def join_org_count(context):
        count = Session.query(JoinOrg).filter(
            JoinOrg.status == 'pending'
        ).count()
        return count
