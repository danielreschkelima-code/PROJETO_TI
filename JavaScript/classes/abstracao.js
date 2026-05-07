console.log();

class Forma {
    constructor(cor){
        this.cor = cor;
    }
    calcularArea() {
        throw new Error("O método calcularArea() deve ser implementado.");
    }
    descrever() {
        console.log(`Forma de cor ${this.cor} com área:
${this.calcularArea().toFixed(2)}`);
    }
}

class Circulo extends Forma {
    constructor(cor, raio){
        super(cor);
        this.raio = raio;
    }
    calcularArea(){
        return Math.PI*this.raio**2;
    }
}

class Retangulo extends Forma {
    constructor (cor, largura, altura){
        super(cor);
        this.largura = largura;
        this.altura = altura;
    }
    calcularArea(){
        return this.largura*this.altura;
    }
}

const circulo1 = new Circulo("azul", 3);
const retangulo1 = new Retangulo("verde", 10, 10);

circulo1.descrever();
console.log();
retangulo1.descrever();

console.log();