'use client'

import { useState } from 'react';

export default function EmployeePage() {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    salary: '',
    weekly_hours: '',
  });

  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({...prev, [name]: value}));
  }

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const payload = {
      first_name: formData.first_name.trim(),
      last_name: formData.last_name.trim(),
      salary: parseFloat(formData.salary),
      weekly_hours: parseFloat(formData.weekly_hours),
    };

    fetch('http://localhost:8000/api/v1/employees/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })
      .then((response) => {
        if(!response.ok){
          throw new Error('Failed to create employee')
        }
        return response.json()
      })
      .then((data) => {
        setSuccess("Employee created successfully")
        console.log('Employee Created:', data)
        setFormData({
          first_name: '',
          last_name: '',
          salary: '',
          weekly_hours: '',
        })
      })
      .catch((err) => {
        setError("Failed to create an employee")
        console.error("Error:", err)
      })
  };

  return (
    <div>CREATE EMPLOYEE
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
        <button type="submit">Create Employee</button>
      </form>
    </div>
  );
}