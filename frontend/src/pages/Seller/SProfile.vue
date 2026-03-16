<template>
  <nav class="navbar">
    <div class="group">
      <div class="logo" @click="goHome">PARS</div>
      <div @click="toggleCategories" class="categories-btn">Categories ▾</div>
    </div>
    <input type="text" v-model="searchQuery" placeholder="Search products..." class="search-bar group" />
    <div class="group">
      <ul class="nav-links">
        <li @click="goToAddProducts">Add Products</li>
        <li @click="goToMyProducts">My Products</li>
        <li>Analysis</li>
        <li @click="goToProfile">Profile</li>
      </ul>
    </div>
  </nav>

  <div class="container">
    <div class="sidebar">
      <div class="profile-image">Profile Image</div>
      <div class="profile-info">
        <span class="profile-name">{{ userProfile.username }}</span><br />
        <span class="mail-id">{{ userProfile.email }}</span>
      </div>
      <ul class="sidebar-links">
        <li>My Profile</li>
        <li>Edit Profile</li>
        <li>Order History</li>
        <li>Settings & Privacy</li>
        <li>Help & Support</li>
        <li @click="logout">Logout</li>
      </ul>
    </div>

    <div class="content">
      <div class="details-container">
        <h2>About</h2>
        <div v-if="loading">Loading profile...</div>
        <div v-else>
          <div class="info-row" v-for="(value, key) in userProfile" :key="key">
            <span class="info-label">{{ formatLabel(key) }}</span><span>{{ value }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";

export default {
  setup() {
    const userProfile = ref({});
    const loading = ref(true);
    const router = useRouter();

    const fetchUserProfile = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/profile/", {
          headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
        });
        userProfile.value = response.data;
      } catch (error) {
        console.error("Error fetching profile:", error);
      } finally {
        loading.value = false;
      }
    };

    const formatLabel = (key) => {
      return key
        .replace(/_/g, " ")
        .replace(/([a-z])([A-Z])/g, "$1 $2")
        .replace(/\b\w/g, (char) => char.toUpperCase());
    };

    const logout = () => {
      localStorage.removeItem("token");
      router.push("/signin");
    };

    onMounted(fetchUserProfile);

    return {
      userProfile,
      loading,
      logout,
      formatLabel
    };
  },

  data() {
    return {
      searchQuery: '',
      selectedCategory: 'all',
      cart: [],
      wishlist: [],
      isSignedIn: false,
      userName: '',
      showCategories: false
    };
  },

  computed: {
    filteredProducts() {
      return this.products?.filter(p =>
        (this.selectedCategory === 'all' || p.category === this.selectedCategory) &&
        p.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      ) || [];
    },
    totalCartItems() {
      return this.cart.length;
    }
  },

  methods: {
    goToAddProducts() {
      window.location.href = '/add-products';
    },
    goToMyProducts() {
      window.location.href = '/my-products';
    },
    goHome() {
      this.$router.push('/seller-dashboard');
    },
    goToProfile() {
      window.location.href = '/seller-profile';
    },
    toggleCategories() {
      this.showCategories = !this.showCategories;
    },
    checkUserStatus() {
      const user = localStorage.getItem('user');
      if (user) {
        this.isSignedIn = true;
        this.userName = JSON.parse(user).name;
      } else {
        this.isSignedIn = false;
      }
    }
  },

  mounted() {
    this.checkUserStatus();
  }
};
</script>

<style>
body {
  background-color: #fafbeb;
  color: rgb(33, 53, 85);
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}

.container {
    display: flex;
    flex-direction: row;
}

.sidebar {
  width: 20vw;
  min-width: 250px;
  max-width: 300px;
  height: 100vh;
  background-color: rgb(245, 239, 231);
  color: rgb(62, 88, 121);
  padding: 20px;
  position: fixed;
  left: 0;
  margin-top: 45px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.profile-image {
  width: 120px;
  height: 120px;
  background-color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 15px;
  margin-top: 30px;
}

.profile-info {
  font-size: 16px;
  margin-bottom: 20px;
}

.sidebar-links {
  list-style: none;
  padding: 0;
  width: 100%;
}

.sidebar-links li {
  padding: 15px;
  background-color: rgb(33, 53, 85);
  color: white;
  margin-bottom: 10px;
  border-radius: 10px;
  cursor: pointer;
  text-align: center;
}

.sidebar-links li:hover {
  background-color: white;
  color: rgb(33, 53, 85);
}

.main-content {
  margin-left: 20vw;
  flex: 1;
  padding: 20px;
  width: 100%;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #2e7d32;
  color: white;
  padding: 30px 20px;
  width: 100vw;
  position: fixed;
  z-index: 1000;
  height: 60px;
  top: 0;
  box-sizing: border-box;
}
.nav-links {
  list-style: none;
  display: flex;
  gap: 30px;
  align-items: center;
  color: white;
}
.navbar input
{
  border-radius: 100px;
}
.search-bar {
  padding: 8px 15px;
  border: 1px solid #ccc;
  width: 50%; 
  font-size: 14px;
  outline: none;
  transition: all 0.3s ease-in-out;
}
.search-bar:focus {
  border-color: #2e7d32;
  box-shadow: 0 0 5px rgba(46, 125, 50, 0.5);
}

.content {
  margin-top: 80px;
  margin-left: 40px;
  background-color: #fafbeb;
  border-radius: 10px;
  padding: 20px;
}

.details-container {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

.details-container h2 {
  margin-bottom: 15px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #ddd;
}

.info-row:last-child {
  border-bottom: none;
}

.info-label {
  font-weight: bold;
  color: #333;
}
</style>