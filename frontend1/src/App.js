import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./App.css";
import styled from "styled-components";
import HomePage from "./containers/HomePage";
import NavBar from "./containers/NavBar/navbar";
import { AccountBox } from "./components/accountBox";
import Index from "./containers/IndexPage/Index";


const AppContainer = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

function App() {
  return (
    <div className="App">
      {/* <AppContainer>
      <AccountBox />
    </AppContainer> */}
       <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/index" element={<Index />} />
          <Route exact path="/nav" element={<NavBar />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
