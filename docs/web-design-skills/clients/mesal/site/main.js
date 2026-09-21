(() => {
  const root = document.querySelector("[data-slider]");
  if (!root) return;

  const track = root.querySelector("[data-track]");
  const cards = track ? Array.from(track.children) : [];
  const prev = root.querySelector("[data-prev]");
  const next = root.querySelector("[data-next]");
  if (!track || cards.length === 0) return;

  let index = 0;

  const go = (dir) => {
    index = (index + dir + cards.length) % cards.length;
    track.scrollTo({
      left: cards[index].offsetLeft,
      behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
        ? "auto"
        : "smooth",
    });
  };

  prev?.addEventListener("click", () => go(-1));
  next?.addEventListener("click", () => go(1));
})();
