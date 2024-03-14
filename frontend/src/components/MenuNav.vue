<script>
import { useRouter } from 'vue-router';

export default {
  data () {
    return {
      useRouter: useRouter(),
    }
  },

  methods: {
    // Redirect to loginPage /redireciona para a página de login.
    redirectToLogin () {
      this.useRouter.push('/login');
    },
    // Exclude Token and redirect to login/
    // Exclui o token e redireciona para o login.
    logout () {
      localStorage.removeItem('token');
      this.redirectToLogin();
    },
  }
}
</script>

<template>
  <!-- Top NavBar that should render on every page except for login page -->
  <!-- Barra de navegação que deve renderizar em todas as paginas -->
  <nav class="navbar navbar-expand-lg bg-body-tertiary margin-bottom" data-bs-theme="dark">
    <div class="container-fluid">

      <!-- Logo/Name -->
      <div class="navbar-brand">
        <p class="constr font-size">File uploader</p>
      </div>

      <!-- Cellphone navMenu /Menu navegação Celular -->
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

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        
      </div>

      <div class="d-flex separate">
        <!-- Logout button/ Botão - Sair -->
        <button
          type="button"
          class="nav-link small"
          title="Logout"
          @click="logout"
        ><img src="../assets/logout.png" alt="logout">
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