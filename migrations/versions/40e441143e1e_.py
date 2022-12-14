"""empty message

Revision ID: 40e441143e1e
Revises: 
Create Date: 2022-09-06 23:56:28.765094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e441143e1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('id_country', sa.Integer(), nullable=True),
    sa.Column('id_department', sa.Integer(), nullable=True),
    sa.Column('id_city', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_user')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
