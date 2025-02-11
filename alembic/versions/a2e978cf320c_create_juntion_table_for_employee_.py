"""Create juntion table for employee_meetings

Revision ID: a2e978cf320c
Revises: 8db89eb41bfe
Create Date: 2025-02-11 15:02:29.297418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2e978cf320c'
down_revision: Union[str, None] = '8db89eb41bfe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'employee_meetings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('meeting_id', sa.Integer(), sa.ForeignKey('meetings.id', ondelete="CASCADE")),
        sa.Column('employee_id', sa.Integer(), sa.ForeignKey('employees.id', ondelete="CASCADE"))
    )


def downgrade() -> None:
    op.drop_table('employee_meetings')
