"""Remove company table, update meetings and employees

Revision ID: 5e8f1717065b
Revises: 8fe2bf9d9101
Create Date: 2025-02-11 12:26:42.008385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e8f1717065b'
down_revision: Union[str, None] = '8fe2bf9d9101'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("SET foreign_key_checks = 0") 
    try:
        op.drop_constraint('meetings_ibfk_1', 'meetings', type_='foreignkey')
    except Exception:
        pass
    try:
        op.drop_constraint('employees_ibfk_1', 'employees', type_='foreignkey')
    except Exception:
        pass

    op.drop_table('companies')

    op.add_column('meetings', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.add_column('meetings', sa.Column('stop_time', sa.DateTime(), nullable=True))

    op.create_table(
        'employee_meetings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('meeting_id', sa.Integer(), sa.ForeignKey('meetings.id', ondelete="CASCADE")),
        sa.Column('employee_id', sa.Integer(), sa.ForeignKey('employees.id', ondelete="CASCADE"))
    )

    op.execute("SET foreign_key_checks = 1")

def downgrade() -> None:
    op.execute("SET foreign_key_checks = 0")

    op.drop_table('employee_meetings')

    op.drop_column('meetings', 'start_time')
    op.drop_column('meetings', 'stop_time')

    op.create_table(
        'companies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False)
    )

    op.add_column('employees', sa.Column('company_id', sa.Integer(), sa.ForeignKey('company.id')))
    op.add_column('meetings', sa.Column('company_id', sa.Integer(), sa.ForeignKey('company.id')))

    op.create_foreign_key('meetings_ibfk_1', 'meetings', 'company', ['company_id'], ['id'])
    op.create_foreign_key('employees_ibfk_1', 'employees', 'company', ['company_id'], ['id'])

    op.execute("SET foreign_key_checks = 1")


