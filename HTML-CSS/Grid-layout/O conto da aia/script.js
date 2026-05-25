const hamburger = document.getElementById('hamburger');
// Seleciona todos os elementos com a classe .menuitens
const menuItens = document.querySelectorAll('.menuitens');

hamburger.addEventListener('click', () => {
    // Passa por cada item da lista e alterna a classe 'active'
    menuItens.forEach(item => {
        item.classList.toggle('active');
    });
});