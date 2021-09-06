"""GroupOrder added to octcsv Table

Revision ID: 24676f0b38bb
Revises: 7866629b41ea
Create Date: 2021-08-21 12:21:07.898908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24676f0b38bb'
down_revision = '7866629b41ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('octcsv', sa.Column('grouporder', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('octcsv', 'grouporder')
    # ### end Alembic commands ###
