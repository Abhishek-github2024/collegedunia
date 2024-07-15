"""empty message

Revision ID: bfc49f9b18ac
Revises: 583c3ac8ebab
Create Date: 2024-03-28 10:16:54.611330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfc49f9b18ac'
down_revision = '583c3ac8ebab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fee_table', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'university_table', ['university_id'], ['university_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fee_table', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###