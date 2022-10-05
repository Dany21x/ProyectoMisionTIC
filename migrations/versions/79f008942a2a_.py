"""empty message

Revision ID: 79f008942a2a
Revises: f2a97c2ead9d
Create Date: 2022-10-01 19:01:21.702680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79f008942a2a'
down_revision = 'f2a97c2ead9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id_country', sa.Integer(), nullable=False),
    sa.Column('country_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id_country')
    )
    op.create_table('department',
    sa.Column('id_department', sa.Integer(), nullable=False),
    sa.Column('department_name', sa.String(length=100), nullable=True),
    sa.Column('id_country', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_country'], ['country.id_country'], ),
    sa.PrimaryKeyConstraint('id_department')
    )
    op.create_table('city',
    sa.Column('id_city', sa.Integer(), nullable=False),
    sa.Column('city_name', sa.String(length=100), nullable=True),
    sa.Column('state', sa.Integer(), nullable=True),
    sa.Column('id_department', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_department'], ['department.id_department'], ),
    sa.PrimaryKeyConstraint('id_city')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    op.drop_table('department')
    op.drop_table('country')
    # ### end Alembic commands ###