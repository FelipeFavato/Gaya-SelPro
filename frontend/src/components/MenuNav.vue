<script>
import { useRouter } from 'vue-router';

export default {
  data () {
    return {
      useRouter: useRouter(),
    }
  },

  methods: {
    // Redirect to login page/ redireciona a pagina de login.
    redirectToLogin () {
      this.useRouter.push('/login');
    },
    // Excludes token and redirects to login page.
    // Exclue o token e redireciona para a tela de LOGIN.
    logout () {
      localStorage.removeItem('token');
      this.redirectToLogin();
    },
  }
}
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary margin-bottom" data-bs-theme="dark">
    <div class="container-fluid">

      <!-- Logo/Name -->
      <div class="navbar-brand">
        <p class="constr font-size">File uploader</p>
      </div>

      <!-- Cellphone menuNav/ Menu navegação Celular -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      ><span class="navbar-toggler-icon"></span>
      </button>

      <div class="d-flex separate">
        <!-- Logout - Button/ Botão - Sair -->
        <button
          type="button"
          class="nav-link small"
          title="Logout"
          @click="logout"
        ><img src="../assets/logout.png" alt="Sair">
        </button>
      </div>
    </div>

  </nav>
</template>

<style scoped>
.font-size {
  font-size: 20px;
  height: 15px;
}

.small img {
  height: 25px;
  width: 25px;
}

.margin-bottom {
  margin-bottom: 5px;
}
</style>