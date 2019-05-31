<template>
  <v-app id="inspire">
    <v-navigation-drawer fixed v-model="drawer" app v-if="authenticated">
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
    <v-toolbar color="teal" dark fixed app v-if="authenticated">
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Je privaat woordenboek</v-toolbar-title>
    </v-toolbar>
    <!-- <v-alert :value="true" type="success">This is a success alert.</v-alert> -->
    <v-content>
      <div>
        <v-alert v-model="submit_success" dismissible type="success">Sucessfully added a new word!</v-alert>
        <v-alert v-model="submit_error" dismissible type="error">Oops, something went wrong!</v-alert>
      </div>
      <router-view @authenticated="setAuthenticated"></router-view>
    </v-content>
    <v-footer color="teal" app inset v-if="authenticated">
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
                <v-flex xs12 sm12>
                  <v-text-field label="note" v-model="form.note"></v-text-field>
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
import axios from "axios";
export default {
  name: "App",
  data() {
    const defaultForm = Object.freeze({
      nederlands: "",
      voorbeeld: "",
      note: ""
    });
    return {
      submit_success: false,
      submit_error: false,
      authenticated: false,
      form: Object.assign({}, defaultForm),
      drawer: false,
      dialog: false
    };
  },
  mounted() {
    if (!this.authenticated) {
      this.$router.replace({ name: "Login" });
    }
  },
  methods: {
    setAuthenticated(status) {
      this.authenticated = status;
    },
    logout() {
      this.authenticated = false;
    },
    add_word(evt) {
      this.dialog = true;
      this.form = Object.assign({}, this.defaultForm);
    },
    add_word_confirm(evt) {
      //TODO: send POST api
      this.dialog = false;
      console.log("add word confirm");
      axios
        .post("http://127.0.0.1:5000/add", {
          nederlands: this.form.nederlands,
          voorbeeld: this.form.voorbeeld,
          note: this.form.note
        })
        .then(response => (this.submit_success = true))
        .catch(error => console.log("error"), (this.submit_error = true));
    },
    add_word_cancel(env) {
      this.dialog = false;
    }
  }
};
</script>

