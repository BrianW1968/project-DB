"""add remaining columns

Revision ID: 047fee840db1
Revises: d641e4356dd1
Create Date: 2022-10-05 21:20:55.140300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '047fee840db1'
down_revision = 'd641e4356dd1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)

    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts','created_at')
    pass
