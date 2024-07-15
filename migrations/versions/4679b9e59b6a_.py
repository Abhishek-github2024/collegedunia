"""empty message

Revision ID: 4679b9e59b6a
Revises: 84026c55afc4
Create Date: 2024-03-26 12:10:06.347757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4679b9e59b6a'
down_revision = '84026c55afc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('jti', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_table', schema=None) as batch_op:
        batch_op.drop_column('jti')

    # ### end Alembic commands ###