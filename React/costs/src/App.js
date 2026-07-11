import { BrowserRouter as Router, Link, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Company from './components/pages/company';
import Contact from './components/pages/contact';
import NewProject from './components/pages/NewProject';
import Projects from './components/pages/Projects';

import Container from './components/layout/Container';
import Navbar from './components/layout/Navbar';
import Footer from './components/layout/Footer';

function App() {
  return (
    <Router>
      <Navbar/>

      <Container customClass="min-height">
        <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/projects" element={<Projects/>} />
              <Route path="/company" element={<Company/>} />
              <Route path="/contact" element={<Contact/>} />
              <Route path="/newproject" element={<NewProject/>} />
        </Routes>
      </Container>
      

      <Footer/>
    </Router>
  );
}

export default App;
