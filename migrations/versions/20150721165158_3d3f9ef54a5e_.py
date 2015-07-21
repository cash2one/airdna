"""empty message

Revision ID: 3d3f9ef54a5e
Revises: 58e19ada9ee5
Create Date: 2015-07-21 16:51:58.519463

"""

# revision identifiers, used by Alembic.
revision = '3d3f9ef54a5e'
down_revision = '58e19ada9ee5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('city', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('education', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('laboratory_site', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('public_mailbox', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('research_areas', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('school', sa.String(length=200), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'school')
    op.drop_column('user', 'research_areas')
    op.drop_column('user', 'public_mailbox')
    op.drop_column('user', 'laboratory_site')
    op.drop_column('user', 'education')
    op.drop_column('user', 'city')
    ### end Alembic commands ###
