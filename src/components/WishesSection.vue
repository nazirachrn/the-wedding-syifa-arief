<template>
  <section id="wishes" class="relative py-24 bg-black text-[#F5F0E8] overflow-hidden">
    <!-- Background Photo: gallery-5.jpeg (portrait, baju hitam) - no zoom -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <img src="/assets/gallery-5.jpeg" alt="" class="absolute inset-0 w-full h-full object-cover opacity-40" style="filter: blur(40px); transform: scale(1.1);" />
      <img src="/assets/gallery-5.jpeg" alt="" class="opacity-85" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-height:100vh;width:100%;object-fit:contain;" />
    </div>
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.65) 100%);"></div>
    <div class="absolute inset-0 floral-overlay opacity-15 pointer-events-none"></div>
    <div class="absolute -right-20 bottom-10 w-80 h-80 rounded-full bg-[#FFFFFF]/5 blur-3xl pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-2xl mx-auto px-6">
      <!-- Section Header -->
      <div class="reveal reveal-up text-center mb-10 md:mb-12">
        <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-medium tracking-wide drop-shadow-lg">
          Doa &amp; Ucapan
        </h2>
        <p class="font-serif italic text-white/95 text-sm sm:text-base mt-2 drop-shadow-md">
          Untaian doa dan ucapan hangat dari para kerabat dan keluarga tercinta
        </p>
        <div class="flex items-center justify-center space-x-3 mt-4">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/50"></div>
          <span class="text-white text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/50"></div>
        </div>
      </div>

      <!-- Single Scrollable Wishes Card Container -->
      <div class="reveal reveal-up w-full mono-card p-6 sm:p-8 rounded-3xl relative shadow-2xl">
        <!-- Floating Heart Icon Accent -->
        <div class="absolute -top-5 right-8 sm:right-10 w-10 h-10 bg-white text-black rounded-full flex items-center justify-center shadow-lg border border-white/40">
          <Heart class="w-5 h-5 text-black fill-black/20" />
        </div>

        <div class="max-h-[480px] overflow-y-auto pr-2 wishes-scroll-container">
          <TransitionGroup name="list" tag="div" class="divide-y divide-white/15">
            <div 
              v-for="wish in wishes" 
              :key="wish.id"
              class="py-4 first:pt-0 last:pb-0 space-y-2.5 transition-all"
            >
              <!-- Top Row: Name and Attendance badge -->
              <div class="flex items-center justify-between">
                <h4 class="font-serif font-medium text-base text-white tracking-wide">{{ wish.name }}</h4>
                
                <span 
                  class="font-sans text-[10px] tracking-[0.15em] uppercase px-3 py-1 rounded-full font-semibold border"
                  :class="wish.attendance === 'Hadir'
                    ? 'bg-white/15 border-white/30 text-white'
                    : 'bg-neutral-800 border-neutral-700 text-neutral-400'"
                >
                  {{ wish.attendance }}
                </span>
              </div>

              <!-- Message Text -->
              <p class="font-sans text-sm text-neutral-200 leading-relaxed italic">
                "{{ wish.message }}"
              </p>

              <!-- Date timestamp -->
              <div class="flex items-center justify-end space-x-1.5 text-neutral-400 text-[10px] font-sans">
                <MessageSquare class="w-3.5 h-3.5 text-white/60" />
                <span>{{ formatRelativeTime(wish.timestamp) }}</span>
              </div>
            </div>
          </TransitionGroup>

          <!-- Empty State -->
          <div v-if="wishes.length === 0" class="text-center py-12 text-neutral-400 font-serif italic text-base">
            Belum ada ucapan. Jadilah yang pertama memberikan ucapan!
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { Heart, MessageSquare } from 'lucide-vue-next';
import { subscribeToWishes } from '../firebase';

const wishes = ref([]);
let unsubscribe = null;

onMounted(() => {
  unsubscribe = subscribeToWishes((updatedWishes) => {
    wishes.value = updatedWishes;
  });
});

onUnmounted(() => {
  if (unsubscribe) unsubscribe();
});

function formatRelativeTime(dateStr) {
  if (!dateStr) return 'Baru saja';
  
  const now = new Date();
  const date = new Date(dateStr);
  const diffMs = now - date;
  
  const diffSecs = Math.floor(diffMs / 1000);
  const diffMins = Math.floor(diffSecs / 60);
  const diffHours = Math.floor(diffMins / 60);
  const diffDays = Math.floor(diffHours / 24);

  if (diffSecs < 60) {
    return 'Baru saja';
  } else if (diffMins < 60) {
    return `${diffMins} menit yang lalu`;
  } else if (diffHours < 24) {
    return `${diffHours} jam yang lalu`;
  } else if (diffDays === 1) {
    return 'Kemarin';
  } else {
    return date.toLocaleDateString('id-ID', {
      day: 'numeric',
      month: 'short',
      year: 'numeric'
    });
  }
}
</script>

<style scoped>
.wishes-scroll-container::-webkit-scrollbar {
  width: 4px;
}
.wishes-scroll-container::-webkit-scrollbar-track {
  background: transparent;
}
.wishes-scroll-container::-webkit-scrollbar-thumb {
  background: rgba(201, 169, 110, 0.4);
  border-radius: 2px;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
.list-enter-from {
  opacity: 0;
  transform: translateY(30px);
}
.list-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}
.list-move {
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
</style>

