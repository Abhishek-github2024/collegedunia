"""empty message

Revision ID: 3e4489792b66
Revises: 9d52d4270585
Create Date: 2024-04-12 14:39:59.864048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e4489792b66'
down_revision = '9d52d4270585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(length=150), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news_table', schema=None) as batch_op:
        batch_op.drop_column('url')

    # ### end Alembic commands ###
