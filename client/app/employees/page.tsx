'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'

interface Employee {
  id: number;
  first_name: string;
  last_name: string;
  salary: number;
  weekly_hours: number;
}

export default function ShowEmployees() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/v1/employees/');
        if (!response.ok) {
          throw new Error('Failed to fetch employees');
        }
        const data = await response.json();
        setEmployees(data);
      } catch (error) {
        setError(error instanceof Error ? error.message : 'An error occurred');
      }
    };

    fetchEmployees();
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }


  return(
    <div>
      HERE ARE YOUR EMPLOYEES

      <ul>
        {employees.map((employee) => (
          <li key={employee.id}>
            {employee.first_name} {employee.last_name} - Salary: ${employee.salary} - Weekly Hours: {employee.weekly_hours}
          </li>
        ))}
      </ul>

      <div>
        Create a new employee:
        <Link href="/createEmployee">Create Employee Page</Link>
      </div>
    </div>
  )
}