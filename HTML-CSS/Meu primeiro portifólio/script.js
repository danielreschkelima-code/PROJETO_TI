document.addEventListener('DOMContentLoaded', () => {
    const botaoMenu = document.querySelector('.menu-hamburguer');
    const listaLinks = document.querySelector('.menu-links');

    botaoMenu.addEventListener('click', () => {
        listaLinks.classList.toggle('ativo');
    });
});