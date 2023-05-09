import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import SignUp from './sign-up-screen.tsx'
import './sign-up-screen.css'


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <SignUp />
  </React.StrictMode>,
)
