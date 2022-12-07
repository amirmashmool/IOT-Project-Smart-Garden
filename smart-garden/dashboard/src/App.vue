<template>
  <div class="max-w-4xl mx-auto my-10">
  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-xl font-semibold text-gray-900">Sensors</h1>
      </div>
    </div>
    <div class="mt-8 flex flex-col">
      <div class="-my-2 -mx-4 sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle">
          <div class="shadow-sm ring-1 ring-black ring-opacity-5">
            <table class="min-w-full border-separate" style="border-spacing: 0">
              <thead class="bg-gray-50">
                <tr>
                  <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">Date</th>
                  <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 sm:table-cell">Temperature</th>
                  <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 lg:table-cell">Motor</th>
                  <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 lg:table-cell">Light (%)</th>
                  <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 lg:table-cell">Soil Moisture (%)</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr v-for="item in data" :key="item._id">
                  <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6" :title=item.created_at>{{ convertDate(item.created_at)}}</td>
                  <td class="hidden whitespace-nowrap px-3 py-4 text-sm text-gray-500 sm:table-cell">{{ item.context.temperature.toFixed(2) }}</td>
                  <td class="hidden whitespace-nowrap px-3 py-4 text-sm text-gray-500 lg:table-cell" :class="[item.context.motor == '1' ? 'text-green-500' : 'text-red-500']">{{ item.context.motor == "1" ? "Open" : "Close" }}</td>
                  <td class="hidden whitespace-nowrap px-3 py-4 text-sm text-gray-500 sm:table-cell">{{ item.context.light.toFixed(2) }}</td>
                  <td class="hidden whitespace-nowrap px-3 py-4 text-sm text-gray-500 sm:table-cell">{{ item.context.humidity.toFixed(2) }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div v-if="data.length == 0 && currentPage != 1">
            <div class="flex items-center justify-center h-64">
              <div class="text-gray-500">No Date for page {{ currentPage }}</div>
            </div>
          </div>
          <div class="flex justify-between mt-2">
            <button v-on:click="previous()" v-if="currentPage != 1" class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Previous</button>
            <button>Page {{  currentPage }}</button>
            <button v-if="data.length != 0" v-on:click="next()"  class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Next</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import request from './environment/request'
import moment from 'moment'
export default {
  name: 'App',
  data() {
    return {
      data: [],
      currentPage: 1
    }
  },
  mounted() {
    this.getData()
  },
  watch: {
    currentPage() {
      this.getData()
    },
  },
  methods: {
    convertDate(date){
      return moment(date).fromNow()
    },
    async getData() {
      request().get(`?page=${this.currentPage}`).then(res => {
        this.data = res.data
      })
    },
    next() {
      this.currentPage += 1
    },
    previous() {
      this.currentPage -= 1
    }
  }
}
</script>