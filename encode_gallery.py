# Read and base64-encode the original file to test pipeline
import base64
with open(r'src\components\GallerySection.vue', 'rb') as f:
    data = f.read()
b64 = base64.b64encode(data).decode('ascii')
# Split into 72-char lines
lines = [b64[i:i+72] for i in range(0, len(b64), 72)]
print('lines:', len(lines))
print('total_b64:', len(b64))
with open(r'gallery_b64.txt', 'w') as f:
    f.write('\n'.join(lines))
print('saved to gallery_b64.txt')