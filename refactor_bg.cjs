const fs = require('fs');
const path = require('path');

const dir = path.join(process.cwd(), 'src/components');
const files = ['CoupleSection.vue', 'EventSection.vue', 'RSVPSection.vue', 'WishesSection.vue', 'GiftSection.vue', 'FooterSection.vue'];

files.forEach(f => {
  const file = path.join(dir, f);
  if (!fs.existsSync(file)) return;
  
  let content = fs.readFileSync(file, 'utf8');
  let original = content;
  
  const regex = /<!-- Background Photo \((.*?)\) -->\s*<div class="absolute inset-0 overflow-hidden pointer-events-none">\s*<!-- Blurred fill layer -->\s*<img\s*src="(.*?)"\s*alt=""\s*class="absolute inset-0 w-full h-full object-cover filter blur-2xl opacity-30 grayscale"\s*\/>\s*<!-- Contained fit layer showing 100% of the photo precisely -->\s*<img\s*src=".*?"\s*alt=""\s*class="absolute inset-0 w-full h-full object-contain grayscale"\s*style="opacity:0.55;"\s*\/>\s*<\/div>\s*<!-- dark gradient overlay -->\s*<div class="absolute inset-0" style="background: linear-gradient\(to bottom, rgba\(0,0,0,0\.7\) 0%, rgba\(0,0,0,0\.35\) 45%, rgba\(0,0,0,0\.8\) 100%\);\"><\/div>/gs;

  content = content.replace(regex, (match, p1, p2) => {
    return `<!-- Background Photo (${p1}) -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none flex items-center justify-center bg-[#0A0A0A]">
      <img
        src="${p2}"
        alt=""
        class="absolute inset-0 w-full h-full object-contain grayscale opacity-60"
        style="-webkit-mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 45%, rgba(0,0,0,0) 90%); mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 45%, rgba(0,0,0,0) 90%);"
      />
    </div>
    <!-- soft dark gradient overlay for text readability -->
    <div class="absolute inset-0 bg-gradient-to-b from-[#0A0A0A]/90 via-[#0A0A0A]/40 to-[#0A0A0A]/90"></div>`;
  });
  
  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    console.log('Fixed ' + f);
  }
});

console.log('Done');
