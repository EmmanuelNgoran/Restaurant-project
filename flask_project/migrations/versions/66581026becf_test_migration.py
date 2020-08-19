"""test migration

Revision ID: 66581026becf
Revises: 3a089a640dca
Create Date: 2020-08-14 23:04:31.334763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66581026becf'
down_revision = '3a089a640dca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.create_foreign_key(None, 'restaurant', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'restaurant', 'address', ['address_id'], ['id'])
    op.drop_column('restaurant', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('address', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.create_foreign_key(None, 'restaurant', 'address', ['address'], ['id'])
    # ### end Alembic commands ###