<template>
  <v-app id="inspire">
    <v-navigation-drawer fixed v-model="drawer" app>
      <!-- style="width:200px !important" -->
      <v-list dense>
        <v-list-tile @click>
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="teal" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Je privaat woordenboek</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <router-view></router-view>
    </v-content>
    <v-footer color="teal" app inset>
      <v-btn absolute dark fab buttom right color="pink" style="bottom:50px" @click="add_word">
        <v-icon>add</v-icon>
      </v-btn>
      <v-layout justify-center row wrap>
        <v-flex py-3 text-xs-center white--text xs12>
          &copy;2019 —
          <strong>Xiaoxu Gao</strong>
        </v-flex>
      </v-layout>
    </v-footer>
    <v-dialog v-model="dialog" max-width="500px">
      <v-form ref="form">
        <v-card>
          <v-card-title>
            <span class="headline">Voeg een nieuw woord toe</span>
          </v-card-title>
          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6>
                  <v-text-field v-model="form.nederlands" label="Nederlands" required></v-text-field>
                </v-flex>
                <v-flex xs12 sm12>
                  <v-text-field v-model="form.voorbeeld" label="Voorbeeld" required></v-text-field>
                </v-flex>
                <v-flex xs12 sm4>
                  <v-text-field label="ik"></v-text-field>
                </v-flex>
                <v-flex xs12 sm4>
                  <v-text-field label="jij"></v-text-field>
                </v-flex>
                <v-flex xs12 sm4>
                  <v-text-field label="wij"></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat color="primary" @click="add_word_confirm">Voorleggen</v-btn>
            <v-btn flat color="primary" @click="add_word_cancel">Annuleren</v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    const defaultForm = Object.freeze({
      nederlands: "",
      voorbeeld: ""
    });
    return {
      form: Object.assign({}, defaultForm),
      drawer: null,
      dialog: false
    };
  },
  methods: {
    add_word(evt) {
      console.log("invoke add word function");
      this.dialog = true;
    },
    add_word_confirm(evt) {
      console.log("is going to send POST api");
      console.log(evt);
      console.log(this.form.nederlands);
      //TODO: send POST api
      this.dialog = false;
    },
    add_word_cancel(env) {
      console.log("cancel");
      this.dialog = false;
    }
  }
};
</script>
