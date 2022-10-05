"""empty message

Revision ID: 21281ca87a66
Revises: 11dd02d5af84
Create Date: 2022-10-01 18:36:30.013933

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '21281ca87a66'
down_revision = '11dd02d5af84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('id_city', sa.Integer(), nullable=False))
    op.add_column('city', sa.Column('city_name', sa.String(length=100), nullable=True))
    op.add_column('city', sa.Column('id_department', sa.Integer(), nullable=True))
    op.drop_constraint('city_ibfk_1', 'city', type_='foreignkey')
    op.create_foreign_key(None, 'city', 'department', ['id_department'], ['id_department'])
    op.drop_column('city', 'id_municipio')
    op.drop_column('city', 'estado')
    op.drop_column('city', 'municipio')
    op.drop_column('city', 'id_departamento')
    op.alter_column('country', 'country_name',
               existing_type=mysql.VARCHAR(collation='utf8_spanish2_ci', length=100),
               nullable=True)
    op.add_column('department', sa.Column('id_department', sa.Integer(), nullable=False))
    op.add_column('department', sa.Column('department_name', sa.String(length=100), nullable=True))
    op.alter_column('department', 'id_country',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.drop_index('id_pais', table_name='department')
    op.drop_constraint('department_ibfk_1', 'department', type_='foreignkey')
    op.create_foreign_key(None, 'department', 'country', ['id_country'], ['id_country'])
    op.drop_column('department', 'departament_name')
    op.drop_column('department', 'id_departament')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('department', sa.Column('id_departament', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.add_column('department', sa.Column('departament_name', mysql.VARCHAR(collation='utf8_spanish2_ci', length=100), nullable=False))
    op.drop_constraint(None, 'department', type_='foreignkey')
    op.create_foreign_key('department_ibfk_1', 'department', 'country', ['id_country'], ['id_country'], ondelete='CASCADE')
    op.create_index('id_pais', 'department', ['id_country'], unique=False)
    op.alter_column('department', 'id_country',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_column('department', 'department_name')
    op.drop_column('department', 'id_department')
    op.alter_column('country', 'country_name',
               existing_type=mysql.VARCHAR(collation='utf8_spanish2_ci', length=100),
               nullable=False)
    op.add_column('city', sa.Column('id_departamento', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('city', sa.Column('municipio', mysql.VARCHAR(collation='utf8_spanish2_ci', length=100), nullable=False))
    op.add_column('city', sa.Column('estado', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('city', sa.Column('id_municipio', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'city', type_='foreignkey')
    op.create_foreign_key('city_ibfk_1', 'city', 'department', ['id_departamento'], ['id_departament'], ondelete='CASCADE')
    op.drop_column('city', 'id_department')
    op.drop_column('city', 'city_name')
    op.drop_column('city', 'id_city')
    # ### end Alembic commands ###