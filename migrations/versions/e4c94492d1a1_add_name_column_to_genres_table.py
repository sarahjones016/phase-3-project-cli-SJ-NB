"""add Name column to genres table

Revision ID: e4c94492d1a1
Revises: 88858ec7b614
Create Date: 2023-05-16 10:30:08.158865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c94492d1a1'
down_revision = '88858ec7b614'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('genres', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('genres', 'name')
    # ### end Alembic commands ###
