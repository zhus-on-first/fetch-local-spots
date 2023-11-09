"""add more propelauth fields to User model

Revision ID: 1c2a1832b376
Revises: c853b8943c47
Create Date: 2023-11-09 02:14:35.824548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c2a1832b376'
down_revision = 'c853b8943c47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('propelauth_first_name', sa.String(length=15), nullable=True))
        batch_op.add_column(sa.Column('propelauth_last_name', sa.String(length=15), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('propelauth_last_name')
        batch_op.drop_column('propelauth_first_name')

    # ### end Alembic commands ###
