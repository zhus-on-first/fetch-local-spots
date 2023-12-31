"""move comment to report table from reported feature

Revision ID: bb68b2e0c05b
Revises: ba6e44840e1a
Create Date: 2023-10-23 17:05:41.666386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb68b2e0c05b'
down_revision = 'ba6e44840e1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location_features', schema=None) as batch_op:
        batch_op.alter_column('feature',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)

    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.alter_column('location_type_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('reported_features', schema=None) as batch_op:
        batch_op.drop_column('comment')

    with op.batch_alter_table('reports', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reports', schema=None) as batch_op:
        batch_op.drop_column('comment')

    with op.batch_alter_table('reported_features', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment', sa.VARCHAR(length=255), nullable=True))

    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.alter_column('location_type_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('location_features', schema=None) as batch_op:
        batch_op.alter_column('feature',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)

    # ### end Alembic commands ###
