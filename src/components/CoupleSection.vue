<template>
  <section id="couple" class="relative py-24 bg-black text-[#F5F0E8] overflow-hidden">
    <!-- Background Photo: gallery-1.jpeg (portrait, baju merah) - no zoom -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <img src="/assets/gallery-1.jpeg" alt="" class="absolute inset-0 w-full h-full object-cover opacity-40" style="filter: blur(40px); transform: scale(1.1);" />
      <img src="/assets/gallery-1.jpeg" alt="" class="opacity-85" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-height:100vh;width:100%;object-fit:contain;" />
    </div>
    <!-- cinematic gradient overlay -->
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.65) 100%);"></div>
    <div class="absolute inset-0 floral-overlay opacity-30 pointer-events-none"></div>
    <div class="absolute -left-32 top-1/4 w-80 h-80 rounded-full bg-[#FFFFFF]/5 blur-3xl"></div>
    <div class="absolute -right-32 bottom-1/4 w-80 h-80 rounded-full bg-[#FFFFFF]/5 blur-3xl"></div>

    <div class="relative z-10 w-full max-w-5xl mx-auto px-6 text-center">
      <!-- Section Title -->
      <div class="reveal reveal-up mb-12 md:mb-16">
        <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-medium tracking-wide drop-shadow-lg">
          Kedua Mempelai
        </h2>
        <p class="font-serif italic text-white/95 text-sm sm:text-base mt-2 drop-shadow-md max-w-xl mx-auto">
          Dengan memohon rahmat dan ridho Allah SWT, kami bermaksud menyelenggarakan pernikahan kami
        </p>
        <div class="flex items-center justify-center space-x-3 mt-4">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/50"></div>
          <span class="text-white text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/50"></div>
        </div>
      </div>

      <!-- Profiles Container (Typography & Monogram Focused) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-10 items-stretch max-w-4xl mx-auto">
        
        <!-- Bride Card (Mempelai Wanita) -->
        <div class="reveal reveal-up mono-card p-8 sm:p-10 rounded-3xl flex flex-col justify-between items-center text-center transition-all duration-300 hover:border-white/40 hover:-translate-y-1" style="transition-delay: 0ms">
          <div class="space-y-6 w-full">
            <!-- Monogram Header Circle -->
            <div class="w-14 h-14 rounded-full bg-white/10 border border-white/25 flex items-center justify-center text-2xl text-white mx-auto shadow-md">
              <span class="font-serif font-light">♀</span>
            </div>

            <div class="space-y-2">
              <h3 class="font-display text-3xl sm:text-4xl font-normal text-white tracking-wide leading-tight">
                dr. Syifa Farhani Ridha
              </h3>
              <div class="inline-block px-3 py-1 rounded-full bg-white/10 border border-white/15">
                <p class="font-sans text-[10px] tracking-[0.25em] text-neutral-200 uppercase font-semibold">
                  Mempelai Wanita
                </p>
              </div>
            </div>
            
            <div class="h-[1px] w-16 bg-white/20 mx-auto"></div>
            
            <p class="font-sans text-sm text-neutral-300 leading-relaxed">
              Anak pertama dari pasangan <br />
              <strong class="text-white font-medium font-serif block mt-2 text-base">Bapak Ir. Herisiswanto, M.T.</strong>
              <span class="text-xs text-neutral-400 block my-0.5">&amp;</span>
              <strong class="text-white font-medium font-serif block text-base leading-snug">
                Ibu Dr. dr. Elda Nazriati, M.Kes., Sp.KKLP, SubSp.FOMC
              </strong>
            </p>
          </div>
        </div>

        <!-- Groom Card (Mempelai Pria) -->
        <div class="reveal reveal-up mono-card p-8 sm:p-10 rounded-3xl flex flex-col justify-between items-center text-center transition-all duration-300 hover:border-white/40 hover:-translate-y-1" style="transition-delay: 150ms">
          <div class="space-y-6 w-full">
            <!-- Monogram Header Circle -->
            <div class="w-14 h-14 rounded-full bg-white/10 border border-white/25 flex items-center justify-center text-2xl text-white mx-auto shadow-md">
              <span class="font-serif font-light">♂</span>
            </div>

            <div class="space-y-2">
              <h3 class="font-display text-3xl sm:text-4xl font-normal text-white tracking-wide leading-tight">
                Arief Rachman Widyanto, S.T.
              </h3>
              <div class="inline-block px-3 py-1 rounded-full bg-white/10 border border-white/15">
                <p class="font-sans text-[10px] tracking-[0.25em] text-neutral-200 uppercase font-semibold">
                  Mempelai Pria
                </p>
              </div>
            </div>
            
            <div class="h-[1px] w-16 bg-white/20 mx-auto"></div>
            
            <p class="font-sans text-sm text-neutral-300 leading-relaxed">
              Anak tunggal dari pasangan <br />
              <strong class="text-white font-medium font-serif block mt-2 text-base">Alm. Bapak Bambang Widyanto</strong>
              <span class="text-xs text-neutral-400 block my-0.5">&amp;</span>
              <strong class="text-white font-medium font-serif block text-base leading-snug">
                Ibu Irma, S.H. - Bapak Zimerman
              </strong>
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
</script>

