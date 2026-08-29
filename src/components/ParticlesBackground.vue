<template>
  <div class="fixed inset-0 z-0 pointer-events-none overflow-hidden">
    <canvas ref="canvas" class="absolute inset-0 w-full h-full opacity-60"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const canvas = ref(null);
let animationFrameId;

onMounted(() => {
  const ctx = canvas.value.getContext('2d');
  let width, height;
  
  const setSize = () => {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.value.width = width;
    canvas.value.height = height;
  };
  
  setSize();
  window.addEventListener('resize', setSize);

  const particles = Array.from({ length: 60 }).map(() => ({
    x: Math.random() * width,
    y: Math.random() * height,
    size: Math.random() * 1.5 + 0.5,
    speedX: (Math.random() - 0.5) * 0.3,
    speedY: (Math.random() - 0.5) * 0.3 - 0.1, // Slight upward drift
    opacity: Math.random() * 0.5 + 0.1
  }));

  const draw = () => {
    ctx.clearRect(0, 0, width, height);
    
    particles.forEach(p => {
      p.x += p.speedX;
      p.y += p.speedY;
      
      if (p.x < 0) p.x = width;
      if (p.x > width) p.x = 0;
      if (p.y < 0) p.y = height;
      if (p.y > height) p.y = 0;
      
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 255, 255, ${p.opacity})`;
      ctx.fill();
    });
    
    animationFrameId = requestAnimationFrame(draw);
  };
  
  draw();

  onBeforeUnmount(() => {
    window.removeEventListener('resize', setSize);
    cancelAnimationFrame(animationFrameId);
  });
});
</script>
