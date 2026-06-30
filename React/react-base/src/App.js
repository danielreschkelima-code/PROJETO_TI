import './App.css';
import HelloWorld from './components/HelloWorld';
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';
import Frase from './components/Frase.js';
import List from './components/List.js';
import Item from './components/Item.js';
import Evento from './components/Evento.js';
import Form from './components/Form.js';
import Condicional from './components/Condicional.js';
import OutraLista from './components/OutraLista.js';
import SeuNome from './components/SeuNome.js';
import { useState } from 'react';
import Saudacao from './components/Saudacao.js';
import {BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';
import Home from './pages/Home.js';
import Contato from './pages/Contato.js';
import Empresa from './pages/Empresa.js';
import NavBar from './components/layout/NavBar.js';
import Footer from './components/layout/Footer.js';

function App() {

  // ALTERANDO JSX
  let name = "Brandon"
  function sum(a, b) {
    return a + b
  }
  let url = "https://via.placeholder.com/150"

  // RENDERIZAÇÃO DE LISTAS
  const lista = ["React", "Vue", "Angular"];
  const listaVazia = [];

  //STATE LIFT
  const [nome, setNome] = useState();

  return ( //aqui começa o JSX
    
    <div className="App">  
      
      <section id="INICIO">
        <h1>INÍCIO DOS ESTUDOS DE REACT</h1>
        <p className="subtitulo">Variáveis, JSX e funções</p>
          <h2>Alterando o JSX COM VARIÁVEIS</h2>
            <p>Olá, {name}!</p>
            <img src={url} alt="Imagem qualquer"/>
          <h2>Função em JSX</h2>
            <p>Soma 1+2: {sum(1, 2)}</p>
      </section>    

      <section id="COMPONENTES">
        <h1>COMPONENTES</h1>
        <p className="subtitulo">Componentes, props, e inserção de args com chaves</p>      
          <h2>COMPONENTE SIMPLES</h2>
            <HelloWorld/>
          <h2>PROPS</h2>
            <SayMyName nome="Daniel"/>
            <SayMyName nome={name}/>
            <h3>Types em Prop</h3>
              <ul> <Item marca="Sansumg" ano_lancamento="2000"/> </ul>
              <ul> <Item/></ul>
          <h2>ARGS</h2>
            <Pessoa nome={name} foto={url} idade="16" profissao="LEM"/> 
      </section>

      <section id="CSS MODULES">
        <h1>CSS MODULES</h1>
          <Frase/>
      </section>

      <section id="FRAGMENTOS">
        <h1>FRAGMENTOS</h1>
          <List />
      </section>

      <section id="EVENTOS">
        <h1>EVENTOS</h1>
          <Evento numero="1"/>
          <Evento numero="2"/>
          <Form/>
      </section>

      <section id="RENDERICACAO CONDICIONAL">
        <h1>RENDERICAÇÃO CONDICIONAL</h1>
          <Condicional />
      </section>

      <section id="RENDERICACAO DE LISTAS">
        <h1>RENDERICAÇÃO DE LISTAS</h1>
          <OutraLista itens={lista}/>
          <OutraLista itens={listaVazia}/>
      </section>

      <section id="STATE LIFT">
        <h1>STATE LIFT</h1>
          <SeuNome setNome={setNome}/>
          <p>{nome}</p>
          <Saudacao nome={nome}/>
      </section>

      <section id="ROUTER">
        <Router>
          <h1>ROUTER</h1>
            <NavBar />
            <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/empresa" element={<Empresa/>} />
              <Route path="/contato" element={<Contato/>} />
            </Routes>
            <Footer />
        </Router>
      </section>

    </div>

  );
}

export default App;