"""add a user table

Revision ID: fdb73f16382e
Revises: e20c394dca3d
Create Date: 2022-10-05 20:38:30.331896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdb73f16382e'
down_revision = 'e20c394dca3d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                     sa.Column('id', sa.Integer(), nullable=False),
                     sa.Column('email', sa.String(), nullable=False),
                     sa.Column('password', sa.String(), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email'))

    pass


def downgrade():
    op.drop_table('users')
    pass
