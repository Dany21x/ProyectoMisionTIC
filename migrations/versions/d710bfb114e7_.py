"""empty message

Revision ID: d710bfb114e7
Revises: 8cd2daceeef6
Create Date: 2022-10-03 21:27:56.541412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd710bfb114e7'
down_revision = '8cd2daceeef6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lost_pet', sa.Column('url_pet_image', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lost_pet', 'url_pet_image')
    # ### end Alembic commands ###