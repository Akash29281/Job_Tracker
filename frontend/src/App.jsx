import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import Button from './components/common/button'
import tailwindcss from '@tailwindcss/vite'
import "tailwindcss"

function App() {
  return(
    <div>
      <Button text="Login " class="bg-blue-500"/> 
      <Button text="Register " class="bg-blue-500"/>
    </div>
  )
}

export default App;
