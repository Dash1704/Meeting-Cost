'use client'

import { useState, useEffect } from 'react'
import { useRouter, useParams } from 'next/navigation'

interface Employee {
  id: number,
  first_name: string;
  last_name: string;
  salary: number;
  weekly_hours: number;
}

export default function EditEmployee() {
  const [employee, setEmployee] = useState<Employee | null>(null)
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    salary: 0,
    weekly_hours: 0,
  });

  const [error, setError] = useState<string | null>(null);
  const router = useRouter();
  const params = useParams(); //This is so I can access the dynamic route parameter

  useEffect(() => {
    const fetchEmployee = async () => {
      await fetch(`http://localhost:8000/api/v1/employees/${params.id}`)
      .then((response) => {
        if(!response.ok){
          throw new Error("Failed to fetch employee");
        }
        return response.json();
      })
      .then((data) => {
        setEmployee(data)
        setFormData({
          first_name: data.first_name,
          last_name: data.last_name,
          salary: data.salary,
          weekly_hours: data.weekly_hours,
        })
      })
      .catch((err) => {
        setError('Failed to update employee')
        console.error("Error:", err)
      })
    }

    fetchEmployee();
  }, [params.id])

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({...prev, [name]: value}));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    fetch(`http://localhost:8000/api/v1/employees/${params.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData)
    })
    .then((response) => {
      if(!response.ok){
        throw new Error("Failed to update employee")
      }
      router.push('/employees')
    })
    .catch((err) => {
      setError(err instanceof Error ? err.message : "An error occurred")
    })
  }

  return (
    <div>
      <h1>Edit Employee</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>First Name:</label>
          <input
            type="text"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Last Name:</label>
          <input
            type="text"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Salary:</label>
          <input
            type="number"
            name="salary"
            value={formData.salary}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Weekly Hours:</label>
          <input
            type="number"
            name="weekly_hours"
            value={formData.weekly_hours}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Update Employee</button>
      </form>
    </div>
  );
}
