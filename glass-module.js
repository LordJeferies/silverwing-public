import { LiquidGlass } from './assets/liquidglass.js';
const hero = document.querySelector('.cinema-hero');
const preferences = [
  matchMedia('(prefers-reduced-motion: reduce)'),
  matchMedia('(prefers-reduced-transparency: reduce)'),
  matchMedia('(prefers-contrast: more)')
];
let visible = false;
let initializing = false;
let generation = 0;

function enabled() {
  return hero && visible && !document.hidden && location.protocol !== 'file:' &&
    !document.body.classList.contains('solid-material') && !preferences.some(p => p.matches);
}

function stopGlass() {
  generation++;
  glassInstance?.destroy();
  glassInstance = null;
  if (hero) hero.dataset.material = document.body.classList.contains('solid-material') ? 'solid' : 'css';
}

async function initGlass() {
  if (!enabled() || glassInstance || initializing) return;
  initializing = true;
  const current = generation;
  try {
    await document.fonts.ready;
    const img = hero.querySelector('.scene-bg');
    if (!img.complete) await img.decode();
    if (!enabled() || current !== generation) return;
    const probe = document.createElement('canvas');
    const context = probe.getContext('webgl');
    if (!context) return;
    context.getExtension('WEBGL_lose_context')?.loseContext();
    const glass = hero.querySelector('.cinema-offer');
    glass.dataset.config = JSON.stringify({cornerRadius:30,zRadius:18,refraction:.32,blurAmount:.08,chromAberration:.015,specular:.12,edgeHighlight:.08,fresnel:.5,floating:false,shadowOpacity:.2});
    const instance = await LiquidGlass.init({root:hero,glassElements:[glass]});
    if (!enabled() || current !== generation) {
      instance.destroy();
      return;
    }
    glassInstance = instance;
    hero.dataset.material = 'webgl';
  } catch (error) {
    if (hero) hero.dataset.material = 'css';
    console.info('Silverwing: material CSS activo.', error.message);
  } finally {
    initializing = false;
    if (current !== generation && enabled()) initGlass();
  }
}

function syncGlass() {
  if (enabled()) initGlass();
  else stopGlass();
}

const observer = new IntersectionObserver(entries => {
  visible = entries.some(e => e.isIntersecting);
  syncGlass();
}, {threshold:.1});
if (hero) observer.observe(hero);
const previousToggle = window.toggleMaterial;
window.toggleMaterial = function() {
  previousToggle();
  syncGlass();
};
document.addEventListener('visibilitychange', syncGlass);
preferences.forEach(p => p.addEventListener('change', syncGlass));
window.addEventListener('pagehide', stopGlass);
window.addEventListener('pageshow', syncGlass);
