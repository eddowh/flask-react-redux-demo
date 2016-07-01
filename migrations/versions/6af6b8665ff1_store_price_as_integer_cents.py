"""store_price_as_integer_cents

Revision ID: 6af6b8665ff1
Revises: 873b2c69b9cd
Create Date: 2016-07-01 14:03:38.520946

"""

# revision identifiers, used by Alembic.
revision = '6af6b8665ff1'
down_revision = '873b2c69b9cd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants_menuitem', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.NUMERIC(precision=2, scale=0),
               type_=sa.Integer(),
               existing_nullable=False)

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants_menuitem', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=2, scale=0),
               existing_nullable=False)

    ### end Alembic commands ###
