"""add start/stop time to meetings

Revision ID: a529a37db781
Revises: e583fa137323
Create Date: 2025-02-11 14:54:58.542364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a529a37db781'
down_revision: Union[str, None] = 'e583fa137323'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('meetings', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.add_column('meetings', sa.Column('stop_time', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('meetings', 'start_time')
    op.drop_column('meetings', 'stop_time')
