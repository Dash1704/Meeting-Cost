"""Drop columns table and add start/stop time to meetings

Revision ID: e583fa137323
Revises: 58d9d90978ec
Create Date: 2025-02-11 14:48:41.968325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e583fa137323'
down_revision: Union[str, None] = '58d9d90978ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('companies')


def downgrade() -> None:
    op.create_table(
        'companies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False)
    )
