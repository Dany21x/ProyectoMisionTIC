"""empty message

Revision ID: f3c75cdaed76
Revises: bf5510475724
Create Date: 2022-09-27 23:28:49.756952

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f3c75cdaed76'
down_revision = 'bf5510475724'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lost_pet', 'pet_location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lost_pet', sa.Column('pet_location', mysql.VARCHAR(collation='utf8_spanish2_ci', length=100), nullable=True))
    # ### end Alembic commands ###