<template>
  <Header v-if="!isAuthPage" />
  <router-view />
  <Footer v-if="!isAuthPage" />
</template>

<script setup>
import { useRoute } from "vue-router"
import { computed } from "vue"
import Header from "@/components/header.vue"
import Footer from "@/components/footer.vue"

const route = useRoute()

const isAuthPage = computed(() =>
  route.path === "/signin" || route.path === "/signup"
)
</script>

<style>
#app {
  height: 100vh;
  width: 100vw;
  background-color: white;
}

body {
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
}

.app-container {
  display: flex;
  flex-direction: column;
}
</style>