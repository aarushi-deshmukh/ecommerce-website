<template>
  <div>
    <SellerHeader 
      :searchQuery="searchQuery"
      @update:searchQuery="searchQuery = $event"
    />

    <div class="container">
      <div class="page-header">
        <h1>Add New Product</h1>
        <p class="subtitle">Fill in the details to add a product to your inventory</p>
      </div>

      <div class="content-wrapper">
        <div class="form-section">
          <form @submit.prevent="addProduct" class="product-form">
            <div class="form-group">
              <label>Product Name <span class="required">*</span></label>
              <input 
                type="text" 
                v-model="newProduct.name" 
                placeholder="Enter product name"
                required
              >
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>Price <span class="required">*</span></label>
                <input 
                  type="number" 
                  v-model="newProduct.price" 
                  placeholder="0.00"
                  step="0.01"
                  required
                >
              </div>

              <div class="form-group">
                <label>Brand <span class="required">*</span></label>
                <input 
                  type="text" 
                  v-model="newProduct.brand" 
                  placeholder="Enter brand name"
                  required
                >
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>Category <span class="required">*</span></label>
                <select v-model="newProduct.category" required>
                  <option value="" disabled>Select Category</option>
                  <option value="clothing">Clothing</option>
                  <option value="shoes">Shoes</option>
                  <option value="accessories">Accessories</option>
                  <option value="books">Books</option>
                  <option value="home-appliances">Home Appliances</option>
                  <option value="electronics">Electronics</option>
                </select>
              </div>

              <div class="form-group">
                <label>Quantity <span class="required">*</span></label>
                <input 
                  type="number" 
                  v-model="newProduct.quantity" 
                  placeholder="0"
                  min="0"
                  required
                >
              </div>
            </div>

            <div class="form-group">
              <label>Description <span class="required">*</span></label>
              <textarea 
                v-model="newProduct.description" 
                placeholder="Describe your product in detail..."
                rows="6"
                required
              ></textarea>
            </div>

            <div class="form-actions">
              <button type="button" @click="goToMyProducts" class="btn-cancel">
                Cancel
              </button>
              <button type="submit" class="btn-publish" :disabled="isPublishing">
                {{ publishMessage }}
              </button>
            </div>
          </form>
        </div>

        <div class="image-section">
          <div class="image-upload-card">
            <h3>Product Image</h3>
            <div 
              class="image-upload-box"
              @click="triggerFileInput"
              @dragover.prevent="isDragging = true"
              @dragleave.prevent="isDragging = false"
              @drop.prevent="handleDrop"
              :class="{ 'dragging': isDragging }"
            >
              <input 
                type="file" 
                ref="fileInput" 
                @change="handleFileSelect"
                accept="image/*"
                style="display: none"
              >
              
              <div v-if="!imagePreview" class="upload-placeholder">
                <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <circle cx="8.5" cy="8.5" r="1.5"></circle>
                  <polyline points="21 15 16 10 5 21"></polyline>
                </svg>
                <p class="upload-text">Click to upload or drag and drop</p>
                <p class="upload-hint">PNG, JPG or JPEG (max. 5MB)</p>
              </div>

              <div v-else class="image-preview">
                <img :src="imagePreview" alt="Product preview">
                <button @click.stop="removeImage" class="remove-image-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <div class="tips-card">
            <h4>Tips for a great listing</h4>
            <ul>
              <li>Use clear, high-quality images</li>
              <li>Write detailed descriptions</li>
              <li>Set competitive prices</li>
              <li>Keep inventory updated</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';
import SellerHeader from '@/components/seller-header.vue';

export default {
  components: {
    SellerHeader
  },
  setup() {
    const searchQuery = ref('');
    const publishMessage = ref('Publish Product');
    const isPublishing = ref(false);
    const imagePreview = ref(null);
    const isDragging = ref(false);
    const fileInput = ref(null);
    
    const newProduct = ref({
      name: '',
      price: '',
      brand: '',
      category: '',
      quantity: '',
      description: '',
      image: null
    });

    const triggerFileInput = () => {
      fileInput.value.click();
    };

    const handleFileSelect = (event) => {
      const file = event.target.files[0];
      if (file) {
        processFile(file);
      }
    };

    const handleDrop = (event) => {
      isDragging.value = false;
      const file = event.dataTransfer.files[0];
      if (file && file.type.startsWith('image/')) {
        processFile(file);
      }
    };

    const processFile = (file) => {
      if (file.size > 5 * 1024 * 1024) {
        alert('File size must be less than 5MB');
        return;
      }

      newProduct.value.image = file;
      const reader = new FileReader();
      reader.onload = (e) => {
        imagePreview.value = e.target.result;
      };
      reader.readAsDataURL(file);
    };

    const removeImage = () => {
      imagePreview.value = null;
      newProduct.value.image = null;
      if (fileInput.value) {
        fileInput.value.value = '';
      }
    };

    const addProduct = async () => {
      isPublishing.value = true;
      publishMessage.value = 'Publishing...';

      try {
        const formData = new FormData();
        Object.keys(newProduct.value).forEach(key => {
          if (newProduct.value[key]) {
            formData.append(key, newProduct.value[key]);
          }
        });

        await axios.post('http://127.0.0.1:8000/api/add-product/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        publishMessage.value = 'Published!';
        setTimeout(() => {
          window.location.href = '/my-products';
        }, 1000);
      } catch (error) {
        console.error('Error adding product:', error);
        publishMessage.value = 'Publish Product';
        isPublishing.value = false;
        alert('Failed to publish product. Please try again.');
      }
    };

    const goToMyProducts = () => {
      window.location.href = '/my-products';
    };

    return {
      searchQuery,
      publishMessage,
      isPublishing,
      newProduct,
      imagePreview,
      isDragging,
      fileInput,
      triggerFileInput,
      handleFileSelect,
      handleDrop,
      removeImage,
      addProduct,
      goToMyProducts
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
  background-color: #fafafa;
  min-height: calc(100vh - 70px);
}

.page-header {
  margin-bottom: 40px;
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
  font-weight: 400;
}

.content-wrapper {
  display: grid;
  grid-template-columns: 1fr 420px;
  gap: 32px;
  max-width: 1400px;
}

/* Form Section */
.form-section {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  padding: 32px;
}

.product-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 500;
  color: #1a1a1a;
  font-size: 14px;
}

.required {
  color: #dc2626;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 10px 14px;
  border: 1px solid #d4d4d4;
  border-radius: 8px;
  font-size: 14px;
  font-family: inherit;
  transition: all 0.2s ease;
  background-color: #ffffff;
  color: #1a1a1a;
}

.form-group input::placeholder,
.form-group textarea::placeholder {
  color: #a3a3a3;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #737373;
  box-shadow: 0 0 0 3px rgba(115, 115, 115, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
  font-family: inherit;
  line-height: 1.5;
}

.form-group select {
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23666' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 36px;
}

.form-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 8px;
  padding-top: 24px;
  border-top: 1px solid #f0f0f0;
}

.btn-publish,
.btn-cancel {
  padding: 10px 24px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.btn-cancel {
  background-color: #ffffff;
  color: #1a1a1a;
  border: 1px solid #d4d4d4;
}

.btn-cancel:hover {
  background-color: #fafafa;
  border-color: #a3a3a3;
}

.btn-publish {
  background-color: #1a1a1a;
  color: #ffffff;
  min-width: 140px;
}

.btn-publish:hover:not(:disabled) {
  background-color: #000000;
}

.btn-publish:disabled {
  background-color: #a3a3a3;
  cursor: not-allowed;
}

/* Image Section */
.image-section {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.image-upload-card,
.tips-card {
  background: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 12px;
  padding: 24px;
}

.image-upload-card h3 {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 16px 0;
}

.tips-card h4 {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 16px 0;
}

.image-upload-box {
  width: 100%;
  height: 280px;
  border: 2px dashed #d4d4d4;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
  background-color: #fafafa;
}

.image-upload-box:hover {
  border-color: #a3a3a3;
  background-color: #f5f5f5;
}

.image-upload-box.dragging {
  border-color: #737373;
  background-color: #f0f0f0;
}

.upload-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 20px;
}

.upload-placeholder svg {
  stroke: #d4d4d4;
  margin-bottom: 16px;
}

.upload-text {
  font-size: 14px;
  font-weight: 500;
  color: #1a1a1a;
  margin: 0 0 4px 0;
}

.upload-hint {
  font-size: 13px;
  color: #a3a3a3;
  margin: 0;
}

.image-preview {
  width: 100%;
  height: 100%;
  position: relative;
}

.image-preview img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background-color: #ffffff;
}

.remove-image-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  background: rgba(0, 0, 0, 0.6);
  border: none;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.remove-image-btn:hover {
  background: rgba(0, 0, 0, 0.8);
}

.remove-image-btn svg {
  stroke: #ffffff;
}

.tips-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.tips-card li {
  padding: 10px 0;
  color: #737373;
  font-size: 14px;
  border-bottom: 1px solid #f5f5f5;
  position: relative;
  padding-left: 24px;
}

.tips-card li:last-child {
  border-bottom: none;
}

.tips-card li:before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #1a1a1a;
  font-weight: 600;
  font-size: 14px;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .content-wrapper {
    grid-template-columns: 1fr;
  }

  .image-section {
    order: -1;
  }
}

@media (max-width: 768px) {
  .container {
    padding: 24px 16px;
  }

  .page-header h1 {
    font-size: 24px;
  }

  .form-section {
    padding: 24px 20px;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .form-actions {
    flex-direction: column-reverse;
  }

  .btn-publish,
  .btn-cancel {
    width: 100%;
  }

  .image-upload-box {
    height: 240px;
  }
}
</style>