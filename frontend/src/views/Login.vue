<script>

import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  data () {
    return {
      useRouter: useRouter(),
      emailLogin: '',
      senhaLogin: '',
      httpStatusCode: 0,
      showPassword: false,
      recarregarPagina: true
    }
  },

  methods: {
    // Method to redirect to 'HOME' upon success.
    // Método para redirecionar para a 'HOME' em caso de sucesso.
    redirectToHome () {
      this.useRouter.push('/');
    },
    // Method to save the generated token in LocalStorage.
    // Método para guardar o token gerado no LocalStorage.
    saveTokenLocalStorage (token) {
      localStorage.setItem('token', token);
    },
    // Method to set 'this.httpStatusCode' with success and error cases.
    // Método para setar o 'this.httpStatusCode' com os casos de sucesso e erro.
    setHttpStatusCode (succesError) {
      this.httpStatusCode = succesError;
    },
    // Method that receives the user login request and
    // handles the error in case of failure.
    // Método que recebe a requisição de login do usuário
    // e trata o erro em caso de erro.
    login () {
      axios.post('http://localhost:8000/token/',
      {
        username: this.emailLogin,
        password: this.senhaLogin
      }).then((res) => {
        this.saveTokenLocalStorage(res['data']['access']);
        this.redirectToHome();
      }).catch((error) => {
        this.setHttpStatusCode(error.response.status);
      })
    },
    // Method that shows and hides the password.
    // Método que mostra a senha.
    changeShowPassword () {
      this.showPassword = !this.showPassword;
    },
    // Handles the click of the ENTER button.
    // Lida com o clique do botão ENTER.
    HGPKEnterLogin (event) {
      const e = event;
      // Checks if the pressed button was 'ENTER'.
      // Confere se o botão apertado foi o 'ENTER'.
      const ENTER = e.key === 'Enter';

      // Retrieves buttons and elements from the page.
      // Recupera botões e elementos da página.
      let loginButton = document.getElementById('login-button');

      if (ENTER) {
        e.preventDefault();
        loginButton.click();
      }
    },
    // Adds the event listener when the page is mounted.
    // Adiciona o escutador de eventos ao montar a página.
    addHGPKEnterLogin () {
      window.addEventListener('keydown', this.HGPKEnterLogin);
    },
    // Removes the event listener when the page is unmounted.
    // Remove o escutador de eventos ao desmontar a página.
    removeHGPKEnterLogin () {
      window.removeEventListener('keydown', this.HGPKEnterLogin);
    },
  },

  mounted () {
    this.addHGPKEnterLogin();
  },

  unmounted () {
    this.removeHGPKEnterLogin();
  }

}

</script>

<template>

  <main class="darker-body">
    <!-- Main Container -->
    <div class="container d-flex justify-content-center align-items-center min-vh-100">
      <!-- Login Container -->
      <div class="row border rounded-5 p-3 bg-white shadow box-area">

        <!-- Left Box -->
        <div class="col-md-6 rounded-4 d-flex justify-content-center align-items-center flex-column left-box" style="background: #252925;">
          <div class="featured-image mb-3 mt-3">
            <!--  -->
          </div>
          <p class="text-white fs-2" style="font-family:'Courier New', Courier, monospace; font-weight: 700;">File Uploader!</p>
          <!-- <small class="text-white text-warp text-center" style="width: 17rem; font-family: 'Courier New', Courier, monospace;"></small> -->
        </div>

        <!-- Right Box -->
        <div class="col-md-6 rounded-4 d-flex flex-column right-box">
          <div class="ajuste-tamanho">
              <form action="POST" class="ajuste-tamanho">

                <div>
                  <!-- @keyup.enter="login" -->
                  <!-- Email -->
                  <div class="mb-3">
                    <label for="email-login-input" class="form-label bold">Username:</label>
                      <input
                        type="text"
                        class="form-control"
                        id="email-login-input"
                        placeholder="username"
                        v-model="emailLogin"
                      >
                  </div>

                  <!-- Senha -->
                  <label for="senha-login-input" class="form-label bold">Password:</label>
                  <div class="input-group" id="senha-login-input">
                    <input
                      :type="this.showPassword ? 'text' : 'password'"
                      class="form-control"
                      placeholder="******"
                      aria-label="Recipient's username with two button addons"
                      v-model="senhaLogin"
                    >
                    <button v-if="!this.showPassword"
                      class="btn btn-outline-secondary small"
                      type="button"
                      title="Mostrar senha"
                      @click="changeShowPassword"
                    ><img src="../assets/hide-password.png" alt="mostrar/esconder senha"/></button>
                    <button v-if="this.showPassword"
                      class="btn btn-outline-secondary small"
                      type="button"
                      title="Esconder senha"
                      @click="changeShowPassword"
                    ><img src="../assets/hide-password.png" alt="mostrar/esconder senha"/></button>
                  </div>

                </div>
                <!-- Lembrar de mim? -->

                <!-- Resposta requisição com falha. -->
                <div>
                  <p
                    class="red-letter mt-2"
                    v-if="httpStatusCode === 401"
                    >Invalid username and/or password.
                  </p>
                </div>

                <!-- Entrar -->
                <div class="mb-3 mt-5">
                  <button
                    id="login-button"
                    type="button"
                    class="btn btn-success  light-green w-100 fs-6"
                    @click="login"
                  >Login</button>
                </div>

              </form>
          </div>

        </div>
      </div>
    </div>
  </main>

</template>

<style setup>

.darker-body{
  background-color: rgb(171, 180, 178);
  /* background-color: #252925; */
}

.small img {
  width: 15px;
  height: 15px;
}

.red-letter {
  color: red;
}

.company-color {
  background-color: #252925;
}

.box-area{
  width: 930px;
}

.border {
  border-radius: 1px solid #000;
}

.ajuste-tamanho {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

</style>
