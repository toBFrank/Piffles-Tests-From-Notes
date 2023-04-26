import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
`;

const Heading = styled.h1`
  font-size: 4rem;
  margin-bottom: 2rem;
`;

const Button = styled.button`
  background-color: #0077ff;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  font-size: 2rem;
  padding: 1rem 2rem;
`;

function LandingPage() {
  // return a heading: "Piffles?"
  // return a subheading: "Making tests has never been easier!"
  // return a button: "Upload your notes"
  return (
    <Container>
      <Heading>Piffles?</Heading>
      <h2>Making tests has never been easier!</h2>
      <Button>Upload your notes</Button>
    </Container>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
      </Routes>
    </Router>
  );
}

export default App;