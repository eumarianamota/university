const card = document.querySelector('.card');
const card_container = document.querySelector('.card_container');

card_container.addEventListener('click', () => {
  card.classList.toggle('flipped')
});