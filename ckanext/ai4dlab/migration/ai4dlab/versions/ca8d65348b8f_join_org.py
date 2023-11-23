"""join_org

Revision ID: 012c401cb5d4
Revises: 7c3f6021cb91
Create Date: 2023-10-19 14:26:58.625197

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, types,Table
import datetime

# revision identifiers, used by Alembic.
revision = 'ca8d65348b8f'
down_revision = '7c3f6021cb91'
branch_labels = None
depends_on = None


def upgrade():
    from ckan.model.meta import metadata
    from ckan.model.types import make_uuid
    Table('join_orgs', metadata,
          Column('join_org_id', types.UnicodeText, primary_key=True, default=make_uuid),
          Column('org_id', types.UnicodeText, nullable=False),
          Column('user_email', types.UnicodeText, nullable=False),
          Column('status', types.UnicodeText,default='pending'),
          Column('created', types.DateTime, nullable=False, default=datetime.datetime.now),
    )
    metadata.create_all()


def downgrade():
    from ckan.model.meta import metadata
    metadata.reflect()
    metadata.tables['join_orgs'].drop()

