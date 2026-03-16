<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// Props
const props = defineProps({
  searchQuery: {
    type: String,
    default: ""
  }
});

// Emits
const emit = defineEmits(['update:searchQuery', 'filter-category']);

// State
const showCategoryDropdown = ref(false);

// Categories list
const categories = ref([
  { label: 'All', value: 'all' },
  { label: 'T-Shirts', value: 'T-Shirts' },
  { label: 'Shoes', value: 'Shoes' },
  { label: 'Accessories', value: 'Accessories' },
  { label: 'Jackets', value: 'Jackets' },
  { label: 'Watches', value: 'Watches' },
  { label: 'Bags', value: 'Bags' }
]);

// Functions
function toggleCategories() {
  showCategoryDropdown.value = !showCategoryDropdown.value;
}

function selectCategory(category) {
  emit('filter-category', category);
  showCategoryDropdown.value = false;
}

function onSearchInput(event) {
  emit('update:searchQuery', event.target.value);
}

function goHome() {
  router.push('/seller-dashboard');
}

function goToAddProducts() {
  router.push('/add-products');
}

function goToMyProducts() {
  router.push('/my-products');
}

function goToAnalysis() {
  router.push('/analysis');
}

function goToProfile() {
  router.push('/seller-profile');
}
</script>

<template>
  <div>
    <nav class="navbar">
      <div class="nav-left">
        <div class="logo" @click="goHome">PARS</div>
        <div class="categories-wrapper">
          <div @click="toggleCategories" class="categories-btn">
            Categories 
            <span class="dropdown-icon" :class="{ rotated: showCategoryDropdown }">▾</span>
          </div>
          <transition name="dropdown">
            <div v-if="showCategoryDropdown" class="category-dropdown">
              <div 
                v-for="cat in categories" 
                :key="cat.value"
                @click="selectCategory(cat.value)"
                class="category-item"
              >
                {{ cat.label }}
              </div>
            </div>
          </transition>
        </div>
      </div>

      <div class="search-wrapper">
        <input
          type="text"
          :value="searchQuery"
          @input="onSearchInput"
          placeholder="Search products..."
          class="search-bar"
        />
      </div>

      <div class="nav-right">
        <ul class="nav-links">
          <li @click="goToAddProducts">Add Products</li>
          <li @click="goToMyProducts">My Products</li>
          <li @click="goToAnalysis">Analysis</li>
          <li @click="goToProfile">Profile</li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<style scoped>
/* NAVBAR */
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #fff;
  padding: 16px 40px;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  height: 70px;
  box-sizing: border-box;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 24px;
}

.nav-right {
  display: flex;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  cursor: pointer;
  color: #1a1a1a;
  letter-spacing: 1px;
}

/* Categories Dropdown */
.categories-wrapper {
  position: relative;
}

.categories-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  padding: 8px 16px;
  border-radius: 8px;
  transition: background-color 0.2s;
  font-weight: 500;
  color: #333;
  user-select: none;
}

.categories-btn:hover {
  background-color: #f5f5f5;
}

.dropdown-icon {
  transition: transform 0.3s ease;
  display: inline-block;
}

.dropdown-icon.rotated {
  transform: rotate(180deg);
}

.category-dropdown {
  position: absolute;
  top: calc(100% + 10px);
  left: 0;
  background: #fff;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  padding: 8px;
  border-radius: 12px;
  min-width: 200px;
  z-index: 1100;
  border: 1px solid #e5e5e5;
}

.category-item {
  padding: 12px 16px;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.2s;
  font-weight: 500;
  color: #333;
}

.category-item:hover {
  background-color: #f5f5f5;
}

/* Dropdown Animation */
.dropdown-enter-active, 
.dropdown-leave-active {
  transition: all 0.3s ease;
}

.dropdown-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}

/* Search Bar */
.search-wrapper {
  flex: 1;
  max-width: 500px;
  margin: 0 32px;
}

.search-bar {
  width: 100%;
  padding: 12px 20px;
  border: 2px solid #e5e5e5;
  border-radius: 24px;
  font-size: 0.95rem;
  outline: none;
  transition: all 0.3s ease;
  background-color: #ffffff;
  color: #1a1a1a;
}

.search-bar:focus {
  border-color: #1a1a1a;
  box-shadow: 0 0 0 3px rgba(26, 26, 26, 0.1);
}

.search-bar::placeholder {
  color: #aaa;
}

/* Nav Links */
.nav-links {
  list-style: none;
  display: flex;
  gap: 30px;
  color: #1a1a1a;
  cursor: pointer;
  margin: 0;
  padding: 0;
  align-items: center;
}

.nav-links li {
  transition: color 0.2s;
  position: relative;
  font-weight: 500;
  font-size: 0.95rem;
}

.nav-links li:hover {
  color: #666;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .navbar {
    padding: 16px 24px;
  }

  .nav-left {
    gap: 16px;
  }

  .search-wrapper {
    max-width: 400px;
    margin: 0 24px;
  }

  .nav-links {
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
    padding: 12px 20px;
    height: auto;
  }

  .nav-left {
    width: 100%;
    justify-content: space-between;
    margin-bottom: 12px;
  }

  .search-wrapper {
    width: 100%;
    max-width: 100%;
    margin: 0;
    order: 3;
  }

  .nav-right {
    width: 100%;
    margin-top: 12px;
  }

  .nav-links {
    width: 100%;
    justify-content: space-between;
    gap: 12px;
    font-size: 0.85rem;
  }

  .category-dropdown {
    max-height: 300px;
    overflow-y: auto;
  }
}
</style>