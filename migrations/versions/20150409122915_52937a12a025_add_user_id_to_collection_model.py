"""Add user_id to Collection model.

Revision ID: 52937a12a025
Revises: 567e157a313a
Create Date: 2015-04-09 12:29:15.957950

"""

# revision identifiers, used by Alembic.
revision = '52937a12a025'
down_revision = '567e157a313a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collection', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'collection', 'user', ['user_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'collection', type_='foreignkey')
    op.drop_column('collection', 'user_id')
    ### end Alembic commands ###
