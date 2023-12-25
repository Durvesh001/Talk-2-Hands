import React from "react";
import "./Navbar.css";
import { Link } from "react-router-dom";

const Navbar = () => {
  const stopCamera = () => {
    if (videoRef.current) {
      const stream = videoRef.current.srcObject;
      if (stream) {
        const tracks = stream.getTracks();

        tracks.forEach((track) => {
          track.stop(); // Stop each track in the stream
        });

        videoRef.current.srcObject = null; // Release the stream
      }
    }
  };

  return (
    <div className="Nav">
      <nav>
        <div className="Logo">
          <img src="/images/final_logo.png" alt="Logo" />
          <p className="logotext">TouchSign Bridge</p>
        </div>

        <div className="contents">
          <ul>
            <li>
              <Link to="/" className="nav-link" onClick={stopCamera}>
                Home
              </Link>
            </li>
            <li>
              <Link to="/about" className="nav-link" onClick={stopCamera}>
                About
              </Link>
            </li>
            <li>
            <Link to="/" className="user-icon" onClick={stopCamera}>
                <button>
                  <i className="fas fa-user" />
                </button>
              </Link>
            </li>
          </ul>
        </div>
        </nav>
    </div>

  );
};

export default Navbar;
