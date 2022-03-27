import Button from 'react-bootstrap/Button';
import "./navbar.css";
import React, { useState } from "react";
import attendence from '../../assets/images/attendance.jpg';
import profile from '../../assets/images/profile.jpg';
import newSite from '../../assets/images/new_site.jpg';
import report from '../../assets/images/report.jpg';
import safetyViolation from '../../assets/images/safety_violations.jpg';

function NavBar() {
    const images = [
        attendence,
        profile,
        newSite,
        report,
        safetyViolation,    
    ];
    
    const [hoverImg, setHoverImg] = useState(images[0]);
       
    return (
        <>
            <div className='navdivs'>
                <div className='block left'>
                    <img src= {hoverImg} />
                </div>
                <div className='block right'>
                <Button className="btn-right" size="lg" 
                onMouseEnter={() => setHoverImg(images[0])}
                onMouseLeave={() => setHoverImg(images[0])}>
                        Update Attendance
                    </Button>
                    <Button className="btn-right" size="lg" 
                    onMouseEnter={() => setHoverImg(images[1])}
                    onMouseLeave={() => setHoverImg(images[0])}>
                        Edit Worker Profile
                    </Button>
                    <Button className="btn-right" size="lg" 
                    onMouseEnter={() => setHoverImg(images[2])}
                onMouseLeave={() => setHoverImg(images[0])}>
                        Add New Site
                    </Button>
                    <br></br>
                    <Button className="btn-right" size="lg" 
                    onMouseEnter={() => setHoverImg(images[3])}
                onMouseLeave={() => setHoverImg(images[0])}>
                        Create Report
                    </Button>
                    <Button className="btn-right" size="lg" 
                    onMouseHover={() => setHoverImg(images[4])}
                onMouseLeave={() => setHoverImg(images[0])}>
                        Safety Violations
                    </Button>
                </div>
            </div>
        </>
    );
}

export default NavBar;