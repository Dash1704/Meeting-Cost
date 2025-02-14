import Link from 'next/link'

export default function Home() {
  return (
    <div>
      THIS IS THE HOME PAGE
      <div>
        Manage your employees:
        <Link href="/employees">Employee Page</Link>
      </div>

      <div>
        Create meeting:
        <Link href="/createMeeting">Create meeting Page</Link>
      </div>
    </div>
  )
}

