<template>
  <section id="map" class="relative py-24 bg-black text-[#F5F0E8] overflow-hidden">
    <!-- Background Photo: gallery-3.jpeg -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <img src="/assets/gallery-3.jpeg" alt="" class="absolute inset-0 w-full h-full object-cover opacity-35" style="filter: blur(40px); transform: scale(1.1);" />
      <img src="/assets/gallery-3.jpeg" alt="" class="opacity-80" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-height:100vh;width:100%;object-fit:contain;" />
    </div>
    <!-- Cinematic gradient overlay -->
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.65) 100%);"></div>
    <div class="absolute inset-0 floral-overlay opacity-15 pointer-events-none"></div>
    <div class="absolute -left-20 bottom-10 w-80 h-80 rounded-full bg-[#FFFFFF]/5 blur-3xl pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-4xl mx-auto px-6">
      <!-- Section Header -->
      <div class="reveal reveal-up text-center mb-10 md:mb-12">
        <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-medium tracking-wide drop-shadow-lg">
          Lokasi Acara
        </h2>
        <p class="font-serif italic text-white/95 text-sm sm:text-base mt-2 drop-shadow-md max-w-xl mx-auto">
          Petunjuk arah dan lokasi pelaksanaan acara pernikahan kami
        </p>
        <div class="flex items-center justify-center space-x-3 mt-4">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/50"></div>
          <span class="text-white text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/50"></div>
        </div>
      </div>

      <!-- Tab Switcher -->
      <div class="reveal reveal-up flex justify-center space-x-3 sm:space-x-4 mb-8">
        <button 
          v-for="(loc, idx) in locations" 
          :key="idx"
          @click="activeTabIndex = idx"
          class="px-6 py-2.5 rounded-full font-sans text-xs font-semibold tracking-[0.2em] uppercase border transition-all duration-300 cursor-pointer focus:outline-none"
          :class="activeTabIndex === idx 
            ? 'bg-white text-black border-white shadow-xl scale-105' 
            : 'bg-black/60 text-white/70 border-white/20 hover:bg-black/80 hover:border-white/40 hover:text-white'"
        >
          {{ loc.tabName }}
        </button>
      </div>

      <!-- Map Detail Card -->
      <div class="reveal reveal-up mono-card p-6 sm:p-8 rounded-3xl shadow-2xl grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        <!-- Info Panel (Left on large screen) -->
        <div class="lg:col-span-5 flex flex-col justify-between space-y-6">
          <div class="space-y-6">
            <!-- Title / Name of Venue -->
            <div>
              <span class="text-neutral-400 font-sans text-[10px] tracking-[0.25em] uppercase block mb-1 font-semibold">Tempat Acara</span>
              <h3 class="font-display text-2xl sm:text-3xl text-white font-normal tracking-wide">
                {{ activeLocation.venueName }}
              </h3>
            </div>

            <!-- Details List -->
            <div class="space-y-5 text-sm text-neutral-300">
              <div class="flex items-start space-x-3.5">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <MapPin class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Alamat</h4>
                  <p class="font-sans text-xs leading-relaxed text-neutral-300">
                    {{ activeLocation.address }}
                  </p>
                </div>
              </div>

              <div class="flex items-start space-x-3.5">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Calendar class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Hari & Tanggal</h4>
                  <p class="font-serif text-sm text-white font-medium">{{ activeLocation.date }}</p>
                </div>
              </div>

              <div class="flex items-start space-x-3.5">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Clock class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Waktu</h4>
                  <p class="font-serif text-sm text-white whitespace-pre-line leading-relaxed font-medium">{{ activeLocation.time }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Open in Google Maps Button -->
          <div class="pt-4">
            <a 
              :href="activeLocation.gmapsUrl" 
              target="_blank" 
              class="group flex items-center justify-center space-x-2 bg-gradient-to-r from-neutral-200 via-white to-neutral-300 hover:from-white hover:to-neutral-100 text-black py-3.5 px-5 rounded-xl font-sans text-xs font-semibold tracking-[0.2em] uppercase transition-all duration-300 shadow-xl active:scale-98 w-full cursor-pointer"
            >
              <Navigation class="w-4 h-4 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300" />
              <span>Buka Google Maps</span>
            </a>
          </div>
        </div>

        <!-- Map Iframe Panel (Right on large screen) -->
        <div class="lg:col-span-7 h-[300px] md:h-[380px] w-full rounded-2xl overflow-hidden border border-white/20 relative bg-neutral-950 shadow-inner">
          <iframe 
            :src="activeLocation.embedUrl" 
            width="100%" 
            height="100%" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade"
            class="w-full h-full opacity-90 grayscale contrast-125 invert-[0.9] hue-rotate-180"
          ></iframe>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue';
import { MapPin, Navigation, Calendar, Clock } from 'lucide-vue-next';

const activeTabIndex = ref(0);

const locations = [
  {
    tabName: 'Pekanbaru',
    venueName: 'Hotel Mutiara Merdeka',
    address: 'Jl. Yos Sudarso No. 12A, Senapelan, Pekanbaru',
    date: 'Minggu, 13 September 2026',
    time: 'Akad: 08.30 WIB - Selesai\nResepsi: 12.30 WIB - Selesai',
    gmapsUrl: 'https://www.google.com/maps/search/?api=1&query=Hotel+Mutiara+Merdeka+Pekanbaru+Jalan+Yos+Sudarso',
    embedUrl: 'https://maps.google.com/maps?q=Hotel+Mutiara+Merdeka+Pekanbaru+Jalan+Yos+Sudarso&t=&z=16&ie=UTF8&iwloc=&output=embed'
  },
  {
    tabName: 'Padang',
    venueName: 'Kediaman Mempelai Pria',
    address: 'Jl. Pulai No. 120 D, Kubu Marapalam, Padang',
    date: 'Sabtu, 19 September 2026',
    time: 'Resepsi: 10.00 WIB - Selesai',
    gmapsUrl: 'https://maps.app.goo.gl/c8Z17myn2EzLW55R7',
    embedUrl: 'https://maps.google.com/maps?q=-0.950971,100.387983&t=&z=16&ie=UTF8&iwloc=&output=embed'
  }
];

const activeLocation = computed(() => locations[activeTabIndex.value]);
</script>

<style scoped>
/* Custom responsive controls or map overlay adjustments */
</style>
