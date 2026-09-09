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

// Open & Scroll to Spec Explanation Card
window.openSpecModal = function(type) {
  let targetId = 'exp-domain';
  if (type === 'hosting') targetId = 'exp-hosting';
  else if (type === 'email') targetId = 'exp-email';
  else if (type === 'ssl') targetId = 'exp-ssl';
  else if (type === 'seo') targetId = 'exp-seo';
  else if (type === 'image' || type === 'setup') targetId = 'exp-image';
  
  const targetElement = document.getElementById(targetId) || document.getElementById('penjelasan-fitur');
  if (targetElement) {
    targetElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    targetElement.style.transition = 'all 0.5s ease';
    targetElement.style.borderColor = 'var(--accent-amber)';
    targetElement.style.boxShadow = '0 0 25px rgba(217, 119, 36, 0.4)';
    
    setTimeout(() => {
      targetElement.style.borderColor = '';
      targetElement.style.boxShadow = '';
    }, 2500);
  }
};

// FAQ Accordion Toggle
window.toggleFaq = function(buttonElement) {
  const faqItem = buttonElement.closest('.faq-item');
  if (!faqItem) return;

  const isActive = faqItem.classList.contains('active');

  // Close all other active FAQ items
  document.querySelectorAll('.faq-item').forEach(item => {
    item.classList.remove('active');
  });

  // Toggle clicked item
  if (!isActive) {
    faqItem.classList.add('active');
  }
};

// Interactive Price Calculator Logic
window.calculatePrice = function() {
  const calcType = document.getElementById('calcType');
  const calcPages = document.getElementById('calcPages');
  const featureWa = document.getElementById('featureWa');
  const featureMultiLang = document.getElementById('featureMultiLang');
  const featureSpeed = document.getElementById('featureSpeed');
  const totalPriceDisplay = document.getElementById('totalPriceDisplay');

  if (!calcType || !totalPriceDisplay) return;

  let total = parseInt(calcType.value) || 3000000;
  
  const pagesCount = Math.max(0, parseInt(calcPages.value) || 0);
  total += pagesCount * 100000;

  if (featureWa && featureWa.checked) total += parseInt(featureWa.value);
  if (featureMultiLang && featureMultiLang.checked) total += parseInt(featureMultiLang.value);
  if (featureSpeed && featureSpeed.checked) total += parseInt(featureSpeed.value);

  totalPriceDisplay.textContent = 'IDR ' + total.toLocaleString('id-ID');
};

// Send Calculator Result to WhatsApp
window.sendCalcToWa = function() {
  const calcType = document.getElementById('calcType');
  const calcPages = document.getElementById('calcPages');
  const totalPriceDisplay = document.getElementById('totalPriceDisplay');
  
  const selectedType = calcType.options[calcType.selectedIndex].text;
  const extraPages = calcPages.value || 0;
  const total = totalPriceDisplay.textContent;

  const msg = `Halo BRWNWEB, saya berminat membuat website dengan rincian kalkulasi berikut:\n\n` +
              `• Jenis Paket: ${selectedType}\n` +
              `• Halaman Tambahan: ${extraPages} Halaman\n` +
              `• Estimasi Total Biaya: ${total}\n\n` +
              `Mohon bantuan konsultasi pengerjaannya, terima kasih!`;

  const waUrl = `https://wa.me/6281285324814?text=${encodeURIComponent(msg)}`;
  window.open(waUrl, '_blank');
};

// Back to Top Scroll & Button Visibility
window.scrollToTop = function() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

window.addEventListener('scroll', () => {
  const btn = document.getElementById('backToTopBtn');
  if (btn) {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }
});

// Portfolio Filter Category Logic
window.filterPortfolio = function(category, btnElement) {
  const cards = document.querySelectorAll('.portfolio-card');
  const filterBtns = document.querySelectorAll('.filter-btn');

  filterBtns.forEach(btn => btn.classList.remove('active'));
  if (btnElement) btnElement.classList.add('active');

  cards.forEach(card => {
    const cardCat = card.getAttribute('data-category');
    if (category === 'all' || cardCat === category) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
};

// Live Demo Modal Handler
window.openDemoModal = function(title, category, imgSrc, desc, liveUrl) {
  const modal = document.getElementById('demoModal');
  if (!modal) return;

  const modalTitle = document.getElementById('modalTitle');
  const modalTag = document.getElementById('modalTag');
  const modalImg = document.getElementById('modalImg');
  const modalDesc = document.getElementById('modalDesc');

  if (modalTitle) modalTitle.textContent = title;
  if (modalTag) modalTag.textContent = category;
  if (modalImg) modalImg.src = imgSrc;
  if (modalDesc) modalDesc.textContent = desc;

  const liveBtn = document.getElementById('modalLiveBtn');
  if (liveBtn) liveBtn.href = liveUrl || '#';

  const waBtn = document.getElementById('modalWaBtn');
  if (waBtn) {
    const msg = `Halo BRWNWEB, saya tertarik ingin memesan model website seperti "${title}" (${category}). Mohon konsultasi pengerjaannya!`;
    waBtn.href = `https://wa.me/6281285324814?text=${encodeURIComponent(msg)}`;
  }

  modal.classList.add('active');
};

window.closeDemoModal = function() {
  const modal = document.getElementById('demoModal');
  if (modal) modal.classList.remove('active');
};

// Close Demo Modal on clicking overlay background
document.addEventListener('click', (e) => {
  const modal = document.getElementById('demoModal');
  if (modal && e.target === modal) {
    modal.classList.remove('active');
  }
});

// Lead Contact Form Submit Handler
window.handleFormSubmit = function(e) {
  e.preventDefault();
  const name = document.getElementById('formName').value;
  const phone = document.getElementById('formPhone').value;
  const pkg = document.getElementById('formPackage').value;
  const msg = document.getElementById('formMessage').value;

  const waMsg = `Halo BRWNWEB, saya ingin berkonsultasi mengenai pembuatan website dengan detail berikut:\n\n` +
                `• Nama: ${name}\n` +
                `• No. WA: ${phone}\n` +
                `• Paket Diminati: ${pkg}\n` +
                (msg ? `• Catatan: ${msg}\n\n` : `\n`) +
                `Mohon bantuan informasi pengerjaannya. Terima kasih!`;

  const waUrl = `https://wa.me/6281285324814?text=${encodeURIComponent(waMsg)}`;
  window.open(waUrl, '_blank');
};



