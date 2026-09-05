const search = document.querySelector('#search');
const cards = [...document.querySelectorAll('.repo-card')];
search.addEventListener('input', () => {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  for (const card of cards) {
    card.hidden = !card.dataset.search.toLocaleLowerCase().includes(query);
    if (!card.hidden) count++;
  }
  document.querySelectorAll('.repo-section').forEach(section => {
    section.hidden = ![...section.querySelectorAll('.repo-card')].some(card => !card.hidden);
  });
  document.querySelector('#result-count').textContent = `${count} ${count === 1 ? 'repository' : 'repositories'}`;
  document.querySelector('#empty').hidden = count !== 0;
});
const videos = [...document.querySelectorAll('video')];
videos.forEach(video => video.addEventListener('play', () => {
  videos.forEach(other => { if (other !== video) other.pause(); });
}));
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (!entry.isIntersecting) entry.target.pause();
  }), { threshold: 0.05 });
  videos.forEach(video => observer.observe(video));
}
