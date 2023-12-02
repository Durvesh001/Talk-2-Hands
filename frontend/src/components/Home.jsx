import React from 'react';
import './Home.css';
import Navbar from './Navbar';
import Body from './Body'

const Home = () => {
  return (
    <>
      <Navbar />
      <div className="Home">
        <div className="connection">Connecting <br/>Hands and Dots</div>
      </div>
      <Body/>
      
    </>
  );
};

export default Home;