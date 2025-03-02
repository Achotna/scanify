// MAIN TITLE ANIMATION ---------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  // Main title
  const mainTitle1 = document.getElementById('main_title');
  const titleText1 = "Manage your expenses now";
  mainTitle1.innerHTML = `<span>${titleText1}</span>`;

  // h1 animation
  const mainTitle2 = document.getElementById('h1');
  const titleText2 = "Our features";
  mainTitle2.innerHTML = `<span>${titleText2}</span>`;
});
// DRAG AND DROP BOX ------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {
  let dropArea = document.getElementById("drop-area");
  let fileInput = document.getElementById("file-input");
  let fileLabel = document.getElementById("file-label");

  ["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
      dropArea.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
      e.preventDefault();
      e.stopPropagation();
  }

  ["dragenter", "dragover"].forEach(eventName => {
      dropArea.addEventListener(eventName, () => dropArea.classList.add("highlight"), false);
  });

  ["dragleave", "drop"].forEach(eventName => {
      dropArea.addEventListener(eventName, () => dropArea.classList.remove("highlight"), false);
  });

  dropArea.addEventListener("drop", (e) => {
      let files = e.dataTransfer.files;
      fileInput.files = files;
      fileLabel.innerText = files[0].name; 
  });

  dropArea.addEventListener("click", () => {
      fileInput.click();
  });

  fileInput.addEventListener("change", () => {
      if (fileInput.files.length > 0) {
          fileLabel.innerText = fileInput.files[0].name;
      }
  });
});

// SCROLLING ANIMATION ---------------------------------------------------------------------------------------

ScrollReveal().reveal('.card', {
  delay: 500,
  distance: '50px',
  origin: 'bottom',
  interval: 500,
  easing: 'ease-in-out',
  reset: true, 
});

AOS.init();

