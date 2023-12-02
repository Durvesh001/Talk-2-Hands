import './About.css'
import Navbar from './components/Navbar'
import { Link } from 'react-router-dom';


const About = () => {

    const Ieee = (event) => {
        window.open('https://drive.google.com/file/d/1hC5u4exCqOJEtTg_VJGChaEDm6JcHpLf/view?usp=sharing', '_blank');
    };
    const Report = (event) => {
        window.open('https://drive.google.com/file/d/1EUezYzZhVw0NkCvKOOz0MvdYXJnoIETT/view?usp=sharing', '_blank');
    };


    return (
        <>
            <Navbar />
            <div className="about">
                <div className="about-head">
                    <div className="container">
                        <div className="but">
                            <h1>About</h1>
                        </div>

                        <div className="exp">
                            <Link className='nav-link' to='/'><button className='explore'>Explore</button></Link>
                        </div>
                    </div>

                </div>

                <div className="about-text">
                    <p>Speech-impaired individuals often face communication
                        barriers that prevent them from effectively communicating with
                        the wider community. Sign language is a basic means of
                        communication for deaf and hard of hearing people, but many
                        individuals in the general public are unable to understand it.
                        <br /><br />The 'TouchSign Bridge' is a web-based application meticulously crafted to facilitate communication between individuals with visual and auditory impairments and those without such challenges. This software offers a dual functionality: one that translates Indian Sign Language into audio and another that transforms textual language into Braille format.</p>
                </div>


                <div className="about-head">
                    <h2>Technical Reports</h2>
                    <div className="technical">
                        <div className="report-head">
                            <Link className='nav-link' onClick={Report} target='_blank'><button>Report</button></Link>
                        </div>
                        <div className="paper-head">
                            <Link className='nav-link' onClick={Ieee} target='_blank'><button>IEEE Paper</button></Link>
                        </div>
                    </div>
                </div>




                <div className="about-head">
                    <h2>Developers</h2>
                </div>
                <div className="names">
                    <div className="first">
                        <p><strong>Durvesh Chaudhari</strong> <br />
                            Electronics Enginnering <br />
                            Sardar Patel Institute of Technology<br />
                            2020100006</p>
                    </div>
                    <div className="second">
                        <p><strong>Adrika Dikshit</strong><br />
                            Electronics Enginnering <br />
                            Sardar Patel Institute of Technology<br />
                            2020100012</p>
                    </div>
                    <div className="third">
                        <p><strong>Jay Kolte</strong><br />
                            Electronics Enginnering <br />
                            Sardar Patel Institute of Technology<br />
                            2020100034</p>
                    </div>
                </div>


            </div>
        </>
    );
};

export default About;   