<script>
// NOTES:
// Almost the entire application has been developed.
// Due to the short time, 2 features are missing:
// - Image download;
// - Better frontend tests.

// Quase toda a aplicação foi desenvolvida.
// Devido ao pouco tempo, faltam 2 funcionalidades:
// - Download de imagens;
// - Testes frontend melhores.

import { RouterView } from 'vue-router';
import MenuNav from './components/MenuNav.vue';

export default {

  components: {
    MenuNav,
  },

  computed: {
    isNotLoginPage() {
      return this.$route.path !== "/login"
    }
  },

}

</script>

<template>
  <header v-if="isNotLoginPage">
    <MenuNav />
  </header>

  <main>
    <RouterView />
  </main>

</template>

<style setup>
body {
  background-color: rgb(240, 240, 240);
}
</style>
