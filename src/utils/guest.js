/**
 * Parses and formats guest names from URL query parameters or URL pathnames.
 * Supports clean URLs like:
 * - ?to=Arief-dan-Keluarga -> "Arief & Keluarga"
 * - ?to=Arief+dan+Keluarga -> "Arief & Keluarga"
 * - /Arief-dan-Keluarga     -> "Arief & Keluarga"
 * - /to/Arief-dan-Keluarga  -> "Arief & Keluarga"
 * - ?to=Bapak-Arief         -> "Bapak Arief"
 */
export function getFormattedGuestName() {
  const urlParams = new URLSearchParams(window.location.search);
  let raw = urlParams.get('to') || urlParams.get('n') || urlParams.get('tamu') || urlParams.get('nama');

  // If not found in query params, inspect pathname (e.g., /Arief-dan-Keluarga)
  if (!raw) {
    const path = window.location.pathname.replace(/^\/+|\/+$/g, '');
    if (path && !path.includes('.') && path !== 'index.html') {
      const parts = path.split('/');
      const lastPart = parts[parts.length - 1];
      if (lastPart && lastPart !== 'to') {
        raw = lastPart;
      }
    }
  }

  if (!raw) return 'Tamu Undangan';

  let decoded = raw;
  try {
    decoded = decodeURIComponent(raw);
  } catch (e) {
    console.warn("Could not decode URL component", e);
  }

  // 1. Replace hyphens and underscores with spaces
  decoded = decoded.replace(/[-_]/g, ' ');

  // 2. Convert "dan" or "and" (standalone word) to "&"
  decoded = decoded.replace(/\bdan\b/gi, '&').replace(/\band\b/gi, '&');

  // 3. Trim and collapse extra spaces
  decoded = decoded.replace(/\s+/g, ' ').trim();

  return decoded || 'Tamu Undangan';
}
