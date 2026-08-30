<template>
  <section id="home" class="relative min-h-screen flex items-center justify-center bg-black text-[#F5F0E8] overflow-hidden py-20">
    <!-- Background Photo: bg-cover.jpeg (portrait, baju hitam) - no zoom -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <img src="/assets/bg-cover.jpeg" alt="" class="absolute inset-0 w-full h-full object-cover grayscale opacity-40" style="filter: blur(40px) grayscale(1); transform: scale(1.1);" />
      <img src="/assets/bg-cover.jpeg" alt="" class="grayscale opacity-85" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-height:100vh;width:100%;object-fit:contain;" />
    </div>
    <!-- cinematic gradient overlay -->
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.65) 100%);"></div>
    <div class="absolute inset-0 floral-overlay opacity-20"></div>



    <!-- Main Container -->
    <div class="relative z-20 w-full max-w-4xl px-6 text-center flex flex-col items-center">
      <!-- Elegantly animated top divider -->
      <div class="reveal reveal-up mb-6" style="transition-delay: 100ms">
        <span class="font-sans text-xs tracking-[0.4em] text-white uppercase font-semibold">
          THE WEDDING OF
        </span>
        <div class="flex items-center justify-center space-x-4 mt-3">
          <div class="h-[1px] w-14 bg-gradient-to-r from-transparent to-white/50"></div>
          <span class="text-white text-lg">⚜</span>
          <div class="h-[1px] w-14 bg-gradient-to-l from-transparent to-white/50"></div>
        </div>
      </div>

      <!-- Main Heading: Syifa & Arief -->
      <h2 class="reveal reveal-up font-display text-6xl md:text-8xl font-light text-white tracking-[0.12em] md:tracking-[0.16em] leading-none select-none drop-shadow-lg" style="transition-delay: 250ms">
        Syifa <span class="font-script text-5xl md:text-6xl text-white block md:inline my-2 md:my-0 md:mx-4">&</span> Arief
      </h2>

      <!-- Description Quote Wording Pill -->
      <div class="reveal reveal-up mt-6 max-w-lg" style="transition-delay: 400ms">
        <div class="bg-black/50 backdrop-blur-md border border-white/15 px-6 py-3.5 rounded-2xl shadow-xl">
          <p class="font-serif italic text-xs sm:text-sm text-neutral-200 leading-relaxed">
            "Dan di antara tanda-tanda kekuasaan-Nya ialah Dia menciptakan untukmu isteri-isteri dari jenismu sendiri..."
          </p>
        </div>
      </div>

      <!-- Elegantly Framed Countdown Timer -->
      <div class="reveal reveal-up w-full max-w-xl mt-10" style="transition-delay: 550ms">
        <div class="inline-block px-4 py-1 rounded-full bg-white/10 border border-white/20 mb-6">
          <p class="font-sans text-[11px] tracking-[0.3em] text-white uppercase font-semibold">
            Menuju Hari Bahagia
          </p>
        </div>

        <!-- Countdown Columns -->
        <div class="grid grid-cols-4 gap-3 sm:gap-4">
          <!-- Days -->
          <div class="mono-card p-3 sm:p-4 rounded-2xl flex flex-col items-center transition-all duration-300 hover:border-white/40 hover:scale-105">
            <span class="font-display text-3xl sm:text-4xl font-light text-white leading-none">{{ timeLeft.days }}</span>
            <span class="font-sans text-[10px] tracking-[0.2em] uppercase text-neutral-300 mt-2 font-medium">Hari</span>
          </div>

          <!-- Hours -->
          <div class="mono-card p-3 sm:p-4 rounded-2xl flex flex-col items-center transition-all duration-300 hover:border-white/40 hover:scale-105">
            <span class="font-display text-3xl sm:text-4xl font-light text-white leading-none">{{ timeLeft.hours }}</span>
            <span class="font-sans text-[10px] tracking-[0.2em] uppercase text-neutral-300 mt-2 font-medium">Jam</span>
          </div>

          <!-- Minutes -->
          <div class="mono-card p-3 sm:p-4 rounded-2xl flex flex-col items-center transition-all duration-300 hover:border-white/40 hover:scale-105">
            <span class="font-display text-3xl sm:text-4xl font-light text-white leading-none">{{ timeLeft.minutes }}</span>
            <span class="font-sans text-[10px] tracking-[0.2em] uppercase text-neutral-300 mt-2 font-medium">Menit</span>
          </div>

          <!-- Seconds -->
          <div class="mono-card p-3 sm:p-4 rounded-2xl flex flex-col items-center transition-all duration-300 hover:border-white/40 hover:scale-105">
            <span class="font-display text-3xl sm:text-4xl font-light text-white leading-none">{{ timeLeft.seconds }}</span>
            <span class="font-sans text-[10px] tracking-[0.2em] uppercase text-neutral-300 mt-2 font-medium">Detik</span>
          </div>
        </div>
      </div>

      <!-- Scroll indicator arrow -->
      <div class="reveal reveal-up mt-14 flex flex-col items-center space-y-2 pointer-events-none" style="transition-delay: 700ms">
        <span class="font-sans text-[10px] tracking-[0.3em] uppercase text-neutral-400 font-light">Scroll ke bawah</span>
        <div class="w-6 h-10 border border-white/30 rounded-full flex justify-center p-1 relative">
          <div class="w-1.5 h-1.5 bg-white rounded-full animate-bounce"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// Wedding date target: Sept 13, 2026 (Minggu) at 09:00 WIB
const targetDate = new Date('2026-09-13T09:00:00+07:00').getTime();

const timeLeft = ref({
  days: '00',
  hours: '00',
  minutes: '00',
  seconds: '00'
});

let timerInterval = null;

function updateCountdown() {
  const now = new Date().getTime();
  const diff = targetDate - now;

  if (diff <= 0) {
    timeLeft.value = { days: '00', hours: '00', minutes: '00', seconds: '00' };
    if (timerInterval) clearInterval(timerInterval);
    return;
  }

  const d = Math.floor(diff / (1000 * 60 * 60 * 24));
  const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const s = Math.floor((diff % (1000 * 60)) / 1000);

  timeLeft.value = {
    days: d.toString().padStart(2, '0'),
    hours: h.toString().padStart(2, '0'),
    minutes: m.toString().padStart(2, '0'),
    seconds: s.toString().padStart(2, '0')
  };
}



onMounted(() => {
  updateCountdown();
  timerInterval = setInterval(updateCountdown, 1000);
});

onUnmounted(() => {
  if (timerInterval) clearInterval(timerInterval);
});
</script>


