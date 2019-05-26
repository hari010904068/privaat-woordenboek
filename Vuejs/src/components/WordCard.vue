<template>
  <div>
    <h1>{{msg}}</h1>
    <p>{{info}}</p>
    <fish-row>
      <fish-col span="24">
        <fish-table :columns="columns" :data="left"></fish-table>
      </fish-col>
    </fish-row>
    <fish-row>
      <fish-col span="8" class="demo-col"></fish-col>
      <fish-col span="8" class="demo-col demo-col2"></fish-col>
      <fish-col span="8" class="demo-col, table">
        <fish-button @click="addWord" type="primary">add new word</fish-button>
      </fish-col>
    </fish-row>

    <fish-modal title="add new item" :visible.sync="showModal">
      <fish-form>
        <fish-fields>
          <fish-field label="First Name" span="eight">
            <fish-input></fish-input>
          </fish-field>
          <fish-field label="Last Name" span="eight">
            <fish-input></fish-input>
          </fish-field>
        </fish-fields>
        <fish-button type="primary" @click="showModal = false">Submit</fish-button>
      </fish-form>
    </fish-modal>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.headers.common['Access-Control-Allow-Origin'] =
  'http://127.0.0.1:8080'
export default {
  name: 'WordCard',
  data() {
    return {
      info: null,
      msg: "Xiaoxu's Dutch Dictionary",
      showModal: false,
      columns: [
        { title: 'Word', key: 'word' },
        { title: 'Conjugation', key: 'conj' },
        { title: 'Example', key: 'example' },
        { title: 'Rate', key: 'rate' }
      ],
      left: null,
      right: null
    }
  },
  methods: {
    addWord(evt) {
      console.log('add word method')
      this.showModal = true
    }
  },
  mounted() {
    axios
      .get('http://127.0.0.1:5000/show')
      .then(response => (this.left = response.data['db_res'].slice(0, 5)))
  }
}
</script>

<style>
.table {
  margin-top: 2%;
}
</style>
