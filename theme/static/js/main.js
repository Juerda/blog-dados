// Theme toggle (dark/light mode) with custom SVG icons
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
                <svg class="theme-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                    <!-- Sun Icon for Light Theme -->
                    <g class="sun-icon" opacity="1" style="transition: opacity 0.3s ease;">
                        <circle cx="50" cy="50" r="25" fill="currentColor"/>
                        <line x1="50" y1="10" x2="50" y2="20" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        <line x1="50" y1="80" x2="50" y2="90" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        <line x1="10" y1="50" x2="20" y2="50" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        <line x1="80" y1="50" x2="90" y2="50" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        <line x1="22" y1="22" x2="29" y2="29" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        <line x1="71" y1="71" x2="78" y2="78" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        <line x1="78" y1="22" x2="71" y2="29" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                        <line x1="29" y1="71" x2="22" y2="78" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                    </g>
                    <!-- Moon Icon for Dark Theme -->
                    <g class="moon-icon" opacity="0" style="transition: opacity 0.3s ease;">
                        <path d="M 65 20 A 35 35 0 1 0 70 70 A 30 30 0 0 1 65 20" fill="currentColor"/>
                        <circle cx="70" cy="35" r="6" fill="white" opacity="0.4"/>
                        <circle cx="55" cy="50" r="4" fill="white" opacity="0.6"/>
                        <circle cx="75" cy="60" r="5" fill="white" opacity="0.5"/>
                    </g>
                </svg>
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
    const sunIcon = document.querySelector('.sun-icon');
    const moonIcon = document.querySelector('.moon-icon');
    
    if (sunIcon && moonIcon) {
        if (theme === 'light') {
            sunIcon.style.opacity = '1';
            moonIcon.style.opacity = '0';
        } else {
            sunIcon.style.opacity = '0';
            moonIcon.style.opacity = '1';
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

