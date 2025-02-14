'use client'

import { useState } from 'react';

export default function EmployeePage() {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    salary: '',
    weekly_hours: '',
  });

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/v1/employees/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Failed to create employee');
      }

      const data = await response.json();
      console.log('Employee created:', data);
      alert('Employee created successfully!');
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to create employee');
    }
  };

  return (
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
  );
}