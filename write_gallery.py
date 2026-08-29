# Generator for GallerySection.vue
import sys
sys.stdout.reconfigure(encoding='utf-8')

T = chr(96)  # backtick not used but just in case
SQ = chr(39)
DQ = chr(34)

def attr(name, val):
    return f'{name}={DQ}{val}{DQ}'

def cls(val):
    return attr('class', val)

parts = []

def ln(s=''):
    parts.append(s)

# ===== TEMPLATE =====
ln('<template>')
ln('  <section id="gallery" class="relative py-24 bg-[#E9EFE9] text-[#2C2A29] overflow-hidden">')
ln('    <div class="absolute inset-0 floral-overlay opacity-15 pointer-events-none"></div>')
ln('    <div class="relative z-10 w-full max-w-5xl mx-auto px-6">')
ln('      <!-- Section Header -->')
ln('      <div class="reveal reveal-up text-center mb-16">')
ln('        <h2 class="font-display text-4xl md:text-5xl font-light text-[#5C775C] tracking-wide">Galeri Bahagia</h2>')
ln('        <p class="font-serif italic text-[#465E46] text-sm md:text-base mt-2">Momen-momen indah perjalanan kasih kami</p>')
ln('        <div class="h-[1px] w-20 bg-[#769376]/35 mx-auto mt-4"></div>')
ln('      </div>')
ln()
ln('      <!-- Desktop Collage -->')
ln('      <div class="reveal reveal-up hidden md:grid grid-cols-3 grid-rows-2 gap-4 h-[600px]">')

desktop_items = [
    (0, 'col-span-1 row-span-2', True),
    (1, 'col-span-1 row-span-1', False),
    (3, 'col-span-1 row-span-1', False),
    (4, 'col-span-1 row-span-1', False),
    (2, 'col-span-1 row-span-1', False),
]
for idx, span, mono in desktop_items:
    extra = ' grayscale' if mono else ''
    ln(f'        <div class="{span} relative rounded-3xl overflow-hidden shadow-md border border-[#769376]/15 group cursor-zoom-in bg-white" @click="openSlideshow({idx})">')
    ln(f'          <img :src="galleryImages[{idx}].src" :alt="galleryImages[{idx}].alt" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105{extra}" />')
    ln('          <div class="absolute inset-0 bg-[#1F2E1F]/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-10"></div>')
    if mono:
        ln('          <div class="mono-badge">MONO</div>')
    ln('        </div>')
ln('      </div>')
ln()

ln('      <!-- Mobile Collage -->')
ln('      <div class="reveal reveal-up grid grid-cols-2 gap-3 md:hidden">')
mobile_items = [
    (0, 'col-span-2 h-[280px]', True),
    (1, 'col-span-1 h-[140px]', False),
    (3, 'col-span-1 h-[140px]', False),
    (2, 'col-span-1 h-[180px]', False),
    (4, 'col-span-1 h-[180px]', False),
]
for idx, span, mono in mobile_items:
    extra = ' grayscale' if mono else ''
    ln(f'        <div class="{span} relative rounded-2xl overflow-hidden shadow-md border border-[#769376]/15 group cursor-zoom-in bg-white" @click="openSlideshow({idx})">')
    ln(f'          <img :src="galleryImages[{idx}].src" :alt="galleryImages[{idx}].alt" class="w-full h-full object-cover{extra}" />')
    if mono:
        ln('          <div class="mono-badge">MONO</div>')
    ln('        </div>')
ln('      </div>')
ln('    </div>')
ln()

# Slideshow
ln('    <!-- Full-Screen Slideshow -->')
ln('    <Transition name="slideshow-fade">')
ln('      <div')
ln('        v-if="slideshow.isOpen"')
ln('        class="slideshow-overlay"')
ln('        @keydown.esc="closeSlideshow"')
ln('        @keydown.left="prevSlide"')
ln('        @keydown.right="nextSlide"')
ln('        tabindex="0"')
ln('        ref="slideshowRef"')
ln('      >')
ln("        <div class=\"slideshow-bg\" :class=\"isMono ? 'bg-mono' : 'bg-color'\"></div>")
ln('        <button @click="closeSlideshow" class="slideshow-close" aria-label="Tutup"><X class="w-6 h-6" /></button>')
ln('        <div class="slideshow-dots">')
ln("          <button v-for=\"(img, idx) in galleryImages\" :key=\"img.id\" @click=\"goToSlide(idx)\" class=\"dot\" :class=\"{ 'dot-active': slideshow.currentIndex === idx }\"></button>")
ln('        </div>')
ln('        <div class="slideshow-content">')
ln('          <button @click="prevSlide" class="nav-btn" aria-label="Sebelumnya"><ChevronLeft class="w-8 h-8" /></button>')
ln('          <div class="photo-page">')
ln('            <Transition :name="transitionName" mode="out-in">')
ln('              <div :key="slideshow.currentIndex" class="photo-frame">')
ln("                <div class=\"photo-img-wrap\" :class=\"isMono ? 'frame-mono' : 'frame-color'\">")
ln('                  <img :src="currentSlide.src" :alt="currentSlide.alt" class="photo-img" :class="{ grayscale: isMono }" />')
ln('                  <div v-if="isMono" class="mono-strip"><span>MONOCHROME</span></div>')
ln('                </div>')
ln('                <div class="photo-info">')
ln('                  <div class="photo-counter">')
ln('                    <span class="counter-num">{{ slideshow.currentIndex + 1 }}</span>')
ln('                    <span class="counter-sep"> / </span>')
ln('                    <span class="counter-total">{{ galleryImages.length }}</span>')
ln('                  </div>')
ln('                  <h3 class="photo-title">{{ currentSlide.title }}</h3>')
ln('                  <p class="photo-caption">{{ currentSlide.caption }}</p>')
ln("                  <div class=\"photo-divider\" :class=\"isMono ? 'divider-mono' : 'divider-color'\"></div>")
ln("                  <p class=\"photo-tag\" :class=\"isMono ? 'tag-mono' : 'tag-color'\">{{ currentSlide.tag }}</p>")
ln('                </div>')
ln('              </div>')
ln('            </Transition>')
ln('          </div>')
ln('          <button @click="nextSlide" class="nav-btn" aria-label="Selanjutnya"><ChevronRight class="w-8 h-8" /></button>')
ln('        </div>')
ln('        <div class="filmstrip">')
ln("          <button v-for=\"(img, idx) in galleryImages\" :key=\"img.id\" @click=\"goToSlide(idx)\" class=\"filmstrip-thumb\" :class=\"{ 'filmstrip-active': slideshow.currentIndex === idx }\">")
ln('            <img :src="img.src" :alt="img.alt" :class="{ grayscale: idx === 0 }" class="filmstrip-img" />')
ln('          </button>')
ln('        </div>')
ln('      </div>')
ln('    </Transition>')
ln('  </section>')
ln('</template>')
ln()

# Script
ln('<script setup>')
ln("import { ref, computed, nextTick } from 'vue';")
ln("import { X, ChevronLeft, ChevronRight } from 'lucide-vue-next';")
ln()
ln('const galleryImages = [')
images = [
    (1, '/assets/gallery-1.jpeg?v=2', 'Foto Pernikahan 1', 'Awal Perjalanan', 'Saat dua hati bertemu dan dunia terasa lebih indah', '\u2726 Monochrome Moment \u2726'),
    (2, '/assets/gallery-2.jpeg?v=2', 'Foto Pernikahan 2', 'Kebersamaan', 'Setiap detik bersamamu adalah kenangan yang tak terlupakan', '\u2726 Warna Kasih \u2726'),
    (3, '/assets/gallery-3.jpeg?v=2', 'Foto Pernikahan 3', 'Senyum Bahagia', 'Senyummu adalah alasan terindah di setiap hariku', '\u2726 Warna Kasih \u2726'),
    (4, '/assets/gallery-4.jpeg?v=2', 'Foto Pernikahan 4', 'Cinta Sejati', 'Dalam peluk dan tawa, kita menemukan rumah satu sama lain', '\u2726 Warna Kasih \u2726'),
    (5, '/assets/gallery-5.jpeg?v=2', 'Foto Pernikahan 5', 'Selamanya', 'Dan di sinilah kisah kita dimulai, untuk selamanya bersama', '\u2726 Warna Kasih \u2726'),
]
for id_, src, alt, title, caption, tag in images:
    ln(f"  {{ id: {id_}, src: '{src}', alt: '{alt}', title: '{title}', caption: '{caption}', tag: '{tag}' }},")
ln('];')
ln()
ln("const slideshow = ref({ isOpen: false, currentIndex: 0 });")
ln("const slideshowRef = ref(null);")
ln("const direction = ref('next');")
ln()
ln("const isMono = computed(() => slideshow.value.currentIndex === 0);")
ln("const transitionName = computed(() => direction.value === 'next' ? 'slide-next' : 'slide-prev');")
ln("const currentSlide = computed(() => galleryImages[slideshow.value.currentIndex]);")
ln()
ln("function openSlideshow(index) {")
ln("  slideshow.value.currentIndex = index;")
ln("  slideshow.value.isOpen = true;")
ln("  nextTick(() => { slideshowRef.value?.focus(); });")
ln("}")
ln("function closeSlideshow() { slideshow.value.isOpen = false; }")
ln("function goToSlide(index) {")
ln("  direction.value = index > slideshow.value.currentIndex ? 'next' : 'prev';")
ln("  slideshow.value.currentIndex = index;")
ln("}")
ln("function nextSlide() {")
ln("  direction.value = 'next';")
ln("  slideshow.value.currentIndex = (slideshow.value.currentIndex + 1) % galleryImages.length;")
ln("}")
ln("function prevSlide() {")
ln("  direction.value = 'prev';")
ln("  slideshow.value.currentIndex = (slideshow.value.currentIndex - 1 + galleryImages.length) % galleryImages.length;")
ln("}")
ln('</script>')
ln()

# Style
ln('<style scoped>')
css_rules = [
    ".mono-badge { position:absolute;top:10px;left:10px;background:rgba(0,0,0,0.55);color:#fff;font-size:9px;font-family:monospace;letter-spacing:2px;padding:3px 8px;border-radius:4px;z-index:20; }",
    ".slideshow-overlay { position:fixed;inset:0;z-index:999;display:flex;flex-direction:column;align-items:center;justify-content:center;outline:none; }",
    ".slideshow-bg { position:absolute;inset:0;transition:background 0.8s ease; }",
    ".bg-mono { background:linear-gradient(135deg,#111 0%,#2a2a2a 50%,#111 100%); }",
    ".bg-color { background:linear-gradient(135deg,#1F2E1F 0%,#2d4a2d 50%,#1b3a2b 100%); }",
    ".slideshow-close { position:absolute;top:20px;right:20px;z-index:60;color:rgba(255,255,255,0.8);background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);border-radius:50%;width:44px;height:44px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background 0.25s,color 0.25s; }",
    ".slideshow-close:hover { background:rgba(255,255,255,0.18);color:#fff; }",
    ".slideshow-dots { position:absolute;top:28px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:60; }",
    ".dot { width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.3);border:none;cursor:pointer;transition:background 0.3s,transform 0.3s; }",
    ".dot-active { background:rgba(255,255,255,0.95);transform:scale(1.35); }",
    ".slideshow-content { position:relative;z-index:10;display:flex;align-items:center;width:100%;max-width:900px;padding:0 16px; }",
    ".nav-btn { flex-shrink:0;color:rgba(255,255,255,0.75);background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:50%;width:52px;height:52px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background 0.25s,color 0.25s,transform 0.25s;z-index:20; }",
    ".nav-btn:hover { background:rgba(255,255,255,0.16);color:#fff;transform:scale(1.08); }",
    ".photo-page { flex:1;display:flex;justify-content:center;overflow:hidden; }",
    ".photo-frame { display:flex;flex-direction:column;align-items:center;width:100%;max-width:560px; }",
    ".photo-img-wrap { position:relative;width:100%;border-radius:20px;overflow:hidden;max-height:52vh; }",
    ".frame-mono { border:2px solid rgba(255,255,255,0.15);box-shadow:0 0 0 1px rgba(255,255,255,0.05),0 30px 80px rgba(0,0,0,0.7); }",
    ".frame-color { border:2px solid rgba(118,147,118,0.35);box-shadow:0 0 0 1px rgba(118,147,118,0.1),0 30px 80px rgba(0,0,0,0.55); }",
    ".photo-img { width:100%;height:100%;object-fit:cover;max-height:52vh;display:block;transition:filter 0.6s ease; }",
    ".mono-strip { position:absolute;bottom:0;left:0;right:0;background:linear-gradient(to top,rgba(0,0,0,0.65) 0%,transparent 100%);padding:16px 16px 12px;display:flex;justify-content:center; }",
    ".mono-strip span { font-family:monospace;font-size:10px;letter-spacing:4px;color:rgba(255,255,255,0.6);text-transform:uppercase; }",
    ".photo-info { margin-top:20px;text-align:center;width:100%;padding:0 8px; }",
    ".photo-counter { display:flex;align-items:baseline;justify-content:center;gap:2px;margin-bottom:10px; }",
    ".counter-num { font-size:28px;font-weight:300;color:rgba(255,255,255,0.9);line-height:1;font-family:Georgia,serif; }",
    ".counter-sep { font-size:16px;color:rgba(255,255,255,0.35); }",
    ".counter-total { font-size:16px;color:rgba(255,255,255,0.5);font-family:Georgia,serif; }",
    ".photo-title { font-family:Georgia,serif;font-size:1.45rem;font-weight:400;color:#fff;letter-spacing:0.5px;margin-bottom:6px; }",
    ".photo-caption { font-family:Georgia,serif;font-style:italic;font-size:0.875rem;color:rgba(255,255,255,0.6);line-height:1.6;margin-bottom:12px; }",
    ".photo-divider { height:1px;width:40px;margin:0 auto 10px;border-radius:2px; }",
    ".divider-mono { background:rgba(255,255,255,0.25); }",
    ".divider-color { background:rgba(118,147,118,0.6); }",
    ".photo-tag { font-size:0.7rem;letter-spacing:2px;text-transform:uppercase; }",
    ".tag-mono { color:rgba(255,255,255,0.35); }",
    ".tag-color { color:rgba(150,200,150,0.7); }",
    ".filmstrip { position:absolute;bottom:20px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:20; }",
    ".filmstrip-thumb { width:52px;height:36px;border-radius:6px;overflow:hidden;cursor:pointer;border:2px solid rgba(255,255,255,0.15);transition:border-color 0.25s,transform 0.25s,opacity 0.25s;opacity:0.5;flex-shrink:0;background:none;padding:0; }",
    ".filmstrip-thumb:hover { opacity:0.8;transform:translateY(-2px); }",
    ".filmstrip-active { border-color:rgba(255,255,255,0.75)!important;opacity:1!important;transform:translateY(-3px) scale(1.05); }",
    ".filmstrip-img { width:100%;height:100%;object-fit:cover;display:block; }",
    ".slideshow-fade-enter-active,.slideshow-fade-leave-active { transition:opacity 0.45s ease; }",
    ".slideshow-fade-enter-from,.slideshow-fade-leave-to { opacity:0; }",
    ".slide-next-enter-active { transition:all 0.45s cubic-bezier(0.25,0.8,0.25,1); }",
    ".slide-next-leave-active { transition:all 0.35s cubic-bezier(0.55,0,0.55,0.2); }",
    ".slide-next-enter-from { opacity:0;transform:translateX(60px) scale(0.97); }",
    ".slide-next-leave-to { opacity:0;transform:translateX(-60px) scale(0.97); }",
    ".slide-prev-enter-active { transition:all 0.45s cubic-bezier(0.25,0.8,0.25,1); }",
    ".slide-prev-leave-active { transition:all 0.35s cubic-bezier(0.55,0,0.55,0.2); }",
    ".slide-prev-enter-from { opacity:0;transform:translateX(-60px) scale(0.97); }",
    ".slide-prev-leave-to { opacity:0;transform:translateX(60px) scale(0.97); }",
    "@media (max-width:640px) {",
    "  .slideshow-content { padding:0 4px; }",
    "  .nav-btn { width:40px;height:40px; }",
    "  .photo-title { font-size:1.15rem; }",
    "  .photo-caption { font-size:0.8rem; }",
    "  .filmstrip-thumb { width:40px;height:28px; }",
    "  .photo-img,.photo-img-wrap { max-height:42vh; }",
    "}",
]
for r in css_rules:
    ln(r)
ln('</style>')

content = '\n'.join(parts) + '\n'
with open(r'src\components\GallerySection.vue', 'w', encoding='utf-8') as f:
    f.write(content)
print('SUCCESS! Written', len(content), 'chars,', len(parts), 'lines')