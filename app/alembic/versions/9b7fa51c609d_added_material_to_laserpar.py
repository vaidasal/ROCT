"""Added material to laserpar

Revision ID: 9b7fa51c609d
Revises: 0546d65ba79e
Create Date: 2021-10-04 10:25:36.737168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b7fa51c609d'
down_revision = '0546d65ba79e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('laserpar', sa.Column('part_number', sa.String(), nullable=True))
    op.add_column('laserpar', sa.Column('laser_programm', sa.Integer(), nullable=True))
    op.add_column('laserpar', sa.Column('ramp_length', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('ramp_type', sa.String(), nullable=True))
    op.add_column('laserpar', sa.Column('laser_power', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('puls_duration', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('fiber_diameter', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('sheet_1_height', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('sheet_2_height', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('sheet_3_height', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('gap_1', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('gap_2', sa.Float(), nullable=True))
    op.add_column('laserpar', sa.Column('material', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('laserpar', 'material')
    op.drop_column('laserpar', 'gap_2')
    op.drop_column('laserpar', 'gap_1')
    op.drop_column('laserpar', 'sheet_3_height')
    op.drop_column('laserpar', 'sheet_2_height')
    op.drop_column('laserpar', 'sheet_1_height')
    op.drop_column('laserpar', 'fiber_diameter')
    op.drop_column('laserpar', 'puls_duration')
    op.drop_column('laserpar', 'laser_power')
    op.drop_column('laserpar', 'ramp_type')
    op.drop_column('laserpar', 'ramp_length')
    op.drop_column('laserpar', 'laser_programm')
    op.drop_column('laserpar', 'part_number')
    # ### end Alembic commands ###