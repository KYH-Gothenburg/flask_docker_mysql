"""Create exisiting database

Revision ID: 195a4a84178f
Revises: 
Create Date: 2020-11-17 13:36:15.774935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '195a4a84178f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
     sa.Column('user_id', sa.Integer, primary_key=True),
     sa.Column('user_name', sa.String(50), nullable=False),
     sa.Column('user_first_name', sa.String(50), nullable=False),
     sa.Column('user_last_name', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('users')
