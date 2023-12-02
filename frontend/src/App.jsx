import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import './App.css';
import Head from './components/Home';
import Body from './components/Body';
import Navbar from './components/Navbar';
import About from './About';
import Talk2hands from './Talk2hands';
import Text2braille from './Text2braille';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={<Head />} />
          <Route exact path="/about" element={<About/>} />
          <Route exact path="/talk2hands" element={<Talk2hands/>} />
          <Route exact path="/Text2braille" element={<Text2braille/>} />
        </Routes>
      </Router>
    </>

  );
}

export default App;
