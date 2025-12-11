// Comments System with Firebase
// Initialize Firebase (configure with your project)
const FIREBASE_CONFIG = {
    // Required keys: replace with your Firebase Web App credentials
    apiKey: "BPXt-MgkkVGVLbuquldNnGn5R5BCU7RwXLR8kzoFTZtrJ6uy0Xnq0KliN89sR-860LeImAsLu7MG-xshGkxlOhg",
    appId: "YOUR_APP_ID",
    measurementId: "YOUR_MEASUREMENT_ID",

    // Pre-filled based on project info provided
    projectId: "jordan-arruda-site",
    authDomain: "jordan-arruda-site.firebaseapp.com",
    databaseURL: "https://jordan-arruda-site-default-rtdb.firebaseio.com",
    storageBucket: "jordan-arruda-site.appspot.com",
    messagingSenderId: "568760583710"
};

// Validate Firebase config and guide the user if incomplete
function validateFirebaseConfig() {
    const required = ["apiKey", "appId", "projectId", "authDomain", "databaseURL"];
    const missing = required.filter(k => !FIREBASE_CONFIG[k] || String(FIREBASE_CONFIG[k]).startsWith("YOUR_"));
    if (missing.length) {
        console.warn(
            "Configuração do Firebase incompleta. Campos faltando:", missing.join(", "),
            "\nComo resolver: Firebase Console → Project Settings → General → suas apps (Web) → copie o SDK Config e substitua os valores em FIREBASE_CONFIG."
        );
        return false;
    }
    return true;
}

// Firebase initialization
let firebaseInitialized = false;
let currentUser = null;

// Initialize Firebase when DOM is ready
function initializeFirebase() {
    if (typeof firebase !== 'undefined' && !firebaseInitialized) {
        try {
            if (!validateFirebaseConfig()) return;
            firebase.initializeApp(FIREBASE_CONFIG);
            firebaseInitialized = true;
            
            // Check auth state
            firebase.auth().onAuthStateChanged(function(user) {
                currentUser = user;
                updateAuthUI();
                if (user) {
                    loadComments();
                }
            });
        } catch (e) {
            console.warn('Firebase não disponível para comentários:', e?.message || e);
        }
    }
}

// Update authentication UI
function updateAuthUI() {
    const authSection = document.getElementById('auth-section');
    const commentsSection = document.getElementById('comments-section');
    const loginForm = document.getElementById('login-form');
    const commentForm = document.getElementById('comment-form');
    
    if (currentUser) {
        if (authSection) authSection.style.display = 'none';
        if (commentForm) commentForm.style.display = 'block';
        if (commentsSection) commentsSection.style.display = 'block';
        updateUserInfo();
    } else {
        if (authSection) authSection.style.display = 'block';
        if (commentForm) commentForm.style.display = 'none';
    }
}

// Update user info display
function updateUserInfo() {
    const userNameEl = document.getElementById('user-name');
    const userEmailEl = document.getElementById('user-email');
    
    if (userNameEl) userNameEl.textContent = currentUser.displayName || 'Usuário';
    if (userEmailEl) userEmailEl.textContent = currentUser.email;
}

// Sign up
function signUp(email, password, name) {
    if (!firebaseInitialized || typeof firebase === 'undefined') {
        alert('Sistema de comentários não disponível');
        return;
    }
    
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then(function(result) {
            return result.user.updateProfile({
                displayName: name
            });
        })
        .then(function() {
            alert('Cadastro realizado com sucesso!');
            document.getElementById('signup-form').reset();
        })
        .catch(function(error) {
            alert('Erro: ' + error.message);
        });
}

// Sign in with Google
function signInWithGoogle() {
    if (!firebaseInitialized || typeof firebase === 'undefined') {
        alert('Sistema de comentários não disponível');
        return;
    }
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
        .then(function() {
            // Carregar comentários após login
            loadComments();
        })
        .catch(function(error) {
            alert('Erro ao fazer login com Google: ' + error.message);
        });
}

// Sign out
function signOut() {
    if (firebaseInitialized && typeof firebase !== 'undefined') {
        firebase.auth().signOut();
    }
}

// Post comment
function postComment() {
    if (!currentUser || !firebaseInitialized) return;
    
    const textarea = document.getElementById('comment-text');
    const text = textarea.value.trim();
    
    if (!text) {
        alert('Escreva um comentário');
        return;
    }
    
    const postSlug = document.body.getAttribute('data-post-slug');
    if (!postSlug) return;
    
    // Get current timestamp
    const timestamp = new Date().toISOString();
    
    // Save comment to Firebase
    const commentRef = firebase.database().ref('comments/' + postSlug).push();
    commentRef.set({
        author: currentUser.displayName || currentUser.email,
        email: currentUser.email,
        text: text,
        timestamp: timestamp,
        likes: 0
    }).then(function() {
        textarea.value = '';
        loadComments();
    }).catch(function(error) {
        alert('Erro ao postar comentário: ' + error.message);
    });
}

// Load comments
function loadComments() {
    const postSlug = document.body.getAttribute('data-post-slug');
    if (!postSlug || !firebaseInitialized) return;
    
    const commentsContainer = document.getElementById('comments-list');
    if (!commentsContainer) return;
    
    firebase.database().ref('comments/' + postSlug)
        .orderByChild('timestamp')
        .on('value', function(snapshot) {
            commentsContainer.innerHTML = '';
            
            const comments = [];
            snapshot.forEach(function(childSnapshot) {
                comments.push({
                    id: childSnapshot.key,
                    ...childSnapshot.val()
                });
            });
            
            // Reverse to show newest first
            comments.reverse();
            
            if (comments.length === 0) {
                commentsContainer.innerHTML = '<p style="color: var(--text-secondary); text-align: center; padding: 20px;">Nenhum comentário ainda. Seja o primeiro!</p>';
                return;
            }
            
            comments.forEach(function(comment) {
                const commentEl = createCommentElement(comment);
                commentsContainer.appendChild(commentEl);
            });
        });
}

// Create comment element
function createCommentElement(comment) {
    const div = document.createElement('div');
    div.className = 'comment-item';
    div.style.cssText = `
        padding: 20px;
        border: 1px solid var(--border);
        border-radius: 8px;
        margin-bottom: 15px;
        background: var(--bg-secondary);
    `;
    
    const date = new Date(comment.timestamp);
    const dateStr = date.toLocaleDateString('pt-BR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
    
    div.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <div>
                <strong style="color: var(--primary);">${escapeHtml(comment.author)}</strong>
                <p style="margin: 4px 0 0 0; font-size: 0.9em; color: var(--text-secondary);">${dateStr}</p>
            </div>
        </div>
        <p style="margin: 0; line-height: 1.6; color: var(--text-primary);">${escapeHtml(comment.text)}</p>
        <div style="margin-top: 12px; display: flex; gap: 12px;">
            <button onclick="likeComment('${comment.id}')" style="background: none; border: none; color: var(--primary); cursor: pointer; font-size: 0.9em;">
                👍 ${comment.likes || 0}
            </button>
        </div>
    `;
    
    return div;
}

// Like comment
function likeComment(commentId) {
    if (!firebaseInitialized) return;
    
    const postSlug = document.body.getAttribute('data-post-slug');
    const likeRef = firebase.database().ref('comments/' + postSlug + '/' + commentId + '/likes');
    
    likeRef.transaction(function(currentValue) {
        return (currentValue || 0) + 1;
    });
}

// Escape HTML
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Share on social media
function shareOnSocial(platform) {
    const url = window.location.href;
    const title = document.querySelector('h1.article-title')?.textContent || 'Confira este artigo';
    
    let shareUrl = '';
    
    switch(platform) {
        case 'facebook':
            shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
            break;
        case 'twitter':
            shareUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`;
            break;
        case 'linkedin':
            shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`;
            break;
        case 'whatsapp':
            shareUrl = `https://wa.me/?text=${encodeURIComponent(title + ' ' + url)}`;
            break;
        case 'telegram':
            shareUrl = `https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`;
            break;
    }
    
    if (shareUrl) {
        window.open(shareUrl, '_blank', 'width=600,height=400');
    }
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', initializeFirebase);
