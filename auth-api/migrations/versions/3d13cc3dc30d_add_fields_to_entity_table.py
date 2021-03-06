"""Add fields to entity table

Revision ID: 3d13cc3dc30d
Revises: a4519a2af112
Create Date: 2019-08-26 11:29:25.581154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d13cc3dc30d'
down_revision = 'a4519a2af112'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entity', sa.Column('business_number', sa.String(length=100), nullable=False, server_default=''))
    op.alter_column('entity', 'business_number', server_default=None)
    op.add_column('entity', sa.Column('name', sa.String(length=250), nullable=False, server_default=''))
    op.alter_column('entity', 'name', server_default=None)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entity', 'name')
    op.drop_column('entity', 'business_number')
    # ### end Alembic commands ###
