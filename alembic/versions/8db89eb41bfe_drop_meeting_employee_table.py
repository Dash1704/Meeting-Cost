"""Drop meeting_employee table

Revision ID: 8db89eb41bfe
Revises: a529a37db781
Create Date: 2025-02-11 14:58:05.364325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8db89eb41bfe'
down_revision: Union[str, None] = 'a529a37db781'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('meeting_employee')


def downgrade() -> None:
    op.create_table(
        'meeting_employee',
        sa.Column('meeting_id', sa.Integer(), nullable=True),
        sa.Column('employee_id', sa.Integer(), nullable=True),
       
        sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], ondelete='CASCADE'),  
        sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ondelete='CASCADE'),
    )
