"""empty message

Revision ID: 11dd02d5af84
Revises: a89f23eaed75
Create Date: 2022-10-01 18:05:19.498978

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11dd02d5af84'
down_revision = 'a89f23eaed75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    op.drop_table('city')
    op.alter_column('country', 'country_name',
               existing_type=mysql.VARCHAR(collation='utf8_spanish2_ci', length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('country', 'country_name',
               existing_type=mysql.VARCHAR(collation='utf8_spanish2_ci', length=100),
               nullable=False)
    op.create_table('city',
    sa.Column('id_municipio', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('municipio', mysql.VARCHAR(collation='utf8_spanish2_ci', length=100), nullable=False),
    sa.Column('estado', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('id_departamento', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_departamento'], ['department.id_departament'], name='city_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_municipio'),
    mysql_collate='utf8_spanish2_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('department',
    sa.Column('id_departament', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('departament_name', mysql.VARCHAR(collation='utf8_spanish2_ci', length=100), nullable=False),
    sa.Column('id_pais', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_pais'], ['country.id_country'], name='department_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_departament'),
    mysql_collate='utf8_spanish2_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
