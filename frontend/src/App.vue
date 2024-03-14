<script>
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
