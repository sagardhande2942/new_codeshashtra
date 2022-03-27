import React, { useState } from "react";
import axios from "../../helpers/axios";
import { getData } from "../../actions";
import { useDispatch, useSelector } from "react-redux";
import bgVideo from "../../assets/videos/pexels-richard-he-5567711.mp4"

import "./index.css";
function HomePage() {
  const [data, setdata] = useState([]);

  const auth = useSelector((state) => state.auth);
  const dispatch = useDispatch();
   
  const fetchData = () => {
    dispatch(getData());
    console.log(auth.dataa);
  }

  return (
    <>
      <div className="bgVideo">
        <video loop autoPlay muted>
          <source
            src={bgVideo}
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>
        
    </div>
    <div className="btnOption">
          <div className="">
            <button className="btn">Owner</button>
            <button className="btn centerBtn">Contractor</button>
            <button className="btn">Worker</button>
          </div>
        </div>
    </>
  );
}

export default HomePage;
