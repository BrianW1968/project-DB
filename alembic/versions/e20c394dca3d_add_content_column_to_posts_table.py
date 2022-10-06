"""add content column to posts table

Revision ID: e20c394dca3d
Revises: f04ee60bb70e
Create Date: 2022-10-05 20:26:50.499077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e20c394dca3d'
down_revision = 'f04ee60bb70e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')

    pass
