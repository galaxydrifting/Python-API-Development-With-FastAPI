"""add phone number

Revision ID: 4281a15f99bb
Revises: 7717dd78907f
Create Date: 2022-06-14 23:55:51.110625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4281a15f99bb'
down_revision = '7717dd78907f'
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
