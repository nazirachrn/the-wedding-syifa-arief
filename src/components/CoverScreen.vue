<template>
  <Transition name="fade-slide">
    <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-[#0D0D0D] overflow-hidden select-none">
      <!-- Fullscreen Background Image with Ken Burns zoom effect (higher opacity for clarity) -->
      <div 
        class="absolute inset-0 bg-cover bg-center opacity-[0.80] scale-105 animate-[zoom-in_20s_infinite_alternate]"
        style="background-image: url('/assets/bg-cincin-bw.png');"
      ></div>

      <!-- Dark gradient overlay to blend the dark photo background with our dark theme -->
      <div class="absolute inset-0 bg-linear-to-t from-[#0D0D0D] via-[#0D0D0D]/75 to-[#0D0D0D]/40"></div>
      <div class="absolute inset-0 floral-overlay opacity-15"></div>

      <!-- Content Container (Minimalist, Compact spacing) -->
      <div class="relative z-10 w-full max-w-md px-6 flex flex-col items-center justify-between h-full py-8 text-center text-[#F8F9FA]">
        <!-- Top Logo -->
        <div class="animate-fade-in-down flex flex-col items-center">
          <img src="/assets/logo-white.png" alt="Logo" class="w-20 h-20 object-contain mb-3 drop-shadow-md" />
          <div class="h-[1px] w-28 bg-gradient-to-r from-transparent via-white/50 to-transparent mx-auto"></div>
        </div>

        <!-- Couple Names and Wording -->
        <div class="my-auto space-y-4 py-4">
          <div class="inline-block px-4 py-1 rounded-full bg-white/10 border border-white/20">
            <p class="font-sans text-[11px] tracking-[0.35em] text-white uppercase font-semibold animate-fade-in">
              Walimatul 'Ursy
            </p>
          </div>
          
          <h1 class="font-display text-5xl sm:text-6xl font-light text-white leading-tight tracking-[0.12em] drop-shadow-md animate-scale-in">
            <span class="block">Syifa</span>
            <span class="font-script text-4xl sm:text-5xl text-white block my-1">&amp;</span>
            <span class="block">Arief</span>
          </h1>

          <div class="h-[1px] w-14 bg-white/40 mx-auto my-3"></div>

          <!-- Date Wording -->
          <p class="font-display text-base sm:text-lg tracking-[0.2em] text-white font-medium uppercase">
            Minggu, 13 September 2026
          </p>
        </div>

        <!-- Invitation Box for Guest (Dark Premium Monokrom Glass Card) -->
        <div class="w-full bg-black/65 backdrop-blur-xl border border-white/20 p-6 rounded-3xl shadow-2xl space-y-4 mb-2 transform hover:scale-[1.01] transition-all duration-300">
          <p class="font-sans text-[11px] tracking-[0.2em] text-neutral-300 uppercase font-medium">
            Kepada Yth. Bapak/Ibu/Saudara/i
          </p>
          <div class="h-[1px] w-16 bg-gradient-to-r from-transparent via-white/30 to-transparent mx-auto"></div>
          
          <h3 class="font-display text-2xl sm:text-3xl font-normal text-white">
            {{ guestName }}
          </h3>
          
          <p class="font-sans text-[10px] text-neutral-400 leading-relaxed italic">
            *Mohon maaf apabila ada kesalahan penulisan nama/gelar
          </p>

          <!-- Buka Undangan Button -->
          <button 
            @click="openInvitation"
            class="group w-full mt-3 relative overflow-hidden bg-gradient-to-r from-neutral-200 via-white to-neutral-300 hover:from-white hover:to-neutral-100 text-black py-3.5 px-6 rounded-xl font-sans text-xs font-semibold tracking-[0.2em] uppercase transition-all duration-300 shadow-xl active:scale-98 cursor-pointer"
          >
            <div class="absolute inset-0 bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000 ease-out"></div>
            
            <div class="flex items-center justify-center space-x-2">
              <MailOpen class="w-4 h-4 text-black group-hover:scale-110 transition-transform duration-300" />
              <span>Buka Undangan</span>
            </div>
          </button>

          <!-- Hashtag -->
          <div class="pt-2 select-text border-t border-white/10">
            <p class="font-sans text-[11px] tracking-[0.25em] text-white/90 font-medium">
              #SYIFAinallyFoundARIEF
            </p>
          </div>
        </div>

        <!-- Bottom Footer Ornament -->
        <div class="text-white/40 text-xs tracking-widest font-sans font-light pt-2">
          ⚜
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { MailOpen } from 'lucide-vue-next';
import { getFormattedGuestName } from '../utils/guest';

const emit = defineEmits(['open']);
const isOpen = ref(true);
const guestName = ref('Tamu Undangan');

onMounted(() => {
  guestName.value = getFormattedGuestName();
});

function openInvitation() {
  isOpen.value = false;
  emit('open');
}
</script>

<style scoped>
.fade-slide-leave-active {
  transition: transform 1.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.1s cubic-bezier(0.16, 1, 0.3, 1);
}
.fade-slide-leave-to {
  transform: scale(1.06) translateY(-25px);
  opacity: 0;
}
</style>

