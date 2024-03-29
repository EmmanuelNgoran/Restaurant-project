"""Added user role

Revision ID: 50bcec5b02d2
Revises: 6d26ab67f639
Create Date: 2020-08-26 22:54:21.681206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50bcec5b02d2'
down_revision = '6d26ab67f639'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('to', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['to'], ['review.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.create_foreign_key(None, 'restaurant', 'address', ['address_id'], ['id'])
    op.create_foreign_key(None, 'restaurant', 'user', ['user_id'], ['id'])
    op.drop_column('restaurant', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('address', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.create_foreign_key(None, 'restaurant', 'address', ['address'], ['id'])
    op.drop_table('comment')
    op.drop_table('user_role')
    op.drop_table('role')
    # ### end Alembic commands ###
