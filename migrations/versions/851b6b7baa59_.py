"""empty message

Revision ID: 851b6b7baa59
Revises: 
Create Date: 2017-02-15 21:37:19.646390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851b6b7baa59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookmarks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_bookmarks_title'), 'bookmarks', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bookmarks_title'), table_name='bookmarks')
    op.drop_table('bookmarks')
    # ### end Alembic commands ###
