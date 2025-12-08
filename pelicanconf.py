# pelicanconf.py

# --- Metadados e Informações do Site ---
AUTHOR = 'Jordan Arruda'
SITENAME = 'Data Insights'
SITEURL = ''  # Deixar vazio para desenvolvimento, Vercel preencherá em produção
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt_BR'
DEFAULT_DATE_FORMAT = '%d de %B de %Y'

# --- Configurações de URL ---
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Home como index
INDEX_SAVE_AS = 'index.html'

# --- Estrutura de Pastas ---
PATH = 'content' 
OUTPUT_PATH = 'output/'
STATIC_PATHS = ['images']

# --- Aparência e Menu ---
THEME = 'theme' 
DIRECT_TEMPLATES = ['index', 'tags', 'categories']
PAGINATED_TEMPLATES = {'archives': None}
ARCHIVES_SAVE_AS = 'blog.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# --- Configurações de Conteúdo ---
PLUGIN_PATHS = ['plugins']
PLUGINS = []

# Feed RSS/Atom
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Cache
LOAD_CONTENT_CACHE = False
