<template>
  <section id="gift" class="relative py-24 bg-black text-[#F5F0E8] overflow-hidden">
    <!-- Background Photo: gallery-4.jpeg (portrait, baju merah) - no zoom -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <img src="/assets/gallery-4.jpeg" alt="" class="absolute inset-0 w-full h-full object-cover opacity-40" style="filter: blur(40px); transform: scale(1.1);" />
      <img src="/assets/gallery-4.jpeg" alt="" class="opacity-85" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-height:100vh;width:100%;object-fit:contain;" />
    </div>
    <!-- cinematic gradient overlay -->
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.65) 100%);"></div>
    <div class="absolute inset-0 floral-overlay opacity-20 pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-lg mx-auto px-6">
      <!-- Section Header -->
      <div class="reveal reveal-up text-center mb-12">
        <div class="inline-flex p-3 rounded-full bg-[#FFFFFF]/10 text-[#FFFFFF] mb-4 border border-[#FFFFFF]/20">
          <Gift class="w-6 h-6 animate-bounce" />
        </div>
        <div>
          <h2 class="section-title text-4xl md:text-5xl font-light tracking-wide">
            Wedding Gift
          </h2>
        </div>
        <p class="font-serif italic text-[#F3F4F6]/80 text-sm md:text-base mt-2">
          Bagi keluarga dan kerabat yang ingin mengirimkan tanda kasih dan kado digital
        </p>
        <div class="flex items-center justify-center space-x-3 mt-4">
          <div class="h-[1px] w-12 bg-linear-to-r from-transparent to-[#FFFFFF]/35"></div>
          <span class="text-[#FFFFFF]/45 text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-linear-to-l from-transparent to-[#FFFFFF]/35"></div>
        </div>
      </div>

      <!-- Bank Accounts (centered, full width) -->
      <div class="reveal reveal-up space-y-5">
        <h3 class="font-display text-2xl font-light text-[#FFFFFF] text-center mb-4">
          Transfer Bank
        </h3>

        <!-- BCA Card -->
        <div class="bg-black/45 p-6 rounded-2xl shadow-xl flex items-center justify-between relative overflow-hidden group">
          <div class="space-y-1.5">
            <span class="font-sans text-[10px] tracking-widest font-bold text-[#FFFFFF] uppercase">Bank BCA</span>
            <p class="font-mono text-lg font-semibold tracking-wider text-white">8600 4567 12</p>
            <p class="font-serif text-sm text-[#F3F4F6] font-medium">a.n. Arief Wijaya</p>
          </div>

          <button
            @click="copyToClipboard('8600456712', 'bca')"
            class="flex items-center space-x-1.5 py-2 px-4 rounded-xl font-sans text-xs font-semibold tracking-wider transition-all duration-300 border border-[#FFFFFF]/20 cursor-pointer hover:bg-[#FFFFFF] hover:text-black"
            :class="copiedState.bca
              ? 'bg-green-950/40 border-green-600 text-green-400'
              : 'bg-black/40 text-[#FFFFFF]'"
          >
            <Check v-if="copiedState.bca" class="w-3.5 h-3.5" />
            <Copy v-else class="w-3.5 h-3.5" />
            <span>{{ copiedState.bca ? 'Tersalin' : 'Salin Rek' }}</span>
          </button>
        </div>

        <!-- Mandiri Card -->
        <div class="bg-black/45 p-6 rounded-2xl shadow-xl flex items-center justify-between relative overflow-hidden group">
          <div class="space-y-1.5">
            <span class="font-sans text-[10px] tracking-widest font-bold text-[#FFFFFF] uppercase">Bank Mandiri</span>
            <p class="font-mono text-lg font-semibold tracking-wider text-white">1370 0123 4567</p>
            <p class="font-serif text-sm text-[#F3F4F6] font-medium">a.n. Syifa Salsabila</p>
          </div>

          <button
            @click="copyToClipboard('137001234567', 'mandiri')"
            class="flex items-center space-x-1.5 py-2 px-4 rounded-xl font-sans text-xs font-semibold tracking-wider transition-all duration-300 border border-[#FFFFFF]/20 cursor-pointer hover:bg-[#FFFFFF] hover:text-black"
            :class="copiedState.mandiri
              ? 'bg-green-950/40 border-green-600 text-green-400'
              : 'bg-black/40 text-[#FFFFFF]'"
          >
            <Check v-if="copiedState.mandiri" class="w-3.5 h-3.5" />
            <Copy v-else class="w-3.5 h-3.5" />
            <span>{{ copiedState.mandiri ? 'Tersalin' : 'Salin Rek' }}</span>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import { Gift, Copy, Check } from 'lucide-vue-next';

const copiedState = ref({
  bca: false,
  mandiri: false
});

function copyToClipboard(value, key) {
  navigator.clipboard.writeText(value).then(() => {
    copiedState.value[key] = true;
    setTimeout(() => {
      copiedState.value[key] = false;
    }, 2000);
  }).catch(err => {
    console.error("Clipboard copy failed: ", err);
  });
}
</script>
