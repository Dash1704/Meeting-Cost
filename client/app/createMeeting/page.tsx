'use client'

import Link from 'next/link'
import { useState, useEffect } from 'react'

interface Employee {
  id: number;
  first_name: string;
  last_name: string;
  salary: number;
  weekly_hours: number;
}

export default function CreateMeetingPage() {
  const [formData, setFormData] = useState({
    title: '',
    start_time: '',
    stop_time: ''
  })

  const [employees, setEmployees] = useState<Employee[]>([]);
  const [selectedEmployees, setSelectedEmployees] = useState<number[]>([]);
  const [meetingCost, setMeetingCost] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/v1/employees/')
      .then((response) => {
        if(!response.ok){
          throw new Error(("Failed to fetch employees"))
        }
        return response.json();
      })
      .then((data) => setEmployees(data))
      .catch((err) => setError(err))
  }, [])  

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({...prev, [name]: value}))
  }

  const handleEmployeeSelect = (employeeId: number) => {
    setSelectedEmployees((prev) =>
      prev.includes(employeeId)
        ? prev.filter((id) => id !== employeeId) : [...prev, employeeId] 
    );
  };

  const handleStartMeeting = () => {
    setFormData((prev) => ({
      ...prev,
      start_time: new Date().toISOString(), 
    }));
  };

  const handleEndMeeting = async () => {
    const stop_time = new Date().toISOString(); 

    fetch('http://localhost:8000/api/v1/meetings/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: formData.title.trim(),
        start_time: formData.start_time,
        stop_time: stop_time,
        employee_ids: selectedEmployees,
      }),
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to save meeting');
      }
      return response.json()
    })
    .then((data) => {
      console.log('Meeting Created:', data)
      setMeetingCost(data.cost);
    })
    .catch((err) => {
      setError(err instanceof Error ? err.message : 'An error occurred');
    })
  };

  return(
    <div>
      Create a new meeting:
      <div>
        <label>Title</label>
        <input
          type='text'
          name='title'
          value={formData.title}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <h3>Choose employees</h3>
        {employees.map((employee) => 
          <div key={employee.id}>
            <label>
              <input
                type='checkbox'
                checked={selectedEmployees.includes(employee.id)}
                onChange={() => handleEmployeeSelect(employee.id)}
              />
            {employee.first_name} {employee.last_name}
            </label>
          </div>  
        )}
      </div>

      <div>
        <button onClick={handleStartMeeting} disabled={!!formData.start_time}>
          Start Meeting
        </button>
        <button onClick={handleEndMeeting} disabled={!formData.start_time || !!formData.stop_time}>
          End Meeting
        </button>
      </div>

      {meetingCost !== null && (
        <div>
          <h3>Meeting Cost:</h3>
          <p>${meetingCost}</p>
        </div>
      )}

      <div>
        Back to home:
        <Link href="/">Home Page</Link>
      </div>
    </div>
  )
}