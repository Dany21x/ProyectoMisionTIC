"""empty message

Revision ID: 94d27228e84d
Revises: 40e441143e1e
Create Date: 2022-09-27 23:21:45.871470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94d27228e84d'
down_revision = '40e441143e1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lost_pet',
    sa.Column('id_lost_pet', sa.Integer(), nullable=False),
    sa.Column('pet_type', sa.String(length=100), nullable=True),
    sa.Column('pet_breed', sa.String(length=100), nullable=True),
    sa.Column('int_pet_age', sa.Integer(), nullable=True),
    sa.Column('um_pet_age', sa.String(length=100), nullable=True),
    sa.Column('pet_color', sa.String(length=100), nullable=True),
    sa.Column('pet_location', sa.String(length=100), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('contact_numer', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id_lost_pet')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lost_pet')
    # ### end Alembic commands ###
