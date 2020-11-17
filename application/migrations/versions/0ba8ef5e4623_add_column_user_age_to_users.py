"""Add column user_age to users

Revision ID: 0ba8ef5e4623
Revises: 195a4a84178f
Create Date: 2020-11-17 13:41:55.274671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba8ef5e4623'
down_revision = '195a4a84178f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',
                  sa.Column('user_age', sa.Integer))


def downgrade():
    op.drop_column('users', 'user_age')
