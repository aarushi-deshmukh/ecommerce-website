<template>
  <div>
    <Header
      :searchQuery="searchQuery"
      :wishlistTotal="wishlistTotal"
      :cartTotal="cartTotal"
      @update:searchQuery="searchQuery = $event"
      @filter-category="filterCategory"
    />

    <div class="product-container" v-if="product">
      <div class="product-img-holder">
        <img :src="product.image || 'https://via.placeholder.com/500x500'" :alt="product.name" />
      </div>

      <div class="product-details">
        <div class="product-title">{{ product.name }}</div>
        <div class="product-brandcategory">
          Brand: {{ product.brand }} | Category: {{ product.category }}
        </div>
        <div class="product-price">${{ product.price }}</div>
        <div class="product-quantity">In Stock: {{ product.quantity }}</div>
        <div class="product-description">{{ product.description }}</div>

        <div class="button-group">
          <button class="add-to-cart" @click="addToCart(product.id)">Add to Cart</button>
          <button class="save-later" @click="addToWishlist(product.id)">Save for Later</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      product: null,
      cart: [],
      wishlist: [],
      searchQuery: '',
      showCategories: false
    };
  },
  methods: {
    async fetchProduct() {
      const { name, brand } = this.$route.params;
      const decodedName = decodeURIComponent(name);
      const decodedBrand = decodeURIComponent(brand);
      try {
        const res = await axios.get(`http://127.0.0.1:8000/api/get-product/${decodedName}/${decodedBrand}/`);
        this.product = res.data;
      } catch (err) {
        console.error('Error loading product:', err);
      }
    },
    async fetchCartItems() {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/cart/');
        this.cart = res.data.items;
      } catch (err) {
        console.error('Cart fetch error:', err);
      }
    },
    async fetchWishlistItems() {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/wishlist/');
        this.wishlist = res.data.items;
      } catch (err) {
        console.error('Wishlist fetch error:', err);
      }
    },
    async addToCart(productId) {
      try {
        await axios.post('http://127.0.0.1:8000/api/cart/add/', { product_id: productId });
        this.fetchCartItems();
      } catch (err) {
        console.error('Add to cart error:', err);
      }
    },
    async addToWishlist(productId) {
      try {
        await axios.post('http://127.0.0.1:8000/api/wishlist/add/', { product_id: productId });
        this.fetchWishlistItems();
      } catch (err) {
        console.error('Add to wishlist error:', err);
      }
    },
    toggleCategories() {
      this.showCategories = !this.showCategories;
    }
  },
  mounted() {
    this.fetchProduct();
    this.fetchCartItems();
    this.fetchWishlistItems();
  }
};
</script>

<style>
/* PRODUCT CONTAINER */
.product-container {
  display: flex;
  max-width: 1200px;
  margin: 100px auto;
  background: rgb(248, 244, 240);
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.product-img-holder {
  flex: 0.5;
  padding: 20px;
  border: 3px solid black;
  border-radius: 6px;
  max-width: 100%;
}

.product-details {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.product-title {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #213555;
}

.product-brandcategory {
  color: #555;
  margin-bottom: 20px;
}

.product-price {
  font-size: 1.8rem;
  color: #b12704;
  margin-bottom: 10px;
}

.product-quantity {
  margin-bottom: 15px;
}

.product-description {
  font-size: 1rem;
  margin-bottom: 30px;
}

.button-group {
  display: flex;
  gap: 10px;
}

.add-to-cart,
.save-later {
  padding: 10px 25px;
  font-size: 1rem;
  border-radius: 8px;
  background-color: #3e5879c6;
  color: #000;
  cursor: pointer;
  transition: background-color 0.2s;
}

.add-to-cart:hover,
.save-later:hover {
  background-color: #2c3e50;
  color: white;
}
</style>
