"""add content column to posts table

Revision ID: 030be5876e3a
Revises: dabd63941fb0
Create Date: 2022-06-14 23:15:03.830101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '030be5876e3a'
down_revision = 'dabd63941fb0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
