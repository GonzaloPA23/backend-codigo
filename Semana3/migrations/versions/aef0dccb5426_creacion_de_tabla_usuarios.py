"""creacion de tabla usuarios

Revision ID: aef0dccb5426
Revises: 
Create Date: 2023-07-26 22:32:31.113790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aef0dccb5426'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('apellido', sa.Text(), nullable=True),
    sa.Column('correo', sa.Text(), nullable=False),
    sa.Column('telefono', sa.Text(), nullable=True),
    sa.Column('linkedin_url', sa.Text(), nullable=True),
    sa.Column('direccion', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###
