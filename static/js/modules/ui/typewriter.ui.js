export function animateTyping() {
  const description = document.getElementById('typewriter-text');
  if (!description) return;

  const text = description.textContent;
  description.textContent = '';

  let i = 0;
  const typing = setInterval(() => {
      if (i < text.length) {
          description.textContent += text[i];
          i++;
      } else {
          clearInterval(typing);
      }
  }, 20);
}