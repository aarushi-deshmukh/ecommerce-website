<template>
  <div>
    <SellerHeader 
      :searchQuery="searchQuery"
      @update:searchQuery="searchQuery = $event"
      @filter-category="filterCategory"
    />

    <div class="container">
      <div class="page-header">
        <div>
          <h1>My Products</h1>
          <p class="subtitle">Manage and track your product inventory</p>
        </div>
        <button @click="goToAddProducts" class="btn-add-product">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Add Product
        </button>
      </div>

      <div v-if="loading" class="loading">
        <div class="loading-spinner"></div>
        <p>Loading products...</p>
      </div>

      <div v-else-if="filteredProducts.length === 0" class="empty-state">
        <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        </svg>
        <h3>No products found</h3>
        <p>Start by adding your first product</p>
        <button @click="goToAddProducts" class="btn-add-first">Add Your First Product</button>
      </div>

      <div v-else class="table-container">
        <table class="products-table">
          <thead>
            <tr>
              <th>Brand</th>
              <th>Product Name</th>
              <th>Category</th>
              <th>Quantity</th>
              <th>Price</th>
              <th class="actions-header">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="product in filteredProducts" :key="product.id">
              <td>
                <span class="brand-text">{{ product.brand }}</span>
              </td>
              <td>
                <span class="product-name">{{ product.name }}</span>
              </td>
              <td>
                <span class="category-badge">{{ product.category }}</span>
              </td>
              <td>
                <span class="quantity-text">{{ product.quantity }}</span>
              </td>
              <td>
                <span class="price-text">₹{{ formatPrice(product.price) }}</span>
              </td>
              <td class="actions-cell">
                <button @click="editProduct(product)" class="btn-action btn-edit" title="Edit">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                  </svg>
                </button>
                <button @click="confirmRemoveProduct(product)" class="btn-action btn-delete" title="Delete">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Confirmation Modal -->
    <div v-if="showDeleteModal" class="modal-overlay" @click="showDeleteModal = false">
      <div class="modal-content" @click.stop>
        <h3>Delete Product</h3>
        <p>Are you sure you want to delete <strong>{{ productToDelete?.name }}</strong>?</p>
        <div class="modal-actions">
          <button @click="showDeleteModal = false" class="btn-modal-cancel">Cancel</button>
          <button @click="removeProduct" class="btn-modal-delete">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
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
    const showDeleteModal = ref(false);
    const productToDelete = ref(null);
    const router = useRouter();

    const fetchProducts = async () => {
      try {
        loading.value = true;
        const response = await axios.get("http://127.0.0.1:8000/api/products/");
        products.value = response.data;
      } catch (error) {
        console.error("Error fetching products:", error);
      } finally {
        loading.value = false;
      }
    };

    const confirmRemoveProduct = (product) => {
      productToDelete.value = product;
      showDeleteModal.value = true;
    };

    const removeProduct = async () => {
      try {
        const product = productToDelete.value;
        await axios.delete(`http://127.0.0.1:8000/api/remove-product/${product.name}/${product.brand}/`);
        products.value = products.value.filter(p => p.id !== product.id);
        showDeleteModal.value = false;
        productToDelete.value = null;
      } catch (error) {
        console.error("Error removing product:", error);
        alert("Failed to delete product. Please try again.");
      }
    };

    const editProduct = (product) => {
      console.log('Edit product:', product);
      // Add edit functionality here
    };

    const formatPrice = (price) => {
      return parseFloat(price).toFixed(2);
    };

    onMounted(fetchProducts);

    const filteredProducts = computed(() =>
      products.value.filter(product =>
        (selectedCategory.value === "all" || product.category.toLowerCase() === selectedCategory.value.toLowerCase()) &&
        (product.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
         product.brand.toLowerCase().includes(searchQuery.value.toLowerCase()))
      )
    );

    const filterCategory = (category) => {
      selectedCategory.value = category;
    };

    const goToAddProducts = () => {
      router.push("/add-products");
    };

    return {
      products,
      searchQuery,
      selectedCategory,
      loading,
      showDeleteModal,
      productToDelete,
      filteredProducts,
      filterCategory,
      goToAddProducts,
      confirmRemoveProduct,
      removeProduct,
      editProduct,
      formatPrice
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
  padding: 48px 64px;
  background-color: #ffffff;
  min-height: calc(100vh - 70px);
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
}

.page-header h1 {
  font-size: 28px;
  font-weight: 600;
  margin: 0 0 6px 0;
  color: #1a1a1a;
}

.subtitle {
  font-size: 14px;
  color: #737373;
  margin: 0;
}

.btn-add-product {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background-color: #1a1a1a;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-add-product:hover {
  background-color: #000000;
  transform: translateY(-1px);
}

/* Loading State */
.loading {
  text-align: center;
  padding: 80px 20px;
  color: #737373;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.loading-spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #f0f0f0;
  border-top-color: #1a1a1a;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.empty-state svg {
  stroke: #d4d4d4;
}

.empty-state h3 {
  font-size: 20px;
  color: #1a1a1a;
  margin: 0;
}

.empty-state p {
  font-size: 14px;
  color: #737373;
  margin: 0;
}

.btn-add-first {
  margin-top: 8px;
  padding: 10px 24px;
  background-color: #1a1a1a;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-add-first:hover {
  background-color: #000000;
}

/* Table */
.table-container {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  overflow: hidden;
}

.products-table {
  width: 100%;
  border-collapse: collapse;
}

.products-table thead {
  background-color: #fafafa;
  border-bottom: 1px solid #e5e5e5;
}

.products-table th {
  padding: 14px 20px;
  text-align: left;
  font-size: 13px;
  font-weight: 600;
  color: #737373;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.actions-header {
  text-align: center;
}

.products-table tbody tr {
  border-bottom: 1px solid #f5f5f5;
  transition: background-color 0.2s ease;
}

.products-table tbody tr:hover {
  background-color: #fafafa;
}

.products-table tbody tr:last-child {
  border-bottom: none;
}

.products-table td {
  padding: 16px 20px;
  font-size: 14px;
  color: #1a1a1a;
}

.brand-text {
  font-weight: 500;
  color: #1a1a1a;
}

.product-name {
  color: #1a1a1a;
}

.category-badge {
  display: inline-block;
  padding: 4px 12px;
  background-color: #f5f5f5;
  color: #737373;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
  text-transform: capitalize;
}

.quantity-text {
  color: #737373;
}

.price-text {
  font-weight: 600;
  color: #1a1a1a;
}

.actions-cell {
  text-align: center;
}

.btn-action {
  padding: 8px;
  border: 1px solid #e5e5e5;
  border-radius: 6px;
  background-color: #ffffff;
  cursor: pointer;
  transition: all 0.2s ease;
  margin: 0 4px;
}

.btn-action:hover {
  background-color: #fafafa;
  transform: translateY(-1px);
}

.btn-edit svg {
  stroke: #737373;
}

.btn-edit:hover {
  border-color: #1a1a1a;
}

.btn-edit:hover svg {
  stroke: #1a1a1a;
}

.btn-delete svg {
  stroke: #dc2626;
}

.btn-delete:hover {
  border-color: #dc2626;
  background-color: #fef2f2;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.modal-content {
  background: #ffffff;
  border-radius: 12px;
  padding: 32px;
  max-width: 440px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal-content h3 {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 12px 0;
}

.modal-content p {
  font-size: 14px;
  color: #737373;
  margin: 0 0 24px 0;
  line-height: 1.6;
}

.modal-content p strong {
  color: #1a1a1a;
}

.modal-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.btn-modal-cancel,
.btn-modal-delete {
  padding: 10px 24px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.btn-modal-cancel {
  background-color: #ffffff;
  color: #1a1a1a;
  border: 1px solid #d4d4d4;
}

.btn-modal-cancel:hover {
  background-color: #fafafa;
}

.btn-modal-delete {
  background-color: #dc2626;
  color: #ffffff;
}

.btn-modal-delete:hover {
  background-color: #b91c1c;
}

/* Responsive */
@media (max-width: 968px) {
  .container {
    padding: 32px 24px;
  }

  .page-header {
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
  }

  .btn-add-product {
    width: 100%;
    justify-content: center;
  }

  .table-container {
    overflow-x: auto;
  }

  .products-table {
    min-width: 800px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 24px 16px;
  }

  .page-header h1 {
    font-size: 24px;
  }
}
</style>