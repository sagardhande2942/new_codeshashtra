import React from 'react'
import "./index.css";
import {Row,Container,Col} from "react-bootstrap";
import workerImg from "../../assets/images/jay-ee-qcBayvKvghM-unsplash.jpg";
import contractorImg from "../../assets/images/contractor.png";
import ownerImg from "../../assets/images/owner.png";

import ConstructionIcon from '@mui/icons-material/Construction';

const Index = () => {
    const val = "Worker";
  return (
      <>

        <div className="hamburgerCircle">
            <ConstructionIcon className="icon"/>
        </div>
        <div className="section">
            <div className="verticalCenter">
            <Container  >
                <Row>
                    <Col lg={7} md={6} sm={6} xs={12}>
                        <div className="flexColCenter">
                         
                            {
                                val=="Worker" && (
                                    <div>
                                        <h2>“Use the best possible materials, and reveal the quality of those materials and the craftsmanship of their assembly.”</h2>  
                                        <p>– Karl Friedrich Schinkel</p>                                 
                                   </div>
                                )
                            }
                            {
                                val=="Contractor" && (
                                    <div>
                                    <h2>“It is not the beauty of the building you should look at: it’s the construction of the foundation that will stand the test of time.”</h2>  
                                    <p>– David Allen Coe</p>                                 
                               </div> 
                                )
                            }
                            {
                                val=="Owner" && (
                                    <div>
                                    <h2>“It is not the beauty of the building you should look at: it’s the construction of the foundation that will stand the test of time.”</h2>  
                                    <p>– David Allen Coe</p>                                 
                               </div>
                                )
                            }
                        </div>
                    </Col>
                    <Col lg={5} md={6} sm={6} xs={12}>
                          
                            {
                                val=="Worker" && (
                                    <div className="imgContainer">
                                        <img src={workerImg} ></img>
                                    </div> 
                                 )
                            }
                            {
                                val=="Contractor" && (
                                    <div className="imgContainer">
                                        <img src={contractorImg} ></img>
                                    </div> 
                                 )
                            }
                            {
                                val=="Owner" && (
                                    <div className="imgContainer">
                                        <img src={ownerImg} ></img>
                                    </div> 
                                 )
                            }
                    </Col>

                </Row>
            </Container>
            </div>
        </div>
        
    </>
  )
}

export default Index
