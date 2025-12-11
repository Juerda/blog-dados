// Comments System with Supabase (Open Source Postgres)
// Fill these with your project values from Supabase → Settings → API
const SUPABASE_URL = "YOUR_SUPABASE_URL"; // e.g. https://xyzcompany.supabase.co
const SUPABASE_ANON_KEY = "YOUR_SUPABASE_ANON_KEY"; // public anon key

let supabaseClient = null;

function initializeSupabase() {
  if (typeof window.supabase === 'undefined') {
    console.warn('Supabase JS não carregado. Inclua o script CDN no template: <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>');
    return;
  }
  if (!SUPABASE_URL || !SUPABASE_ANON_KEY || SUPABASE_URL.startsWith('YOUR_') || SUPABASE_ANON_KEY.startsWith('YOUR_')) {
    console.warn('Configuração do Supabase incompleta. Defina SUPABASE_URL e SUPABASE_ANON_KEY.');
    return;
  }
  supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  // Carregar comentários ao iniciar
  loadCommentsSupabase();
}

async function postCommentSupabase() {
  const textarea = document.getElementById('comment-text');
  const text = (textarea?.value || '').trim();
  if (!text) { alert('Escreva um comentário'); return; }

  const postSlug = document.body.getAttribute('data-post-slug');
  if (!postSlug) return;

  const profile = await supabaseClient.auth.getUser();
  const user = profile?.data?.user || null;
  const author = user?.user_metadata?.name || user?.email || 'Convidado';
  const email = user?.email || null;

  const { error } = await supabaseClient.from('comments').insert({
    post_slug: postSlug,
    author,
    email,
    text,
    inserted_at: new Date().toISOString(),
    likes: 0
  });
  if (error) { alert('Erro ao postar: ' + error.message); return; }
  if (textarea) textarea.value = '';
  await loadCommentsSupabase();
}

async function loadCommentsSupabase() {
  const postSlug = document.body.getAttribute('data-post-slug');
  if (!postSlug || !supabaseClient) return;

  const container = document.getElementById('comments-list');
  if (!container) return;

  const { data, error } = await supabaseClient
    .from('comments')
    .select('*')
    .eq('post_slug', postSlug)
    .order('inserted_at', { ascending: false });

  if (error) { console.error(error); return; }
  container.innerHTML = '';
  if (!data || data.length === 0) {
    container.innerHTML = '<p style="color: var(--text-secondary); text-align: center; padding: 20px;">Nenhum comentário ainda. Seja o primeiro!</p>';
    return;
  }

  data.forEach((comment) => {
    const el = createSupabaseCommentElement(comment);
    container.appendChild(el);
  });
}

async function likeCommentSupabase(id) {
  if (!supabaseClient) return;
  const { data, error } = await supabaseClient
    .from('comments')
    .update({ likes: window.Number((window.Number.isFinite ? 1 : 1)) })
    .eq('id', id);
  if (error) { console.error(error); return; }
  await loadCommentsSupabase();
}

function createSupabaseCommentElement(comment) {
  const div = document.createElement('div');
  div.className = 'comment-item';
  div.style.cssText = `
    padding: 20px;
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 15px;
    background: var(--bg-secondary);
  `;

  const date = new Date(comment.inserted_at);
  const dateStr = date.toLocaleDateString('pt-BR', {
    year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
  });

  div.innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
      <div>
        <strong style="color: var(--primary);">${escapeHtml(comment.author || 'Convidado')}</strong>
        <p style="margin:4px 0 0 0;font-size:0.9em;color:var(--text-secondary);">${dateStr}</p>
      </div>
    </div>
    <p style="margin:0;line-height:1.6;color:var(--text-primary);">${escapeHtml(comment.text)}</p>
    <div style="margin-top:12px;display:flex;gap:12px;">
      <button onclick="likeCommentSupabase('${comment.id}')" style="background:none;border:none;color:var(--primary);cursor:pointer;font-size:0.9em;">👍 ${comment.likes || 0}</button>
    </div>
  `;
  return div;
}

function escapeHtml(text) {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
  return String(text || '').replace(/[&<>"']/g, (m) => map[m]);
}

// Optionally call initializeSupabase on DOMContentLoaded when you switch to Supabase
// document.addEventListener('DOMContentLoaded', initializeSupabase);
