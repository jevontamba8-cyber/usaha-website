// BRWNWEB Script

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
});

// Navbar Scroll & Mobile Drawer
function initNavbar() {
  const navbar = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });

    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('active');
      });
    });
  }
}

// Toggle WhatsApp Dropdown Menu
window.toggleWaDropdown = function() {
  const menu = document.getElementById('waDropdownMenu');
  if (menu) {
    menu.classList.toggle('active');
  }
};

// Open WhatsApp Contact Selector / Scroll to Kontak
window.openWaSelector = function() {
  const menu = document.getElementById('waDropdownMenu');
  if (menu) {
    menu.classList.add('active');
  }
  const kontakSection = document.getElementById('kontak');
  if (kontakSection) {
    kontakSection.scrollIntoView({ behavior: 'smooth' });
  }
};

// Close WhatsApp Dropdown when clicking outside
document.addEventListener('click', (e) => {
  const menu = document.getElementById('waDropdownMenu');
  const btn = document.querySelector('.floating-wa-btn');
  if (menu && menu.classList.contains('active')) {
    if (!menu.contains(e.target) && !btn.contains(e.target)) {
      menu.classList.remove('active');
    }
  }
});

// Copy Phone Number to Clipboard
window.copyNumber = function(number, btnElement) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(number).then(() => {
      showCopiedFeedback(btnElement);
    }).catch(() => {
      fallbackCopy(number, btnElement);
    });
  } else {
    fallbackCopy(number, btnElement);
  }
};

function showCopiedFeedback(btnElement) {
  const originalHtml = btnElement.innerHTML;
  btnElement.innerHTML = '<i class="fa-solid fa-check"></i> Nomor Disalin!';
  btnElement.style.background = '#25D366';
  btnElement.style.color = '#FFFFFF';
  btnElement.style.borderColor = '#25D366';

  setTimeout(() => {
    btnElement.innerHTML = originalHtml;
    btnElement.style.background = '';
    btnElement.style.color = '';
    btnElement.style.borderColor = '';
  }, 2000);
}

function fallbackCopy(number, btnElement) {
  const tempInput = document.createElement('input');
  tempInput.value = number;
  document.body.appendChild(tempInput);
  tempInput.select();
  document.execCommand('copy');
  document.body.removeChild(tempInput);
  showCopiedFeedback(btnElement);
}
