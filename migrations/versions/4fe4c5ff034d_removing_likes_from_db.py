"""removing likes from db

Revision ID: 4fe4c5ff034d
Revises: 2900d29cc9d8
Create Date: 2022-05-23 10:02:30.907129

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4fe4c5ff034d'
down_revision = '2900d29cc9d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like')
    op.create_foreign_key(None, 'comment', 'user', ['author'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'post', 'user', ['author'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_table('like',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.Column('author', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('post_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    # ### end Alembic commands ###
