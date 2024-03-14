<template>
  <main class=" flex">

    <!-- Cards -->
    <div class="row row-cols-1 row-cols-md-3 g-4 mt-1">
      <div v-for="(arquivo, i) in 9" :key="i" class="col">
        <div class="card loading-elements bigger-cards">
          <div class="card-body flex-direction-row">
              <h5 class="card-title texto-centralizado loading-elements"></h5>
              <div>
                <button
                class="btn loading-elements"
                type="button"
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
.loading-elements {
  border-radius: 5px;
  animation: pulse-bg 1.5s infinite, pulse-text 1.5s infinite;
}

.bigger-cards {
  height: 300px;
}

@keyframes pulse-bg {
  0% {
    background-color: #f0f0f0;
  }
  50% {
    background-color: #bcbcbc;
  }
  100% {
    background-color: #f0f0f0;
  }
}

@keyframes pulse-text {
  0% {
    color: #f0f0f0;
  }
  50% {
    color: #bcbcbc;
  }
  100% {
    color: #f0f0f0;
  }
}
</style>