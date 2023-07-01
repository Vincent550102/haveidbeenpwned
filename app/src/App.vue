<script>
import axios from 'axios';
import VividBackground from './components/VividBackground.vue'
import { useI18n } from 'vue-i18n'

const api = new axios.Axios({
  baseURL: 'http://ocrserver.vincent55.tw:8000',
  headers: {
    'Content-Type': 'application/json',
    'api-version': '1',
  },
})

export default {
  setup() {
    const { t, locale } = useI18n({ useScope: 'global' })
    return { t, locale }
  },
  data() {
    return {
      idNumber: "",
      leaks: [
        {
          name: "2023台灣個資外洩事件",
          columns: [
            "姓名",
            "出生年月日",
            "性別",
            "身分證字號",
            "戶籍地址",
            "戶籍郵遞區號",
            "通訊地址",
          ],
        }
      ]
    };
  },
  methods: {
    async checkHash() {
      try {
        const data = await api.get('/leak', {
          params: {
             id_number: this.idNumber,
          }
        })
        console.log(data)
      } catch (error) {
        console.error(error)
      }
    },
  },
  components: {
    VividBackground,
  },
};
</script>

<template>
  <div class="relative w-screen h-screen">
    <VividBackground class="w-full h-full" />
    <div class="absolute z-10 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
      <header class="float-right">
        <select v-model="locale">
          <option value="zh-tw">中文</option>
          <option value="en">English</option>
        </select>
      </header>
      <h1 class="text-3xl font-bold text-white">
        {{ t("message.title") }}
      </h1>
      <div class="relative mt-10 h-11 w-full min-w-[200px]">
        <input placeholder="A123456789" v-model="idNumber"
          class="peer text-white h-full w-full border-b border-blue-gray-200 bg-transparent pt-4 pb-1.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-green-500 focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50" />
        <label
          class="after:content[' '] pointer-events-none absolute left-0 -top-2.5 flex h-full w-full select-none text-sm font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-2.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-green-500 after:transition-transform after:duration-300 peer-placeholder-shown:leading-tight peer-placeholder-shown:text-blue-gray-500 peer-focus:text-sm peer-focus:leading-tight peer-focus:text-green-500 peer-focus:after:scale-x-100 peer-focus:after:border-green-500 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
          ID number
        </label>
      </div>
      <div class="">
        <button @click="checkHash()" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded">
          Check
        </button>
      </div>
      <div>
        <h2 class="text-xl text-white font-bold">Leaked in datasets:</h2>
        <div v-for="leak in leaks" v-key="leak.name">
          <h2 class="text-xltext-white  font-bold">{{ leak.name }}</h2>
          <ul class="flex flex-wrap items-center justify-center mb-6 text-gray-900">
            <li v-for="column in leak.columns" v-key="column" class="mr-4 text-white hover:underline md:mr-6">
              {{ column }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
