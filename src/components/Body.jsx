import React from 'react';
import './Body.css';
import { Link } from 'react-router-dom';

const Body = () => {
  return (
    <div className="Body">

      <div className="connect">
        <Link className='process' to='/talk2hands'>
          <div className="sec-1">
            <img src="/images/interpreter.jpg" alt="" srcSet="" />
            <p className="t2h">Talk 2 Hands</p>
          </div>
        </Link>

        <Link className='process' to='/Text2braille'>
          <div className="sec-2">
            <img src="/images/braille.png" alt="" srcSet="" />
            <p className="t2b">Text 2 Braille</p>
          </div>
        </Link>
      </div>

    </div>
  );
};

export default Body;
