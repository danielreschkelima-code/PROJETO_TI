import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home.js';
import Company from './components/pages/company.js';
import Contact from './components/pages/contact.js';
import NewProject from './components/pages/NewProject.js';
import Projects from './components/pages/Projects.js';
import Project from './components/pages/Project.js';

import Container from './components/layout/Container.js';
import Navbar from './components/layout/Navbar.js';
import Footer from './components/layout/Footer.js';

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
              <Route path="/project/:id" element={<Project/>} />
        </Routes>
      </Container>
      

      <Footer/>
    </Router>
  );
}

export default App;
