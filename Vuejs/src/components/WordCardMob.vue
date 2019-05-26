<template>
  <div>
    <h1>{{title}}</h1>
    <ul>
      <li v-for="card in cards">{{card.word}}</li>
    </ul>
    <fish-row>
      <fish-col span="8" class="demo-col">
        <fish-card fluid class="card-margin">
          <div slot="header">Title</div>Kristy is an art director living in New York.
          <div slot="footer">
            <fish-button>GO-Back</fish-button>
          </div>
        </fish-card>
      </fish-col>
      <fish-col span="8" class="demo-col demo-col2">
        <fish-card fluid class="card-margin">
          <div slot="header">Title</div>Kristy is an art director living in New York.
          <div slot="footer">
            <fish-button>GO-Back</fish-button>
          </div>
        </fish-card>
      </fish-col>
      <fish-col span="8" class="demo-col demo-col2">
        <fish-card fluid class="card-margin">
          <div slot="header">Title</div>Kristy is an art director living in New York.
          <div slot="footer">
            <fish-button>GO-Back</fish-button>
          </div>
        </fish-card>
      </fish-col>
    </fish-row>
    <fish-row>
      <fish-col span="8" class="demo-col">
        <fish-card fluid class="card-margin">
          <div slot="header">Title</div>Kristy is an art director living in New York.
          <div slot="footer">
            <fish-button>GO-Back</fish-button>
          </div>
        </fish-card>
      </fish-col>
      <fish-col span="8" class="demo-col demo-col2">
        <fish-card fluid class="card-margin">
          <div slot="header">Title</div>Kristy is an art director living in New York.
          <div slot="footer">
            <fish-button>GO-Back</fish-button>
          </div>
        </fish-card>
      </fish-col>
      <fish-col span="8" class="demo-col demo-col2">
        <fish-card fluid class="card-margin">
          <div slot="header">Title</div>Kristy is an art director living in New York.
          <div slot="footer">
            <fish-button>GO-Back</fish-button>
          </div>
        </fish-card>
      </fish-col>
    </fish-row>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.headers.common['Access-Control-Allow-Origin'] =
  'http://127.0.0.1:8080'
export default {
  name: 'WordCardMob',
  data() {
    return {
      title: "Xiaoxu's Dutch Dictionary Mobile",
      cards: [
        { word: 'dutch', example: 'example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' },
        { word: 'want', example: 'want example' }
      ]
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
      .then(response => (this.left = response.data['db_res'].get(0)))
  }
}
</script>

<style>
.card-margin {
  margin-bottom: 20px;
}
</style>

