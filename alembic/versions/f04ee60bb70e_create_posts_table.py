"""Create posts table

Revision ID: f04ee60bb70e
Revises: 
Create Date: 2022-10-05 14:19:40.322243

"""
from operator import truediv
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f04ee60bb70e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))

    pass

def downgrade():
    op.drop_table('posts')
    pass
