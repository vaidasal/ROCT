"""Remove Data from OctCSV Table

Revision ID: 70cd017ecec2
Revises: 93c3526b1071
Create Date: 2021-08-20 12:40:08.389804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '70cd017ecec2'
down_revision = '93c3526b1071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('octcsv', 'data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('octcsv', sa.Column('data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
