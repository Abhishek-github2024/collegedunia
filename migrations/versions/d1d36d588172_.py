"""empty message

Revision ID: d1d36d588172
Revises: 359a6e99e2e6
Create Date: 2024-03-21 18:07:30.696183

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd1d36d588172'
down_revision = '359a6e99e2e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cutoff_table', schema=None) as batch_op:
        batch_op.alter_column('test',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('year',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    with op.batch_alter_table('fee_table', schema=None) as batch_op:
        batch_op.alter_column('year_wise',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    with op.batch_alter_table('hostel_table', schema=None) as batch_op:
        batch_op.alter_column('max_fee',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    with op.batch_alter_table('placement_table', schema=None) as batch_op:
        batch_op.drop_constraint('placement_table_ibfk_2', type_='foreignkey')
        batch_op.drop_column('course_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('placement_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('course_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('placement_table_ibfk_2', 'course_table', ['course_id'], ['course_id'])

    with op.batch_alter_table('hostel_table', schema=None) as batch_op:
        batch_op.alter_column('max_fee',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)

    with op.batch_alter_table('fee_table', schema=None) as batch_op:
        batch_op.alter_column('year_wise',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)

    with op.batch_alter_table('cutoff_table', schema=None) as batch_op:
        batch_op.alter_column('year',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
        batch_op.alter_column('test',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)

    # ### end Alembic commands ###
