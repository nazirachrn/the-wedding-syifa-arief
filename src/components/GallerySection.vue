<template>
  <section id="gallery" class="relative py-20 md:py-28 bg-[#0A0A0A] text-[#F8F9FA] overflow-hidden border-t border-b border-white/10">
    <!-- Subtle Background Ornaments -->
    <div class="absolute inset-0 floral-overlay opacity-15 pointer-events-none"></div>
    <div class="absolute left-1/4 top-1/4 w-96 h-96 rounded-full bg-white/[0.03] blur-3xl pointer-events-none"></div>
    <div class="absolute right-1/4 bottom-1/4 w-96 h-96 rounded-full bg-white/[0.03] blur-3xl pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-6xl mx-auto px-4 sm:px-6 md:px-8">
      <!-- Section Header -->
      <div class="reveal reveal-up text-center mb-10 md:mb-14">
        <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-medium tracking-wide drop-shadow-lg">
          Galeri Foto
        </h2>
        <div class="flex items-center justify-center space-x-3 mt-4">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/50"></div>
          <span class="text-white text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/50"></div>
        </div>
      </div>

      <!-- Symmetrical & Face-Optimized Grid for 11 Photos -->
      <!-- Luxury Staggered Scroll Reveal with Soft Zoom & Dissolve -->
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3.5 sm:gap-4 md:gap-5">
        <div 
          v-for="(img, idx) in galleryImages" 
          :key="idx" 
          :class="[
            'reveal reveal-up relative group overflow-hidden rounded-2xl md:rounded-3xl cursor-pointer border border-white/10 hover:border-white/30 shadow-2xl bg-neutral-900/90 transform-gpu',
            img.gridClass
          ]"
          :style="{ transitionDelay: `${(idx % 4) * 120}ms` }"
          @click="openLightbox(idx)"
        >
          <!-- Skeleton Loading Pulse Background -->
          <div 
            v-if="!loadedImages[idx]" 
            class="absolute inset-0 bg-gradient-to-br from-neutral-900 via-neutral-800 to-neutral-900 animate-pulse pointer-events-none"
          ></div>

          <!-- Photo Image with Smooth Dissolve & Face-Focused Positioning -->
          <img 
            :src="img.src" 
            :alt="img.alt" 
            :class="[
              'w-full h-full object-cover transition-all duration-700 ease-out transform-gpu group-hover:scale-105',
              loadedImages[idx] ? 'opacity-100 scale-100' : 'opacity-0 scale-102',
              img.objectPosition || 'object-[center_25%]'
            ]" 
            loading="eager"
            decoding="async"
            @load="onImageLoad(idx)"
          />

          <!-- Gradient Hover Overlay -->
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-between p-3.5 sm:p-4 md:p-5">
            <div class="flex justify-end">
              <span class="w-8 h-8 md:w-9 md:h-9 rounded-full bg-white/20 backdrop-blur-md border border-white/30 text-white flex items-center justify-center transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
                <Maximize2 class="w-4 h-4" />
              </span>
            </div>
            <div class="transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
              <span class="text-xs font-serif text-white/90 italic tracking-wider">Foto #{{ idx + 1 }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Lightbox Modal -->
    <Transition name="fade">
      <div 
        v-if="isLightboxOpen" 
        class="fixed inset-0 z-50 flex flex-col items-center justify-between bg-black/96 p-4 md:p-8 select-none"
        @click.self="closeLightbox"
      >
        <!-- Header Controls -->
        <div class="w-full max-w-6xl flex justify-between items-center z-50 pt-2 px-2">
          <div class="text-xs md:text-sm font-sans tracking-widest text-white/80 font-light flex items-center space-x-2">
            <span class="text-white font-medium">{{ activeImageIndex + 1 }}</span>
            <span>/</span>
            <span>{{ galleryImages.length }}</span>
          </div>
          <button 
            @click="closeLightbox" 
            class="w-10 h-10 md:w-12 md:h-12 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 text-white flex items-center justify-center cursor-pointer transition-all duration-200 focus:outline-none"
            aria-label="Tutup"
          >
            <X class="w-5 h-5 md:w-6 md:h-6" />
          </button>
        </div>

        <!-- Main Lightbox Display (With Touch Swipe Support) -->
        <div 
          class="relative w-full max-w-5xl flex-1 flex items-center justify-center my-4 overflow-hidden touch-pan-y"
          @touchstart="handleTouchStart"
          @touchend="handleTouchEnd"
        >
          <!-- Navigation Prev -->
          <button 
            @click="prevImage" 
            @touchstart.prevent="prevImage"
            class="absolute left-2 md:left-4 z-50 w-11 h-11 md:w-12 md:h-12 rounded-full bg-black/70 hover:bg-white/20 border border-white/30 text-white flex items-center justify-center cursor-pointer transition-all duration-100 active:scale-90 focus:outline-none shadow-lg"
            aria-label="Sebelumnya"
          >
            <ChevronLeft class="w-6 h-6 text-white" />
          </button>

          <!-- Main Image Container with Ultra-Responsive Fluid Directional Slide Transition -->
          <div class="relative w-full h-full flex items-center justify-center overflow-hidden">
            <Transition :name="slideDirection === 'next' ? 'slide-next' : 'slide-prev'">
              <img 
                :key="activeImageIndex"
                :src="galleryImages[activeImageIndex].src" 
                :alt="galleryImages[activeImageIndex].alt" 
                class="max-w-full max-h-[68vh] md:max-h-[74vh] object-contain rounded-xl shadow-2xl border border-white/10 transform-gpu select-none"
              />
            </Transition>
          </div>

          <!-- Navigation Next -->
          <button 
            @click="nextImage" 
            @touchstart.prevent="nextImage"
            class="absolute right-2 md:right-4 z-50 w-11 h-11 md:w-12 md:h-12 rounded-full bg-black/70 hover:bg-white/20 border border-white/30 text-white flex items-center justify-center cursor-pointer transition-all duration-100 active:scale-90 focus:outline-none shadow-lg"
            aria-label="Selanjutnya"
          >
            <ChevronRight class="w-6 h-6 text-white" />
          </button>
        </div>

        <!-- Thumbnail Strip Navigation -->
        <div class="w-full max-w-4xl overflow-x-auto py-2 px-4 flex justify-start md:justify-center items-center space-x-2 md:space-x-3 scrollbar-none z-50">
          <button
            v-for="(img, idx) in galleryImages"
            :key="'thumb-' + idx"
            @click="selectImage(idx)"
            @touchstart.passive="selectImage(idx)"
            :class="[
              'relative shrink-0 rounded-lg overflow-hidden border transition-all duration-150 active:scale-95 cursor-pointer bg-neutral-900',
              img.gridClass.includes('lg:col-span-4') ? 'w-16 h-10 md:w-20 md:h-12' : 'w-10 h-14 md:w-12 md:h-16',
              activeImageIndex === idx ? 'border-white scale-105 opacity-100 ring-2 ring-white/50' : 'border-transparent opacity-40 hover:opacity-80'
            ]"
          >
            <img :src="img.src" :alt="img.alt" class="w-full h-full object-cover" />
          </button>
        </div>
      </div>
    </Transition>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { X, ChevronLeft, ChevronRight, Maximize2 } from 'lucide-vue-next';

const loadedImages = ref({});

function onImageLoad(index) {
  loadedImages.value[index] = true;
}

const galleryImages = [
  // 1. Top Hero Banner: True Landscape Photo (YDS04858.jpg) for 100% full face & scenery framing
  { 
    id: 1, 
    src: '/assets/galeri/YDS04858.jpg', 
    alt: 'Galeri Foto 1', 
    gridClass: 'col-span-2 md:col-span-3 lg:col-span-4 aspect-[16/9] md:aspect-[21/9]',
    objectPosition: 'object-[center_35%]'
  },

  // 2-5. Grid Row 1 (Portrait Photos in Portrait Slots -> Full Face Visibility with object-top)
  { id: 2, src: '/assets/galeri/YDS04716.jpg', alt: 'Galeri Foto 2', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-top' },
  { id: 3, src: '/assets/galeri/Edit 1.jpg', alt: 'Galeri Foto 3', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-top' },
  { id: 4, src: '/assets/galeri/Edit 2.jpg', alt: 'Galeri Foto 4', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-top' },
  { id: 5, src: '/assets/galeri/YDS04933(2).jpg', alt: 'Galeri Foto 5', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-top' },

  // 6-9. Grid Row 2
  { id: 6, src: '/assets/galeri/YDS05147.jpg', alt: 'Galeri Foto 6', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-top' },
  { id: 7, src: '/assets/galeri/Edit 3.jpg', alt: 'Galeri Foto 7', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-center' },
  { id: 8, src: '/assets/galeri/Edit 4.jpg', alt: 'Galeri Foto 8', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-center' },
  { id: 9, src: '/assets/galeri/YDS05386(1).jpg', alt: 'Galeri Foto 9', gridClass: 'col-span-1 aspect-[3/4]', objectPosition: 'object-top' },

  // 10-11. Closing Items (Landscape photos side-by-side)
  { 
    id: 10, 
    src: '/assets/galeri/YDS05364.jpg', 
    alt: 'Galeri Foto 10', 
    gridClass: 'col-span-1 md:col-span-3 lg:col-span-2 aspect-[4/3] md:aspect-[16/10]',
    objectPosition: 'object-center'
  },
  { 
    id: 11, 
    src: '/assets/galeri/YDS05318.jpg', 
    alt: 'Galeri Foto 11', 
    gridClass: 'col-span-1 md:col-span-3 lg:col-span-2 aspect-[4/3] md:aspect-[16/10]',
    objectPosition: 'object-center'
  },
];

const isLightboxOpen = ref(false);
const activeImageIndex = ref(0);
const slideDirection = ref('next');

// Mobile Touch Swipe Variables
let touchStartX = 0;
let touchStartY = 0;

function handleTouchStart(e) {
  if (e.touches && e.touches.length > 0) {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
  }
}

function handleTouchEnd(e) {
  if (!e.changedTouches || e.changedTouches.length === 0) return;
  const touchEndX = e.changedTouches[0].clientX;
  const touchEndY = e.changedTouches[0].clientY;
  const deltaX = touchEndX - touchStartX;
  const deltaY = touchEndY - touchStartY;

  // Ensure horizontal swipe is dominant
  if (Math.abs(deltaX) > 35 && Math.abs(deltaX) > Math.abs(deltaY)) {
    if (deltaX < 0) {
      nextImage();
    } else {
      prevImage();
    }
  }
}

// Preload ALL gallery images in background memory for 0ms loading delay on mobile
function preloadAllImages() {
  galleryImages.forEach((img) => {
    const i = new Image();
    i.src = img.src;
  });
}

function openLightbox(index) {
  slideDirection.value = 'next';
  activeImageIndex.value = index;
  isLightboxOpen.value = true;
  document.body.style.overflow = 'hidden';
  preloadAllImages();
}

function closeLightbox() {
  isLightboxOpen.value = false;
  document.body.style.overflow = '';
}

function selectImage(index) {
  slideDirection.value = index >= activeImageIndex.value ? 'next' : 'prev';
  activeImageIndex.value = index;
}

function nextImage() {
  slideDirection.value = 'next';
  activeImageIndex.value = (activeImageIndex.value + 1) % galleryImages.length;
}

function prevImage() {
  slideDirection.value = 'prev';
  activeImageIndex.value = (activeImageIndex.value - 1 + galleryImages.length) % galleryImages.length;
}

function handleKeyDown(e) {
  if (!isLightboxOpen.value) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowRight') nextImage();
  if (e.key === 'ArrowLeft') prevImage();
}

onMounted(() => {
  window.addEventListener('keydown', handleKeyDown);
  preloadAllImages();
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyDown);
  document.body.style.overflow = '';
});
</script>

<style scoped>
/* Instant & Crisp Lightbox Open/Close Modal Transition (120ms) */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.12s ease-out, transform 0.12s ease-out;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scale(0.97);
}

/* Rich, Fluid & Clearly Visible Directional Slide + Soft Zoom Animations (180ms cubic-bezier) */
.slide-next-enter-active,
.slide-next-leave-active,
.slide-prev-enter-active,
.slide-prev-leave-active {
  transition: opacity 0.18s cubic-bezier(0.22, 1, 0.36, 1), transform 0.18s cubic-bezier(0.22, 1, 0.36, 1);
  will-change: transform, opacity;
}

.slide-next-leave-active,
.slide-prev-leave-active {
  position: absolute;
}

/* Next Slide (Slides gracefully from right +45px, Exits to left -45px) */
.slide-next-enter-from {
  opacity: 0;
  transform: translate3d(45px, 0, 0) scale(0.93);
}
.slide-next-leave-to {
  opacity: 0;
  transform: translate3d(-45px, 0, 0) scale(0.93);
}

/* Prev Slide (Slides gracefully from left -45px, Exits to right +45px) */
.slide-prev-enter-from {
  opacity: 0;
  transform: translate3d(-45px, 0, 0) scale(0.93);
}
.slide-prev-leave-to {
  opacity: 0;
  transform: translate3d(45px, 0, 0) scale(0.93);
}

/* Hide scrollbar for thumbnail strip */
.scrollbar-none::-webkit-scrollbar {
  display: none;
}
.scrollbar-none {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
