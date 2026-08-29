<template>
  <section id="event" class="relative py-24 bg-black text-[#F5F0E8] overflow-hidden">
    <!-- Background Photo: gallery-2.jpeg (portrait, baju hitam) - no zoom -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <img src="/assets/gallery-2.jpeg" alt="" class="absolute inset-0 w-full h-full object-cover opacity-40" style="filter: blur(40px); transform: scale(1.1);" />
      <img src="/assets/gallery-2.jpeg" alt="" class="opacity-85" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-height:100vh;width:100%;object-fit:contain;" />
    </div>
    <!-- cinematic gradient overlay -->
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.65) 100%);"></div>
    <div class="absolute inset-0 floral-overlay opacity-20 pointer-events-none"></div>
    <div class="absolute -right-32 top-10 w-96 h-96 rounded-full bg-[#FFFFFF]/5 blur-3xl pointer-events-none"></div>
    <div class="absolute -left-32 bottom-10 w-96 h-96 rounded-full bg-[#FFFFFF]/5 blur-3xl pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-6xl mx-auto px-6">
      <!-- Section Header -->
      <div class="reveal reveal-up text-center mb-12 md:mb-16">
        <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-medium tracking-wide drop-shadow-lg">
          Detail Acara
        </h2>
        <p class="font-serif italic text-white/95 text-sm sm:text-base mt-2 drop-shadow-md max-w-xl mx-auto">
          Merupakan kehormatan besar bagi kami apabila Bapak/Ibu/Saudara/i berkenan hadir di hari bahagia kami
        </p>
        <div class="flex items-center justify-center space-x-3 mt-4">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/50"></div>
          <span class="text-white text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/50"></div>
        </div>
      </div>

      <!-- Events Cards Grid (3 Columns for Akad, Resepsi 1, Resepsi 2) -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch">
        
        <!-- 1. Akad Nikah Card -->
        <div class="reveal reveal-up mono-card p-8 rounded-3xl flex flex-col justify-between transition-all duration-300 hover:border-white/40 hover:-translate-y-1.5" style="transition-delay: 0ms">
          <div>
            <!-- Header Ornament Circle -->
            <div class="w-12 h-12 rounded-full bg-white/10 border border-white/25 flex items-center justify-center mx-auto mb-5 text-white shadow-md">
              <span class="font-serif text-xl font-light">⚜</span>
            </div>

            <!-- Title -->
            <h3 class="font-display text-3xl font-light text-white tracking-wide text-center mb-8">
              Akad Nikah
            </h3>

            <!-- Details List -->
            <div class="space-y-6 text-sm text-neutral-300 px-1">
              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Calendar class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Hari & Tanggal</h4>
                  <p class="font-serif text-base text-white font-medium">Minggu, 13 September 2026</p>
                </div>
              </div>

              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Clock class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Waktu</h4>
                  <p class="font-serif text-base text-white font-medium">Pukul 08.30 WIB - Selesai</p>
                </div>
              </div>

              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <MapPin class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Tempat</h4>
                  <p class="font-serif text-base text-white font-semibold">Hotel Mutiara Merdeka</p>
                  <p class="font-sans text-xs mt-1 leading-relaxed text-neutral-300">
                    Jl. Yos Sudarso No. 12A, Senapelan, Pekanbaru
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. Resepsi Pertama Card -->
        <div class="reveal reveal-up mono-card p-8 rounded-3xl flex flex-col justify-between transition-all duration-300 hover:border-white/40 hover:-translate-y-1.5" style="transition-delay: 150ms">
          <div>
            <!-- Header Ornament Circle -->
            <div class="w-12 h-12 rounded-full bg-white/10 border border-white/25 flex items-center justify-center mx-auto mb-5 text-white shadow-md">
              <span class="font-serif text-xl font-light">⚜</span>
            </div>

            <!-- Title -->
            <h3 class="font-display text-3xl font-light text-white tracking-wide text-center mb-8">
              Resepsi Pekanbaru
            </h3>

            <!-- Details List -->
            <div class="space-y-6 text-sm text-neutral-300 px-1">
              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Calendar class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Hari & Tanggal</h4>
                  <p class="font-serif text-base text-white font-medium">Minggu, 13 September 2026</p>
                </div>
              </div>

              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Clock class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Waktu</h4>
                  <p class="font-serif text-base text-white font-medium">Pukul 12.30 WIB - Selesai</p>
                </div>
              </div>

              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <MapPin class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Tempat</h4>
                  <p class="font-serif text-base text-white font-semibold">Hotel Mutiara Merdeka</p>
                  <p class="font-sans text-xs mt-1 leading-relaxed text-neutral-300">
                    Jl. Yos Sudarso No. 12A, Senapelan, Pekanbaru
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Resepsi Kedua Card -->
        <div class="reveal reveal-up mono-card p-8 rounded-3xl flex flex-col justify-between transition-all duration-300 hover:border-white/40 hover:-translate-y-1.5" style="transition-delay: 300ms">
          <div>
            <!-- Header Ornament Circle -->
            <div class="w-12 h-12 rounded-full bg-white/10 border border-white/25 flex items-center justify-center mx-auto mb-5 text-white shadow-md">
              <span class="font-serif text-xl font-light">⚜</span>
            </div>

            <!-- Title -->
            <h3 class="font-display text-3xl font-light text-white tracking-wide text-center mb-8">
              Resepsi Padang
            </h3>

            <!-- Details List -->
            <div class="space-y-6 text-sm text-neutral-300 px-1">
              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Calendar class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Hari & Tanggal</h4>
                  <p class="font-serif text-base text-white font-medium">Sabtu, 19 September 2026</p>
                </div>
              </div>

              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <Clock class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Waktu</h4>
                  <p class="font-serif text-base text-white font-medium">Pukul 10.00 WIB - Selesai</p>
                </div>
              </div>

              <div class="flex items-start space-x-4">
                <div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 shrink-0 flex items-center justify-center text-white mt-0.5">
                  <MapPin class="w-4 h-4 text-white" />
                </div>
                <div>
                  <h4 class="font-sans font-semibold text-xs tracking-[0.2em] uppercase text-white mb-1">Tempat</h4>
                  <p class="font-serif text-base text-white font-semibold">Kediaman Mempelai Pria</p>
                  <p class="font-sans text-xs mt-1 leading-relaxed text-neutral-300">
                    Jl. Pulai No. 120 D, Kubu Marapalam, Padang
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import { Calendar, Clock, MapPin } from 'lucide-vue-next';
</script>

