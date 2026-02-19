// tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  // content
  content: [
    "./app/templates/**/*.html",
    "./app/modules/**/templates/**/*.html",
    "./app/static/**/*.js"
  ],
  // theme
  theme: {
    extend: {
      fontFamily: {
        'main': ['"Orbitron"', 'sans-serif'],
        'mono': ['"Share Tech Mono"', 'monospace'],
      },
      colors: {
        'neon-blue': '#00f3ff',
        'neon-pink': '#ff00ff',
      },
      animation: {
        'marquee': 'marquee 10s linear infinite',
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(100%)' },
          '100%': { transform: 'translateX(-100%)' },
        }
      }
    },
  },
  plugins: [],
}