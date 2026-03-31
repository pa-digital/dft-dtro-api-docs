function toggleAccordion(event, toggleEl) {
  event.preventDefault();
  event.stopPropagation();

  const section = toggleEl.closest(".toc-section");
  const container = toggleEl.closest(".toc-toggle");
  const subitems = section.querySelector(".toc-subitems");
  const text = container.querySelector(".icon-container");

  if (subitems) {
    const isOpen = subitems.classList.contains("expanded");
    subitems.classList.toggle("expanded");
    container.classList.toggle("expanded", !isOpen);
    section.classList.toggle("expanded");
    text.innerHTML = isOpen ? "+" : "-";
  }
}
