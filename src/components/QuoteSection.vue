<template>
  <section class="relative py-24 md:py-32 bg-[#0A0A0A] text-[#F8F9FA] overflow-hidden flex items-center justify-center border-t border-b border-white/10">
    <!-- Subtle Monochrome Background Glows -->
    <div class="absolute inset-0 floral-overlay opacity-15 pointer-events-none"></div>
    <div class="absolute -right-40 -top-40 w-96 h-96 rounded-full bg-white/[0.03] blur-3xl pointer-events-none"></div>
    <div class="absolute -left-40 -bottom-40 w-96 h-96 rounded-full bg-white/[0.03] blur-3xl pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-4xl px-6 text-center">
      <!-- Section Header Divider -->
      <div class="reveal reveal-up mb-8 flex justify-center text-white">
        <div class="flex items-center space-x-3">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/40"></div>
          <span class="text-lg">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/40"></div>
        </div>
      </div>

      <!-- Framed Monochrome Card for Quran Verse -->
      <div class="reveal reveal-up mono-card p-8 md:p-12 rounded-3xl space-y-8 relative overflow-hidden">
        <!-- Badge Tag -->
        <div class="inline-block px-5 py-1.5 rounded-full bg-white/10 border border-white/20">
          <p class="font-sans text-xs tracking-[0.3em] text-white uppercase font-semibold">
            QS. AR-RUM : 21
          </p>
        </div>

        <!-- Arabic Calligraphy -->
        <div class="select-none py-2">
          <p 
            class="text-2xl sm:text-3xl md:text-4xl text-white leading-loose antialiased px-2 font-medium" 
            style="font-family: 'Amiri', serif;" 
            dir="rtl"
          >
            وَمِنْ اٰيٰتِهٖٓ اَنْ خَلَقَ لَكُمْ مِّنْ اَنْفُسِكُمْ اَزْوَاجًا لِّتَسْكُنُوْٓا اِلَيْهَا وَجَعَلَ بَيْنَكُمْ مَّوَدَّةً وَّرَحْمَةً ۗ اِنَّ فِيْ ذٰلِكَ لَاٰيٰتٍ لِّقَوْمٍ يَّتَفَكَّرُوْنَ
          </p>
        </div>

        <div class="h-[1px] w-20 bg-white/20 mx-auto"></div>

        <!-- Indonesian Translation -->
        <div class="max-w-2xl mx-auto">
          <p class="font-serif italic text-sm md:text-base text-neutral-300 leading-relaxed">
            "Dan di antara tanda-tanda (kebesaran)-Nya ialah Dia menciptakan pasangan-pasangan untukmu dari jenismu sendiri, agar kamu cenderung dan merasa tenteram kepadanya, dan Dia menjadikan di antaramu rasa kasih dan sayang. Sungguh, pada yang demikian itu benar-benar terdapat tanda-tanda (kebesaran Allah) bagi kaum yang berpikir."
          </p>
        </div>
      </div>

      <!-- Bottom Ornament -->
      <div class="reveal reveal-up mt-8 flex justify-center text-white/50">
        <div class="flex items-center space-x-3">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/20"></div>
          <span class="text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/20"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// Static presentation component
</script>


