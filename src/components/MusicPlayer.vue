<template>
  <div class="fixed bottom-6 right-6 z-40">
    <button 
      @click="togglePlayback"
      class="w-12 h-12 rounded-full bg-black/70 backdrop-blur-md shadow-2xl flex items-center justify-center border border-white/30 text-white cursor-pointer transition-all duration-300 hover:scale-110 hover:border-white/60 active:scale-95 group focus:outline-none"
      :class="{ 'animate-spin-slow': isPlaying }"
      aria-label="Toggle Musik"
    >
      <Volume2 v-if="isPlaying" class="w-5 h-5 text-white group-hover:scale-110 transition-transform" />
      <VolumeX v-else class="w-5 h-5 text-white group-hover:scale-110 transition-transform" />
    </button>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue';
import { Volume2, VolumeX } from 'lucide-vue-next';

const props = defineProps({
  shouldPlay: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits(['update:isPlaying']);

const isPlaying = ref(false);
let audio = null;

const audioUrl = '/assets/new-bgm.m4a';

onMounted(() => {
  // Initialize HTML5 Audio
  audio = new Audio(audioUrl);
  audio.loop = true;
  audio.volume = 0.5; // Medium comfortable volume
  
  // Keep states synchronized
  audio.onplay = () => {
    isPlaying.value = true;
    emit('update:isPlaying', true);
  };
  audio.onpause = () => {
    isPlaying.value = false;
    emit('update:isPlaying', false);
  };
});

onUnmounted(() => {
  if (audio) {
    audio.pause();
    audio = null;
  }
});

// Watch trigger from CoverScreen unlock
watch(() => props.shouldPlay, (newVal) => {
  if (newVal && audio) {
    playAudio();
  }
});

function playAudio() {
  if (!audio) return;
  audio.play().then(() => {
    isPlaying.value = true;
  }).catch((error) => {
    console.warn("Autoplay block prevented audio startup. Waiting for interaction:", error);
    isPlaying.value = false;
  });
}

function pauseAudio() {
  if (audio) {
    audio.pause();
    isPlaying.value = false;
  }
}

function togglePlayback() {
  if (!audio) return;
  if (isPlaying.value) {
    pauseAudio();
  } else {
    playAudio();
  }
}
</script>

<style scoped>
/* Spinning slow keyframe class from tailwind v4 is registered in style.css */
</style>

