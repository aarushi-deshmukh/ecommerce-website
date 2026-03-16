<template>
  <div>
    <SellerHeader 
      :searchQuery="searchQuery"
      @update:searchQuery="searchQuery = $event"
      @filter-category="filterCategory"
    />

    <div class="container">
      <div class="page-header">
        <h1>My Products</h1>
        <p class="subtitle">Manage your product inventory</p>
      </div>

      <div v-if="loading" class="loading">
        <div class="loading-spinner"></div>
        <p>Loading products...</p>
      </div>
      
      <div v-else-if="error" class="error">
        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="12" y1="8" x2="12" y2="12"></line>
          <line x1="12" y1="16" x2="12.01" y2="16"></line>
        </svg>
        <p>{{ error }}</p>
      </div>
      
      <div v-else-if="filteredProducts.length === 0" class="empty-state">
        <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        </svg>
        <h3>No products found</h3>
        <p>Try adjusting your search or filter</p>
      </div>

      <div class="product-grid" v-else>
        <div class="product-card" v-for="product in filteredProducts" :key="product.id">
          <div class="product-image">
            <img :src="product.image || '/placeholder-product.jpg'" :alt="product.name" />
          </div>
          <div class="product-info">
            <div class="product-category">{{ product.category }}</div>
            <h3 class="product-name">{{ product.name }}</h3>
            <p class="product-brand">{{ product.brand }}</p>
            <div class="product-details">
              <div class="detail-row">
                <span class="detail-label">Price:</span>
                <span class="detail-value">${{ product.price }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">Quantity:</span>
                <span class="detail-value">{{ product.quantity }}</span>
              </div>
            </div>
            <div class="product-actions">
              <button class="btn-edit" @click="editProduct(product.id)">Edit</button>
              <button class="btn-delete" @click="deleteProduct(product.id)">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, computed, onMounted } from "vue";
import SellerHeader from '@/components/seller-header.vue';

export default {
  components: {
    SellerHeader
  },
  setup() {
    const products = ref([]);
    const searchQuery = ref("");
    const selectedCategory = ref("all");
    const loading = ref(true);
    const error = ref(null);

    const fetchProducts = async () => {
      try {
        loading.value = true;
        const response = await axios.get("http://127.0.0.1:8000/api/products/");
        products.value = response.data;
        error.value = null;
      } catch (err) {
        error.value = "Failed to fetch products. Please try again.";
        console.error("Fetch error:", err);
      } finally {
        loading.value = false;
      }
    };

    const filteredProducts = computed(() => {
      let filtered = products.value;

      // Filter by category
      if (selectedCategory.value !== 'all') {
        filtered = filtered.filter(product =>
          product.category.toLowerCase() === selectedCategory.value.toLowerCase()
        );
      }

      // Filter by search query
      if (searchQuery.value) {
        filtered = filtered.filter(product =>
          product.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          product.brand.toLowerCase().includes(searchQuery.value.toLowerCase())
        );
      }

      return filtered;
    });

    const filterCategory = (category) => {
      selectedCategory.value = category;
    };

    const editProduct = (productId) => {
      console.log('Edit product:', productId);
      // Add edit logic here
    };

    const deleteProduct = (productId) => {
      if (confirm('Are you sure you want to delete this product?')) {
        console.log('Delete product:', productId);
        // Add delete logic here
      }
    };

    onMounted(fetchProducts);

    return { 
      products, 
      searchQuery, 
      loading, 
      error, 
      filteredProducts,
      filterCategory,
      editProduct,
      deleteProduct
    };
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.container {
  margin-top: 90px;
  padding: 40px;
  background-color: #ffffff;
  min-height: calc(100vh - 70px);
}

.page-header {
  margin-bottom: 40px;
}

.page-header h1 {
  font-size: 32px;
  font-weight: 600;
  margin: 0 0 8px 0;
  color: #1a1a1a;
  letter-spacing: -0.5px;
}

.subtitle {
  font-size: 15px;
  color: #6b6b6b;
  margin: 0;
}

/* Loading State */
.loading {
  text-align: center;
  padding: 80px 20px;
  color: #6b6b6b;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #f5f5f0;
  border-top-color: #1a1a1a;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Error State */
.error {
  text-align: center;
  padding: 80px 20px;
  color: #d32f2f;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.error svg {
  stroke: #d32f2f;
}

.error p {
  font-size: 16px;
  margin: 0;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 20px;
  color: #6b6b6b;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.empty-state svg {
  stroke: #d0d0d0;
}

.empty-state h3 {
  font-size: 20px;
  color: #1a1a1a;
  margin: 0;
}

.empty-state p {
  font-size: 15px;
  margin: 0;
}

/* Product Grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
  margin-top: 24px;
}

.product-card {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.product-image {
  width: 100%;
  height: 240px;
  background: #f5f5f5;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-info {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
}

.product-category {
  font-size: 0.75rem;
  font-weight: 600;
  color: #888;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.product-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
  line-height: 1.4;
}

.product-brand {
  font-size: 0.9rem;
  color: #666;
  margin: 0;
}

.product-details {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 12px 0;
  border-top: 1px solid #f0f0f0;
  border-bottom: 1px solid #f0f0f0;
  margin: 8px 0;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.detail-label {
  font-size: 0.9rem;
  color: #666;
  font-weight: 500;
}

.detail-value {
  font-size: 0.9rem;
  color: #1a1a1a;
  font-weight: 600;
}

.product-actions {
  display: flex;
  gap: 8px;
  margin-top: auto;
}

.btn-edit,
.btn-delete {
  flex: 1;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.btn-edit {
  background-color: #1a1a1a;
  color: #ffffff;
}

.btn-edit:hover {
  background-color: #000000;
  transform: translateY(-1px);
}

.btn-delete {
  background-color: transparent;
  color: #d32f2f;
  border: 1px solid #d32f2f;
}

.btn-delete:hover {
  background-color: #d32f2f;
  color: #ffffff;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: 24px 16px;
  }

  .page-header h1 {
    font-size: 28px;
  }

  .product-grid {
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 16px;
  }
}

@media (max-width: 480px) {
  .product-grid {
    grid-template-columns: 1fr;
  }
}
</style>