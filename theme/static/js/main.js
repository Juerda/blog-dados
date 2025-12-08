// Theme toggle (dark/light mode)
function initThemeToggle() {
    // Check for saved theme preference or default to light mode
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    // Create theme toggle button if it doesn't exist
    const navbar = document.querySelector('.navbar-menu');
    if (navbar && !document.getElementById('themeToggleBtn')) {
        const themeBtn = document.createElement('li');
        themeBtn.innerHTML = `
            <button id="themeToggleBtn" class="theme-toggle-btn" title="Alternar tema" aria-label="Alternar tema escuro/claro">
                <i class="fas fa-moon"></i>
            </button>
        `;
        navbar.appendChild(themeBtn);
        
        const themeBtnElement = document.getElementById('themeToggleBtn');
        themeBtnElement.addEventListener('click', toggleTheme);
        updateThemeIcon(savedTheme);
    }
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
        const icon = themeBtn.querySelector('i');
        if (icon) {
            icon.classList.remove('fa-moon', 'fa-sun');
            icon.classList.add(theme === 'light' ? 'fa-moon' : 'fa-sun');
        }
    }
}

// Menu mobile
document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme toggle
    initThemeToggle();
    
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navbarMenu = document.getElementById('navbarMenu');

    if (mobileMenuBtn && navbarMenu) {
        // Toggle menu
        mobileMenuBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            mobileMenuBtn.classList.toggle('active');
            navbarMenu.classList.toggle('active');
        });

        // Close menu when clicking on a link
        const navLinks = navbarMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenuBtn.classList.remove('active');
                navbarMenu.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navbarMenu.contains(event.target) || mobileMenuBtn.contains(event.target);
            
            if (!isClickInsideNav && navbarMenu.classList.contains('active')) {
                mobileMenuBtn.classList.remove('active');
                navbarMenu.classList.remove('active');
            }
        });
    }

    // Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            const element = document.querySelector(href);
            
            if (element) {
                e.preventDefault();
                element.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Highlight active link
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === '/' && href === '/')) {
            link.style.borderBottomColor = 'var(--secondary)';
        }
    });
});

// Lazy loading for images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                }
                observer.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

