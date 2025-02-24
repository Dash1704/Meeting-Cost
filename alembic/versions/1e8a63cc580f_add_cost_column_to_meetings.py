"""add_cost_column_to_meetings

Revision ID: 1e8a63cc580f
Revises: a2e978cf320c
Create Date: 2025-02-24 16:33:23.997905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '1e8a63cc580f'
down_revision: Union[str, None] = 'a2e978cf320c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('meetings', sa.Column('cost', sa.Numeric(10, 2), nullable=True))

def downgrade() -> None:
    op.drop_column('meetings', 'cost')