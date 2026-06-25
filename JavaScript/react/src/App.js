import './App.css';
import HelloWorld from './components/HelloWorld';
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';
import Frase from './components/Frase.js';
import List from './components/List.js';
import Item from './components/Item.js';


function App() {

  let name = "Brandon"
  function sum(a, b) {
    return a + b
  }

  let url = "https://via.placeholder.com/150"

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

    </div>

  );
}

export default App;