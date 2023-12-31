"""comment_table

Revision ID: d3e12e093db9
Revises: 
Create Date: 2023-10-14 14:18:12.197176

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, types,Table
import datetime

# revision identifiers, used by Alembic.
revision = 'd3e12e093db9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    from ckan.model.meta import metadata
    from ckan.model.types import make_uuid
    Table('comments', metadata,
          Column('comment_id', types.UnicodeText, primary_key=True, default=make_uuid),
          Column('text', types.UnicodeText, nullable=False),
          Column('user_email', types.UnicodeText, nullable=False),
          Column('created', types.DateTime, nullable=False, default=datetime.datetime.now),
          Column('status', types.UnicodeText, nullable=False,default='pending'),
          Column('dataset_id', types.UnicodeText, nullable=False),
    )
    metadata.create_all()



def downgrade():
    from ckan.model.meta import metadata
    metadata.reflect()
    metadata.tables['comments'].drop()
