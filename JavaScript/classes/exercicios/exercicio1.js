/* Crie uma classe Veiculo com os atributos marca, modelo e velocidadeAtual,
e métodos acelerar(valor) e frear(valor).
Em seguida, crie as subclasses Carro e Moto, cada uma adicionando pelo menos um atributo específco.
*/
console.log();

class Veiculo{
    constructor(marca, modelo, velocidadeAtual){
        this.marca = marca;
        this.modelo = modelo;
        this.velocidadeAtual = velocidadeAtual;
    }
    acelerar(valor, mostrar=false){
        this.velocidadeAtual += valor;
        if (mostrar){
            console.log(`
Acelerando ${valor}.
`)
        }
    }
    frear(valor, mostrar=false){
        this.velocidadeAtual -= valor;
        if (mostrar){
            console.log(`
Freando ${valor}.
`)
        }
    }
    apresentar(){
        console.log(`Marca: ${this.marca}
Modelo: ${this.modelo}
Velocidade atual: ${this.velocidadeAtual}`)
    }
}

class Carro extends Veiculo{
    constructor(marca, modelo, velocidadeAtual, automatico){
        super(marca, modelo, velocidadeAtual);
        this.automatico = automatico;
    }
    apresentar(){
        super.apresentar();
        console.log(`Automático: ${this.automatico? "Sim" : "Não"}`);
    }
}

class Moto extends Veiculo{
    constructor(marca, modelo, velocidadeAtual, motorEletrico){
        super(marca, modelo, velocidadeAtual);
        this.motorEletrico = motorEletrico;
    }
    apresentar(){
        super.apresentar();
        console.log(`Motor elétrico: ${this.motorEletrico? "Sim" : "Não"}`);
    }
}

const Moto1 = new Moto("Chevrolet", "Turbo", 40, false);
Moto1.apresentar();
console.log();
Moto1.acelerar(40, true); // diz que está acelerando
Moto1.frear(20); // não diz que está freando (valor mostrar permanece sendo false)
Moto1.apresentar();

console.log();