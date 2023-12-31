"""add token column

Revision ID: 97f5df4f51b2
Revises: 5f58a3631d64
Create Date: 2023-08-01 19:31:29.436819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97f5df4f51b2'
down_revision = '5f58a3631d64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.String(length=250), nullable=True))
        batch_op.create_unique_constraint(None, ['token'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('token')

    # ### end Alembic commands ###
