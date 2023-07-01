import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createI18n } from 'vue-i18n'
import messages from './messages.json'

const i18n = createI18n({
  legacy: false, // set `false` in order to use Composition API
  locale: 'zh-tw', // set locale
  fallbackLocale: 'en', // set fallback locale
  messages, // set locale messages
})

createApp(App).use(i18n).mount('#app')
