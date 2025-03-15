// MAIN TITLE ANIMATION ---------------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', () => {
    const mainTitle1 = document.getElementById('main_title');
    const titleText1 = "Prenez le contrôle de vos dépenses dès maintenant";
    mainTitle1.innerHTML = `<span>${titleText1}</span>`;
  
    const mainTitle2 = document.getElementById('h1');
    const titleText2 = "Nos fonctionnalités";
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
  
  // PARTICLES ------------------------------------------------------------------------------------------------

particlesJS.load('particles-js', 'static/particlesjs-config.json', function() {
    console.log('Particles are loaded');
});

  
  particlesJS("particles-js", {
    "particles": {
      "number": {
        "value": 62,
        "density": {
          "enable": true,
          "value_area": 473.02197975465907
        }
      },
      "color": {
        "value": "#ffffff"
      },
      "shape": {
        "type": "circle",
        "stroke": {
          "width": 0,
          "color": "#000000"
        },
        "polygon": {
          "nb_sides": 5
        },
        "image": {
          "src": "img/github.svg",
          "width": 100,
          "height": 100
        }
      },
      "opacity": {
        "value": 0.5,
        "random": false,
        "anim": {
          "enable": false,
          "speed": 1,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 3,
        "random": true,
        "anim": {
          "enable": false,
          "speed": 40,
          "size_min": 0.1,
          "sync": false
        }
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#ffffff",
        "opacity": 0.4,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 1.5,
        "direction": "none",
        "random": false,
        "straight": false,
        "out_mode": "bounce",
        "bounce": false,
        "attract": {
          "enable": false,
          "rotateX": 600,
          "rotateY": 800
        }
      }
    },
    "interactivity": {
      "detect_on": "window",
      "events": {
        "onhover": {
          "enable": false,
          "mode": "grab"
        },
        "onclick": {
          "enable": true,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 400,
          "line_linked": {
            "opacity": 1
          }
        },
        "bubble": {
          "distance": 400,
          "size": 40,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "repulse": {
          "distance": 200,
          "duration": 0.4
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": true
  });
   
// ---------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("jsPieChart").getContext("2d");

  new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Alimentation", "Transport", "Entretien", "Multimédia"],
      datasets: [{
        data: [300, 70, 80, 250],
        backgroundColor: ["#6a7998", "#3f4d58", "#B1B3B5", "#919191"]
      }]
    },
    options: {
      animation: {
        animateRotate: true, 
        duration: 2000
      },
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true, 
          text: 'Répartition des dépenses', 
          font: {
            size: 20,
            weight: 'bold',
          },
          color: 'white', 
          padding: {
            top: 5, 
            bottom: 10 
          },
          align: 'center', 
        },
        legend: {
          labels: {
            color: 'white', 
            font: {
              size: 14, 
            }
          }
        }
      }
    }
  });
});

console.log(typeof Chart);

// Animated bubble notif ------------------------------------------------------------------------------//

document.getElementById('upload-button').addEventListener('click', function (event) {
  event.preventDefault(); 

  const sumElement = document.getElementById('sum-value');
  const notificationBubble = document.getElementById('notification-bubble');
  const addedValue = document.getElementById('added-value');

  const previousSum = parseFloat(sumElement.textContent);
  const addedAmount = parseFloat(addedValue.textContent);

  if (addedAmount > 0) {
    const newTotal = previousSum + addedAmount;

    notificationBubble.textContent = `+${addedAmount} €`;

    notificationBubble.style.display = 'block'; 
    notificationBubble.style.visibility = 'visible';
    notificationBubble.style.opacity = 1;

    setTimeout(() => {
      sumElement.textContent = `${newTotal} €`;
    }, 2000);
    
    setTimeout(() => {
      notificationBubble.style.opacity = 0;
      notificationBubble.style.visibility = 'hidden';
      notificationBubble.style.display = 'none';
    }, 2000);
  }
});
// --------------------------------------------------------------------

function showSidebar(){
  const sidebar=document.querySelector('.sidebar')
  sidebar.style.display = 'flex'
}

function hideSidebar(){
  const sidebar=document.querySelector('.sidebar')
  sidebar.style.display = 'none'
}

// ---------------------------------------------------------------------
document.getElementById('analyzebtn').addEventListener('click', function () {
  const button = this;
  const form = document.getElementById('uploadForm');
  const formData = new FormData(form);

  document.getElementById('loader').style.display = 'block';

  button.disabled = true;
  document.getElementById('content').style.display = 'none';

  fetch('/your-api-endpoint', {
    method: 'POST',
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error:', error);
    })
    .finally(() => {
      document.getElementById('loader').style.display = 'none';
      document.getElementById('content').style.display = 'block';
      button.disabled = false;
    });
});