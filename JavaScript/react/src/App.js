import logo from './logo.svg';
import './App.css';

function App() {

  let name = "Brandon"

  function sum(a, b) {
    return a + b
  }

  let url = "https://via.placeholder.com/150"

  return ( //aqui começa o JSX
    <div className="App">
      <h2>Alterando o JSX</h2>
      <p>Olá, {name}!</p>
      <p>Soma 1+2: {sum(1, 2)}</p>
      <img src={url} alt="Imagem qualquer"/>
    </div>
  );
}

export default App;