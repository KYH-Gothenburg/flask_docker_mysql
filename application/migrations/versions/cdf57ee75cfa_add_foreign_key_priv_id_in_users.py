"""Add foreign key priv_id in users

Revision ID: cdf57ee75cfa
Revises: 9d0a3131ece2
Create Date: 2020-11-17 13:53:41.256220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdf57ee75cfa'
down_revision = '9d0a3131ece2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',
                  sa.Column('priv_id', sa.Integer, sa.ForeignKey('privileges.priv_id')))


def downgrade():
    op.drop_column('users', 'priv_id')
