"""added profil pic column

Revision ID: b2fdebcfccb4
Revises: 51ecb176454a
Create Date: 2023-10-05 20:17:38.495083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2fdebcfccb4'
down_revision = '51ecb176454a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('likes')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profil_picture', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('profil_picture')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('likes', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
