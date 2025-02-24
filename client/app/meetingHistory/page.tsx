'use client'

import { useState, useEffect } from 'react'
import Header from '../components/header/header'

interface Meeting {
  id: number,
  title: string,
  start_time: string,
  stop_time: string,
  cost: number
}

export default function meetingHistory() {
  const [meetings, setMeetings] = useState<Meeting[]>([]) 
  // const [totalCost, setTotalCost] = useState<number>(0)

  useEffect(() => {
    fetch('http://localhost:8000/api/v1/meetings')
      .then((response) => {
        if(!response.ok){
          throw new Error("failed to fetch meetings")
        }
        return response.json()
      })
      .then((data) => setMeetings(data))
      .catch((err) => console.log(err)) 
  }, [])

  const meetingHistoryCost = () => {
    const meetingCostArray = []
    for(let i = 0; i < meetings.length; i++){
      meetingCostArray.push(meetings[i].cost)
    }

    console.log(meetingCostArray)

    const totalCost = parseFloat(meetingCostArray.reduce((acc, money) => Number(money) + acc, 0).toFixed(2));
    return totalCost
  }

  return(
    <div>
      <Header
              firstLink='/'
              firstText='Home'
              secondLink='/employees'
              secondText='Employees'
            />
    <div>
      This is the meeting history Page
      {meetings.map((meeting) => (
        <li key={meeting.id}>
          {meeting.title} - £{meeting.cost}
        </li>
      ))}
    </div>
    <div>
      Your total cost of meetings:
      £{meetingHistoryCost()}
    </div>
    </div>
  )
}