"""Add table privileges

Revision ID: 9d0a3131ece2
Revises: 0ba8ef5e4623
Create Date: 2020-11-17 13:49:40.789664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d0a3131ece2'
down_revision = '0ba8ef5e4623'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'privileges',
        sa.Column('priv_id', sa.Integer, primary_key=True),
        sa.Column('priv_name', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('privileges')
