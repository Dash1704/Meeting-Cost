import Link from 'next/link'
import Header from './components/header/header'

export default function Home() {
  return (
    <div>
      <Header
        firstLink='/employees'
        firstText='Employees'
        secondLink='/meetingHistory'
        secondText='Meetings'
      >
      </Header>
      THIS IS THE HOME PAGE
      {/* <div>
        Manage your employees:
        <Link href="/employees">Employee Page</Link>
      </div>

      <div>
        Create meeting:
        <Link href="/createMeeting">Create meeting Page</Link>
      </div> */}
    </div>
  )
}

