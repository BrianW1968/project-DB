"""add phone number

Revision ID: 09aab84ef0e1
Revises: e6035900db4a
Create Date: 2022-10-06 08:33:04.688322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09aab84ef0e1'
down_revision = 'e6035900db4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###