"""empty message

Revision ID: a6f75bd19b07
Revises: 09aab84ef0e1
Create Date: 2022-10-07 09:05:57.380164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6f75bd19b07'
down_revision = '09aab84ef0e1'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table('votes', sa.Column('user_id', sa.Integer(), nullable=False, primary_key=True), sa.Column('post_id', sa.Integer(), nullable=False, primary_key=True))
     op.create_foreign_key('users_fk', source_table='votes', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
     op.create_foreign_key('posts_fk', source_table='votes', referent_table='posts', local_cols=['post_id'], remote_cols=['id'], ondelete="CASCADE")
     pass


def downgrade():
    op.drop_constraint('users_fk', table_name="votes")
    op.drop_constraint('posts_fk', table_name="votes")
    op.drop_table('votes')
    pass
