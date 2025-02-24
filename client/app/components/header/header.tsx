'use client'

import Link from 'next/link'
import styles from './header.module.css'

interface HeaderProps {
  firstLink: string;
  secondLink: string;
  firstText: string;
  secondText: string;
}

export default function Header(props: HeaderProps){
  return (
    <header className={styles.homeHeader}>
      <div>
        <Link className={styles.logo} href='/'>MC</Link>
      </div>
      <div className={styles.headerLinks}>
        <Link className={styles.headerText} href={props.firstLink}>{props.firstText}</Link>
        <Link className={styles.headerText} href={props.secondLink}>{props.secondText}</Link>
      </div>
    </header>
  )
}