"""CsvData delete cascade v5 Table

Revision ID: 118ed4ccbf4d
Revises: ca80a7686df8
Create Date: 2021-08-20 16:29:13.401742

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '118ed4ccbf4d'
down_revision = 'ca80a7686df8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('octcsv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('seamid', sa.Integer(), nullable=False),
    sa.Column('linenumber', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('csvdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('octcsv_id', sa.Integer(), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['octcsv_id'], ['octcsv.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('csvdata')
    op.drop_table('octcsv')
    # ### end Alembic commands ###
