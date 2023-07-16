const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;

let theme = prefersDarkScheme ? "dark" : "light"


const switchButton = document.getElementById("theme-toggle");

const checkbox = document.getElementById("theme-toggle-checkbox");

if (document.readyState !== 'loading') {
  setTheme(theme);
} else {
  document.addEventListener('DOMContentLoaded', () => setTheme(theme));
}

switchButton.addEventListener("click", (e) => {
  e.preventDefault()
  toggleTheme()
});

function toggleTheme() {
  theme = theme === "light" ? "dark" : "light";
  setTheme(theme);
}

function setTheme(mode) {
  if (mode === 'light') {
    document.documentElement.dataset.theme = "light"
    checkbox.checked = false;
    for (let source of document.querySelectorAll("picture > source")) {
      source.media = "none"
    }
  } else {
    document.documentElement.dataset.theme = "dark"
    checkbox.checked = true;
    for (let source of document.querySelectorAll("picture > source")) {
      source.media = "all"
    }
  }
}
