<template>
  <section id="rsvp" class="relative py-24 bg-black text-[#F5F0E8] overflow-hidden">
    <!-- Background Photo: gallery-6.jpeg -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <img src="/assets/gallery-6.jpeg" alt="" class="absolute inset-0 w-full h-full object-cover opacity-40" style="filter: blur(40px); transform: scale(1.1);" />
      <img src="/assets/gallery-6.jpeg" alt="" class="opacity-85" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-height:100vh;width:100%;object-fit:contain;" />
    </div>
    <!-- cinematic gradient overlay -->
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.65) 100%);"></div>
    <div class="absolute inset-0 floral-overlay opacity-20 pointer-events-none"></div>
    <div class="absolute left-10 top-10 w-72 h-72 rounded-full bg-[#FFFFFF]/5 blur-3xl pointer-events-none"></div>

    <div class="relative z-10 w-full max-w-lg mx-auto px-6">
      <!-- Section Header -->
      <div class="reveal reveal-up text-center mb-10 md:mb-12">
        <h2 class="section-title text-3xl sm:text-4xl md:text-5xl font-medium tracking-wide drop-shadow-lg">
          RSVP & Konfirmasi Kehadiran
        </h2>
        <p class="font-serif italic text-white/95 text-sm sm:text-base mt-2 drop-shadow-md max-w-xl mx-auto">
          Mohon konfirmasi kehadiran Bapak/Ibu/Saudara/i untuk membantu persediaan konsumsi kami
        </p>
        <div class="flex items-center justify-center space-x-3 mt-4">
          <div class="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/50"></div>
          <span class="text-white text-sm">⚜</span>
          <div class="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/50"></div>
        </div>
      </div>

      <!-- RSVP Box -->
      <div class="reveal reveal-up mono-card p-8 sm:p-10 rounded-3xl relative overflow-hidden">
        
        <!-- Success State -->
        <Transition name="fade-scale" mode="out-in">
          <div v-if="isSubmitted" class="text-center py-10 space-y-6">
            <div class="w-20 h-20 bg-white/10 rounded-full flex items-center justify-center mx-auto border border-white/30 shadow-lg">
              <Check class="w-10 h-10 text-white" />
            </div>
            <div class="space-y-2">
              <h3 class="font-display text-3xl font-light text-white">Terima Kasih!</h3>
              <p class="font-sans text-sm text-neutral-300 leading-relaxed">
                Konfirmasi kehadiran Anda telah berhasil kami simpan. Doa restu Anda sangat berarti bagi kami.
              </p>
            </div>
          </div>

          <!-- Form State -->
          <form v-else @submit.prevent="handleSubmit" class="space-y-6">
            <!-- Name Input -->
            <div class="space-y-1.5">
              <label for="name" class="block font-sans text-xs tracking-[0.2em] uppercase text-white font-semibold">
                Nama Lengkap
              </label>
              <div class="relative">
                <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-white/70">
                  <User class="w-4 h-4" />
                </span>
                <input 
                  type="text" 
                  id="name" 
                  v-model="form.name" 
                  required
                  placeholder="Masukkan nama lengkap Anda"
                  class="w-full pl-10 pr-4 py-3 bg-black/70 border border-white/25 rounded-xl font-sans text-sm focus:outline-none focus:ring-1 focus:ring-white focus:border-white text-white placeholder-white/40 transition-all"
                />
              </div>
            </div>

            <!-- Guest Count Selector -->
            <div class="space-y-1.5">
              <label for="guests" class="block font-sans text-xs tracking-[0.2em] uppercase text-white font-semibold">
                Jumlah Tamu
              </label>
              <div class="relative">
                <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-white/70">
                  <Users class="w-4 h-4" />
                </span>
                <select 
                  id="guests" 
                  v-model="form.guests"
                  class="w-full pl-10 pr-4 py-3 bg-black/70 border border-white/25 rounded-xl font-sans text-sm focus:outline-none focus:ring-1 focus:ring-white focus:border-white text-white [&>option]:bg-neutral-900 transition-all"
                >
                  <option :value="1">1 Orang</option>
                  <option :value="2">2 Orang</option>
                  <option :value="3">3 Orang</option>
                  <option :value="4">4 Orang</option>
                </select>
              </div>
            </div>

            <!-- Attendance Selection (Cards) -->
            <div class="space-y-2">
              <label class="block font-sans text-xs tracking-[0.2em] uppercase text-white font-semibold">
                Konfirmasi Kehadiran
              </label>
              <div class="grid grid-cols-2 gap-4">
                <!-- Hadir -->
                <button 
                  type="button"
                  @click="form.attendance = 'Hadir'"
                  class="py-3 px-4 rounded-xl font-sans text-xs font-semibold tracking-wider transition-all duration-300 flex items-center justify-center space-x-2 cursor-pointer border"
                  :class="form.attendance === 'Hadir' 
                    ? 'border-white bg-white text-black shadow-md' 
                    : 'border-white/20 bg-black/50 text-white/70 hover:border-white/40 hover:text-white'"
                >
                  <div class="w-3.5 h-3.5 rounded-full border flex items-center justify-center" :class="form.attendance === 'Hadir' ? 'border-black bg-black' : 'border-white/30'">
                    <div v-if="form.attendance === 'Hadir'" class="w-1.5 h-1.5 bg-white rounded-full"></div>
                  </div>
                  <span>Hadir</span>
                </button>

                <!-- Tidak Hadir -->
                <button 
                  type="button"
                  @click="form.attendance = 'Tidak Hadir'"
                  class="py-3 px-4 rounded-xl font-sans text-xs font-semibold tracking-wider transition-all duration-300 flex items-center justify-center space-x-2 cursor-pointer border"
                  :class="form.attendance === 'Tidak Hadir' 
                    ? 'border-white bg-white text-black shadow-md' 
                    : 'border-white/20 bg-black/50 text-white/70 hover:border-white/40 hover:text-white'"
                >
                  <div class="w-3.5 h-3.5 rounded-full border flex items-center justify-center" :class="form.attendance === 'Tidak Hadir' ? 'border-black bg-black' : 'border-white/30'">
                    <div v-if="form.attendance === 'Tidak Hadir'" class="w-1.5 h-1.5 bg-white rounded-full"></div>
                  </div>
                  <span>Tidak Hadir</span>
                </button>
              </div>
            </div>

            <!-- Messages / Wishes Textarea -->
            <div class="space-y-1.5">
              <label for="message" class="block font-sans text-xs tracking-[0.2em] uppercase text-white font-semibold">
                Ucapan Doa & Harapan
              </label>
              <textarea 
                id="message" 
                v-model="form.message" 
                rows="4"
                placeholder="Tuliskan pesan ucapan doa dan harapan Anda untuk kedua mempelai di sini..."
                class="w-full p-4 bg-black/70 border border-white/25 rounded-xl font-sans text-sm focus:outline-none focus:ring-1 focus:ring-white focus:border-white text-white placeholder-white/40 resize-none transition-all"
              ></textarea>
            </div>

            <!-- Submit Button -->
            <button 
              type="submit" 
              :disabled="isSubmitting"
              class="group w-full relative overflow-hidden bg-gradient-to-r from-neutral-200 via-white to-neutral-300 hover:from-white hover:to-neutral-100 text-black py-3.5 px-6 rounded-xl font-sans text-xs font-semibold tracking-[0.2em] uppercase transition-all duration-300 shadow-xl disabled:opacity-70 disabled:cursor-not-allowed cursor-pointer active:scale-98"
            >
              <span class="flex items-center justify-center space-x-2">
                <span v-if="isSubmitting" class="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin"></span>
                <Send v-else class="w-4 h-4 text-black group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
                <span>{{ isSubmitting ? 'Mengirim...' : 'Kirim Konfirmasi' }}</span>
              </span>
            </button>
          </form>
        </Transition>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { User, Users, Check, Send } from 'lucide-vue-next';
import { submitRSVPApi } from '../firebase';
import { getFormattedGuestName } from '../utils/guest';

const form = ref({
  name: '',
  guests: 1,
  attendance: 'Hadir',
  message: ''
});

const isSubmitting = ref(false);
const isSubmitted = ref(false);

onMounted(() => {
  const gName = getFormattedGuestName();
  if (gName && gName !== 'Tamu Undangan') {
    form.value.name = gName;
  }
});

async function handleSubmit() {
  if (!form.value.name.trim()) return;

  isSubmitting.value = true;
  try {
    const result = await submitRSVPApi({
      name: form.value.name,
      guests: parseInt(form.value.guests),
      attendance: form.value.attendance,
      message: form.value.message
    });
    
    if (result.success) {
      isSubmitted.value = true;
    }
  } catch (error) {
    console.error("RSVP Submission Error:", error);
  } finally {
    isSubmitting.value = false;
  }
}
</script>

<style scoped>
.fade-scale-enter-active,
.fade-scale-leave-active {
  transition: all 0.5s ease;
}
.fade-scale-enter-from {
  opacity: 0;
  transform: scale(0.95);
}
.fade-scale-leave-to {
  opacity: 0;
  transform: scale(1.05);
}
</style>

