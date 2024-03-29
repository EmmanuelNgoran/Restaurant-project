"""Second Migration

Revision ID: d306f5233db7
Revises: 
Create Date: 2020-08-12 03:19:58.179912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd306f5233db7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'restaurant', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.drop_column('restaurant', 'user_id')
    # ### end Alembic commands ###
