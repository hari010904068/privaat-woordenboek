<template>
  <v-app>
    <v-container grid-list-md>
      <div class="title">
        <v-icon medium color="red lighten-2" class="icon-margin">favorite</v-icon>
        <span class="font-weight-medium title icon-margin">De uitdaging van vandaag</span>
        <v-icon medium color="red lighten-2">favorite</v-icon>
      </div>
      <v-layout row wrap>
        <v-flex xs12 sm4 md4 v-for="card in cards">
          <v-card>
            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">{{card.word}}</h3>
                <div>example</div>
              </div>
            </v-card-title>
            <v-card-actions>
              <v-btn flat icon color="blue lighten-2">
                <v-icon>thumb_up</v-icon>
              </v-btn>
              <v-btn flat icon color="red lighten-2">
                <v-icon>thumb_down</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "Challenge",
  data() {
    return {
      cards: [
        { word: "dutch", example: "example" },
        { word: "dutch", example: "example" },
        { word: "dutch", example: "example" },
        { word: "dutch", example: "example" },
        { word: "dutch", example: "example" },
        { word: "dutch", example: "example" },
        { word: "dutch", example: "example" }
      ]
    };
  }
};
</script>

<style>
.title {
  margin-bottom: 10px;
}
.icon-margin {
  margin-right: 10px;
}
</style>

