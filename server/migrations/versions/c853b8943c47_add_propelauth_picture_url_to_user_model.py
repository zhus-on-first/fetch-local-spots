"""add propelauth_picture_url to User model

Revision ID: c853b8943c47
Revises: 98985b7122ca
Create Date: 2023-11-09 01:27:27.098896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c853b8943c47'
down_revision = '98985b7122ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('propelauth_picture_url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('propelauth_picture_url')

    # ### end Alembic commands ###