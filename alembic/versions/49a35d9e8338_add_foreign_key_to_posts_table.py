"""add foreign-key to posts table

Revision ID: 49a35d9e8338
Revises: c865ec1a7951
Create Date: 2022-06-14 23:35:56.059054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49a35d9e8338'
down_revision = 'c865ec1a7951'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
