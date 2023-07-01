<script>
import axios from 'axios';

const api = new axios.Axios({
  baseURL: 'http://ocrserver.vincent55.tw:8000',
  headers: {
    'Content-Type': 'application/json',
    'api-version': '1',
  },
})

export default {
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
          id_number: this.idNumber,
        })
        console.log(data)
      } catch (error) {
        console.error(error)
      }
    },
  },
};
</script>

<template>
  <div class="container sm:mx-auto mt-20">
    <h1 class="text-3xl font-bold">Have my ID been pwned?</h1>
    <div class="flex w-72 flex-col gap-6 mt-10">
      <div class="relative h-11 w-full min-w-[200px]">
        <input placeholder="A123456789" v-model="idNumber"
          class="peer h-full w-full border-b border-blue-gray-200 bg-transparent pt-4 pb-1.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-pink-500 focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50" />
        <label
          class="after:content[' '] pointer-events-none absolute left-0 -top-2.5 flex h-full w-full select-none text-sm font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-2.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-pink-500 after:transition-transform after:duration-300 peer-placeholder-shown:leading-tight peer-placeholder-shown:text-blue-gray-500 peer-focus:text-sm peer-focus:leading-tight peer-focus:text-pink-500 peer-focus:after:scale-x-100 peer-focus:after:border-pink-500 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
          ID number
        </label>
      </div>
      <div class="">
        <button @click="checkHash()" class="bg-pink-500 hover:bg-pink-600 text-white font-bold py-2 px-4 rounded">
          Check
        </button>
      </div>
      <div>
        <h2 class="text-xl font-bold">Leaked in datasets:</h2>
        <div v-for="leak in leaks" v-key="leak.name">
          <h2 class="text-xl font-bold">{{ leak.name }}</h2>
          <ul class="flex flex-wrap items-center justify-center mb-6 text-gray-900">
            <li v-for="column in leak.columns" v-key="column" class="mr-4 hover:underline md:mr-6">
              {{ column }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>