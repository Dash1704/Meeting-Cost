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
    fetch('http://localhost:8000/api/v1/employees/')
      .then((response) => {
        if(!response.ok){
          throw new Error("Failed to fetch employee");
        }
        return response.json();
      })
      .then((data) => setEmployees(data))
      .catch((err) => setError(err))
  }, [])  

  const deleteEmployee = (id: number) => {
    fetch(`http://localhost:8000/api/v1/employees/${id}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if(!response.ok){
          throw new Error('Failed to delete employee')
        }
        setEmployees((prevEmployees) => prevEmployees.filter((employee) => employee.id !== id))
      })
    .catch((err) => {
      setError('Failed to delete employee')
      console.error(err)
    })
  }

  return(
    <div>
      HERE ARE YOUR EMPLOYEES
      <ul>
        {employees.map((employee) => (
          <li key={employee.id}>
            {employee.first_name} {employee.last_name} - Salary: ${employee.salary} - Weekly Hours: {employee.weekly_hours}
            - <button onClick={() => deleteEmployee(employee.id)}>Delete Employee</button>
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