"""notebooks

Revision ID: 7c3f6021cb91
Revises: d3e12e093db9
Create Date: 2023-10-19 14:26:24.616839

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, types,Table
import datetime

# revision identifiers, used by Alembic.
revision = '7c3f6021cb91'
down_revision = 'd3e12e093db9'
branch_labels = None
depends_on = None


def upgrade():
    from ckan.model.meta import metadata
    from ckan.model.types import make_uuid
    Table('notebooks', metadata,
          Column('notebook_id', types.UnicodeText, primary_key=True, default=make_uuid),
          Column('url', types.UnicodeText, nullable=False),
          Column('user_email', types.UnicodeText, nullable=False),
          Column('created', types.DateTime, nullable=False, default=datetime.datetime.now),
          Column('dataset_id', types.UnicodeText, nullable=False),
    )
    metadata.create_all()


def downgrade():
    from ckan.model.meta import metadata
    metadata.reflect()
    metadata.tables['notebooks'].drop()
