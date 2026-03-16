<template>
  <div class="container">
    <div class="left-side">
      <div class="content-wrapper">
        <h1 class="main-title">Welcome Back</h1>
        <p class="subtitle">Sign in to access your account and continue shopping.</p>
      </div>
    </div>

    <div class="right-side">
      <div class="form-wrapper">
        <router-link to="/" class="back-link">← Back to Home</router-link>
        
        <div class="tabs-container">
          <router-link 
            :to="'/signup'" 
            :class="['tab-link', { active: activeTab === 'signup' }]" 
            @click="activeTab = 'signup'"
          >
            Sign Up
          </router-link>
          <router-link 
            :to="'/signin'" 
            :class="['tab-link', { active: activeTab === 'signin' }]" 
            @click="activeTab = 'signin'"
          >
            Sign In
          </router-link>
        </div>

        <SigninForm />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import SigninForm from "@/components/signin-form.vue";

const activeTab = ref("signin");

</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
  display: flex;
  min-height: 100vh;
  width: 100vw;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.left-side {
  width: 45%;
  position: relative;
  background-image: url('/background-image.jpg');
  background-size: cover;
  background-position: center;
  overflow: hidden;
}

.content-wrapper {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem 3rem;
  color: white;
}

.main-title {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  color: #ffffff;
  text-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
}

.subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
  max-width: 400px;
  font-weight: 400;
}

.right-side {
  width: 55%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ffffff;
  padding: 3rem 2rem;
  position: relative;
}

.form-wrapper {
  width: 100%;
  max-width: 480px;
}

.back-link {
  display: inline-flex;
  align-items: center;
  color: #666;
  text-decoration: none;
  font-size: 0.9rem;
  margin-bottom: 2rem;
  transition: color 0.3s ease;
}

.back-link:hover {
  color: #1a1a1a;
}

.tabs-container {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
  border-bottom: 2px solid #f0f0f0;
}

.tab-link {
  flex: 1;
  text-align: center;
  padding: 1rem;
  color: #999;
  text-decoration: none;
  font-size: 1rem;
  font-weight: 500;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  transition: all 0.3s ease;
}

.tab-link:hover {
  color: #1a1a1a;
}

.tab-link.active {
  color: #1a1a1a;
  border-bottom-color: #1a1a1a;
  font-weight: 600;
}

@media (max-width: 1024px) {
  .container {
    flex-direction: column;
  }
  
  .left-side {
    width: 100%;
    min-height: 40vh;
  }
  
  .content-wrapper {
    padding: 2rem 1.5rem;
  }
  
  .main-title {
    font-size: 2.5rem;
  }
  
  .subtitle {
    font-size: 1.1rem;
  }
  
  .right-side {
    width: 100%;
    padding: 2rem 1.5rem;
  }
}

@media (max-width: 640px) {
  .main-title {
    font-size: 2rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .form-wrapper {
    max-width: 100%;
  }
}
</style>