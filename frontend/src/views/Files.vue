<script>
// npm install bootstrap
// npm create vue@latest
// npm i vue3-toastify 
// npm install axios
// npm install vue-router@4
import axios from 'axios';
import { useRouter } from 'vue-router';
import { getLocalStorageToken, insertSuccessToast,
  checkInputValue, deleteSuccessToast, clickSavecheckRequiredInsertField, removeElementClass } from '../utils';
import SkeletonCardsLoading from '@/components/SkeletonLoading/SkeletonCardsLoading.vue';

export default {
  data () {
    return {
      useRouter: useRouter(),
      localStorageToken: getLocalStorageToken(),
      info: [],
      id: '',
      name: '',
      picture: '',
      percentage: 0,
      loadingB: '',
    }
  },

  computed: {
  },

  components: {
    SkeletonCardsLoading
  },

  methods: {
    // Login validations methods/ Métodos de validação de login: -----------------------\
    redirectToLogin () {
      this.useRouter.push('/login');
    },
    validateHttpStatus (httpStatus) {
      httpStatus === 401 && this.redirectToLogin();
    },
    //////////////////////////////////////////////////////////////////////////////////////

    // Fetch data method/ Método de busca de dados - GET: -------------------------------\
    fetchData () {
      axios.get(
        'http://localhost:8000',
        {
          headers: {
            Authorization: `Bearer ${this.localStorageToken}`
          }
        }
      ).then(res => {
        this.info = res.data.sort((s1, s2) => s2.id - s1.id);
      }).catch(error => {
        this.validateHttpStatus(error.response.status);
      })
    },
    //////////////////////////////////////////////////////////////////////////////////////

    // Clean/reset d request data/ Método para resetar/limpar os dados de requisição: ---\
    resetData () {
      this.name = '';
      this.picture = '';
      document.getElementById('file').value = '';

      removeElementClass('nameCategory', 'required-red-border');
      removeElementClass('name-category-label', 'campo-obrigatorio-warning');
      removeElementClass('file', 'required-red-border');
      removeElementClass('file-label', 'campo-obrigatorio-warning');
    },
    //////////////////////////////////////////////////////////////////////////////////////

    // Insert data methods/ Métodos de inserção de dados - POST: ------------------------\
    handleFileChange (event) {
      const file = event.target.files[0];
      this.picture = file;
      checkInputValue(this.picture, 'file');
    },
    createDataDB () {
      const formData = new FormData();
      formData.append('name', this.name);
      formData.append('picture', this.picture);

      axios.post('http://localhost:8000', formData,
      {
        headers: {
          Authorization: `Bearer ${this.localStorageToken}`
        }
      })
      .then(res => {
        this.handleLoadingBar(); // Atualiza a lista de Arquivos.
        insertSuccessToast('Arquivo');
      }).catch(error => {
        this.validateHttpStatus(error.response.status);
      });
      this.resetData();
    },
    createData () {

      clickSavecheckRequiredInsertField(this.name, 'nameCategory', 'name-category-label');
      clickSavecheckRequiredInsertField(this.picture, 'file', 'file-label');

      if (this.name && this.picture) {
        this.createDataDB();
      }
    },
    checkInputValue,
    //////////////////////////////////////////////////////////////////////////////////////

    // Delete data method/ Método de deleção de dados - DELETE: -------------------------\
    deleteData (pk) {
      axios.delete(`http://localhost:8000/delete/${pk}`,
      {
        headers: {
          Authorization: `Bearer ${this.localStorageToken}`
        }
      }).then(res => {
        this.fetchData();
        deleteSuccessToast('Arquivo DELETADO com sucesso.')
      }).catch(error => {
        this.validateHttpStatus(error.response.status);
      });
    },
    //////////////////////////////////////////////////////////////////////////////////////

    // Loading bar/ Barra de carregamento: ----------------------------------------------\
    loadingBar () {
      let interval = setInterval(() => {
        if (this.percentage < 100)
          this.percentage += 0.5
        else
          clearInterval(interval)
      })
    },
    handleLoadingBar () {
      this.loadingBar();
      this.loadingB = 'loading';
      setTimeout(() => {
        this.loadingB = '';
      }, 500);

      this.fetchData();
    },
    //////////////////////////////////////////////////////////////////////////////////////

    // (to finish development) Download image method/ Método para baixar a imagem: ------\
    async downloadImage(urlImagem) {
      try {
        const response = await fetch(urlImagem);
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        const link = document.createElement('a');
        link.href = url;
        link.download = 'imagem.jpg';
        link.click();

        window.URL.revokeObjectURL(url);
      } catch (error) {
        console.error('Erro ao baixar a imagem:', error);
      }
    }
    //////////////////////////////////////////////////////////////////////////////////////

  },

  mounted () {
    this.fetchData();
  }

}
</script>

<template>

  <main class="flex">

    <!-- upload form -->
    <div class="form-div">
      <div></div>
      <form class="row row-cols-lg-auto g-3 align-items-center forms">
        <div class="row justify-content-center margin-left-2"> <!-- Centralizar os elementos verticalmente -->

            <div class="col-6">
              <label id="name-category-label" class="visually-hidden" for="nameCategory">Name/Category</label>
              <div class="input-group">
                <input
                  type="text"
                  class="form-control"
                  id="nameCategory"
                  placeholder="Name/Category"
                  v-model="name"
                  @keyup="checkInputValue(name, 'nameCategory')"
                >
              </div>
            </div>
            
            <div class="col-6">
              <label id="file-label" class="visually-hidden" for="file">File</label>
              <div class="input-group">
                <input
                  type="file"
                  class="form-control"
                  id="file"
                  @change="handleFileChange"
                >
              </div>
            </div>

          <div class="col-6 mt-2 buttons-div">
            <div class="">
              <button type="submit" class="btn btn-secondary btn-block" @click="resetData">Cancel</button>
            </div>
            <div class="">
              <button type="submit" class="btn btn-success btn-block" @click="createData">Upload</button>
            </div>
          </div>
        </div>
      </form>
      <div></div>
    </div>

    <SkeletonCardsLoading v-if="this.info == ''" />

    <!-- Card -->
    <div v-if="this.info != ''" class="row row-cols-1 row-cols-md-3 g-4 mt-1">

      <div v-if="this.loadingB != ''" class="col loading">
        <div class="loading-bar loading-info">
          <div>{{ percentage.toFixed() }}%</div>
          <div class="percentage" :style="{'width': percentage + '%'}"></div>
        </div>
      </div>

      <div v-for="(arquivo, i) in info" :key="i" class="col">
        <div class="card">
          <img :src='arquivo.picture' class="card-img-top" :alt="arquivo.name, i">
          <div class="card-body flex-direction-row">
              <!-- <p></p> -->
              <h5 class="card-title texto-centralizado">{{ arquivo.name }}</h5>
              <div>
                <!-- <button
                  class="btn btn-warning"
                  type="button"
                  @click="downloadImage(arquivo.picture)"
                >
                Download
                </button> -->
                <button
                class="btn btn-danger"
                type="button"
                @click="deleteData(Number(arquivo.id))"
                >
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>

  </main>

</template>

<style>

.margin-left-2 {
  margin-left: 1.5px;
}

.texto-centralizado {
  display: flex;
  justify-content: center;
}

.flex {
  display: flex;
  flex-direction: column;
}

.flex-direction-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.form-div {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

.buttons-div {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.loading-info {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}

.loading {
  display: flex;
  justify-content: center;
  /* align-items: center; */
}

.forms {
  display: flex;
  /* justify-content: space-between; */
  /* background-color: #2B3035; */
  background-color: #38424b;
  border-radius: 5px;
  padding: 4px;
  margin-top: 3px;
}

.red-border {
  border: 1px solid red;
}

.loading-bar {
  position: relative;
  width: 300px;
  height: 20px;
  border-radius: 15px;
  overflow: hidden;
  border-bottom: 1px solid #ddd;
  box-shadow: inset 0 1px 2px, 0 -1px 1px #fff, 0 1px 0 #fff; 
  /* rgba($color: #000, $alpha: .4) */
}

.percentage {
  position: absolute;
  top: 1px; left: 1px; right: 1px;
  display: block;
  height: 100%;
  border-radius: 15px;
  background-color: #a5df41;
  background-size: 30px 30px;
  animation: animate-stripes 3s linear infinite;
}

@keyframes piscar {
  0%, 100% {
    border-color: #ff0000;
  }
  50% {
    border-color: #FF69B4;
  }
}

.required-red-border {
  border: 2px solid red;
  animation: piscar 2s infinite;
}

.red-asterisk::after {
  content: " *";
  color: red;
}

.campo-obrigatorio-warning::after {
  content: " * Campo obrigatório";
  color: red;
}
</style>