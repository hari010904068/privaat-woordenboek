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
      <!-- style="padding-left:200px !important" -->
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Je privaat woordenboek</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <router-view></router-view>
    </v-content>
    <v-footer color="teal" app inset>
      <v-btn absolute dark fab buttom right color="pink" style="bottom:50px">
        <v-icon>add</v-icon>
      </v-btn>
      <v-layout justify-center row wrap>
        <v-flex py-3 text-xs-center white--text xs12>
          &copy;2019 —
          <strong>Xiaoxu Gao</strong>
        </v-flex>
      </v-layout>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      drawer: null
    };
  }
};
</script>
