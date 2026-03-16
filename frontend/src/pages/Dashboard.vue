<template>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

  <div>
    <!-- Navigation Bar -->
    <nav class="navbar">
      <div class="nav-left">
        <div class="logo" @click="goHome">PARS</div>
        <div @click="toggleCategories" class="categories-btn">
          Categories 
          <span class="dropdown-icon" :class="{ rotated: showCategories }">▾</span>
        </div>
      </div>
      
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="Search products..." 
        class="search-bar"
      />
      
      <div class="nav-right">
        <button @click="goToSignIn" class="btn-outline">Sign In</button>
        <button @click="goToSignUp" class="btn-solid">Sign Up</button>
      </div>
    </nav>

    <!-- Categories Dropdown -->
    <transition name="dropdown">
      <div v-if="showCategories" class="categories-dropdown">
        <div 
          v-for="cat in categories" 
          :key="cat.value"
          @click="filterCategory(cat.value)"
          class="category-item"
        >
          {{ cat.label }}
        </div>
      </div>
    </transition>

    <!-- Banner Section -->
    <section class="banner">
      <div class="banner-content">
        <h1>Discover Your Perfect <span style="color: #d2b48c; font-family: cursive;"><i>Style</i></span></h1>
        <p>Explore our curated collection of premium products designed to elevate your lifestyle. From fashion to electronics, find everything you need in one place.</p>
        <div class="banner-features">
          <div class="feature">✓ Free Shipping on Orders</div>
          <div class="feature">✓ 30-Day Easy Returns</div>
          <div class="feature">✓ Exclusive Member Deals</div>
        </div>
        <button class="shop-btn">Shop Now</button>
      </div>
      <div class="banner-images">
        <div class="main-image">
          <img src="/banner-image.jpg" alt="Featured Store" />
        </div>
        <div class="side-images">
          <img src="/side-image1.jpg" alt="Product 1" />
          <img src="/side-image2.jpg" alt="Product 2" />
        </div>
      </div>
    </section>

    <!-- Categories Grid -->
    <section class="category-section">
      <h2 class="section-title">Shop by Category</h2>
      <div class="category-container">
        <button 
          @click="scrollCategories('left')" 
          class="nav-arrow left-arrow"
          v-show="canScrollLeft"
        >
          ‹
        </button>
        
        <div class="category-grid" ref="categoryGrid" @scroll="updateScrollButtons">
          <div 
            v-for="cat in displayCategories" 
            :key="cat.name"
            class="category-card" 
            @click="filterCategory(cat.name)"
          >
            <div class="category-icon">
              <img :src="cat.image" :alt="cat.name" />
            </div>
            <span>{{ cat.name }}</span>
          </div>
        </div>
        
        <button 
          @click="scrollCategories('right')" 
          class="nav-arrow right-arrow"
          v-show="canScrollRight"
        >
          ›
        </button>
      </div>
    </section>

     <!-- Featured Products Section -->
    <section class="featured-section">
      <h2 class="section-title">Featured Products</h2>
      <div class="products-grid">
        <div class="product-card" v-for="product in featuredProducts" :key="product.id">
          <div class="product-image">
            <img :src="product.image" :alt="product.name" />
          </div>
          <div class="product-info">
            <span class="product-category">{{ product.category }}</span>
            <h3 class="product-name">{{ product.name }}</h3>
            <p class="product-description">{{ product.description }}</p>
            <div class="product-footer">
              <span class="product-price">{{ product.price }}</span>
              <button class="add-to-cart-btn">Add to Cart</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-section">
          <h3 class="footer-logo">PARS</h3>
          <p class="footer-desc">Your one-stop destination for premium products and exceptional shopping experience.</p>
          <div class="social-icons">
            <a href="#" class="social-icon"><i class="fa fa-instagram"></i></a>
            <a href="#" class="social-icon"><i class="fa fa-twitter"></i></a>
            <a href="#" class="social-icon"><i class="fa fa-facebook-f"></i></a>
            <a href="#" class="social-icon"><i class="fa fa-telegram"></i></a>
          </div>
        </div>
        
        <div class="footer-section">
          <h4>Shop</h4>
          <ul class="footer-links">
            <li><a href="#">Electronics</a></li>
            <li><a href="#">Clothing</a></li>
            <li><a href="#">Accessories</a></li>
            <li><a href="#">Home Appliances</a></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4>Support</h4>
          <ul class="footer-links">
            <li><a href="#">Contact Us</a></li>
            <li><a href="#">FAQs</a></li>
            <li><a href="#">Shipping Info</a></li>
            <li><a href="#">Returns</a></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4>Company</h4>
          <ul class="footer-links">
            <li><a href="#">About Us</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2025 PARS. All rights reserved.</p>
      </div>
    </footer>

  </div>
</template>

<script>
import axios from 'axios';
import { ref, computed, onMounted, nextTick } from "vue";
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const products = ref([]);
    const searchQuery = ref("");
    const selectedCategory = ref("all");
    const showCategories = ref(false);
    const categoryGrid = ref(null);
    const canScrollLeft = ref(false);
    const canScrollRight = ref(false);

    const categories = [
      { label: 'All Products', value: 'all' },
      { label: 'Electronics', value: 'Electronics' },
      { label: 'Clothing', value: 'Clothing' },
      { label: 'Shoes', value: 'Shoes' },
      { label: 'Accessories', value: 'Accessories' },
      { label: 'Books', value: 'Books' },
      { label: 'Home Appliances', value: 'Home-Appliances' }
    ];

    const displayCategories = [
      { name: 'Electronics', image: '/categories/electronics.jpg' },
      { name: 'Make-up', image: '/categories/makeup.jpg' },
      { name: 'Clothes', image: '/categories/clothes.jpg' },
      { name: 'Shoes', image: '/categories/shoes.jpg' },
      { name: 'Accessories', image: '/categories/accessories.jpg' },
      { name: 'Books', image: '/categories/books.jpg' },
      { name: 'Home Appliances', image: '/categories/home-appliances.jpg' }
    ];

    const featuredProducts = [
      {
        id: 1,
        name: 'Premium Wireless Headphones',
        category: 'ELECTRONICS',
        description: 'High-quality wireless headphones with active noise cancellation',
        price: 'Rs 299.99',
        image: '/products/headphones.jpg'
      },
      {
        id: 2,
        name: 'Luxury Leather Handbag',
        category: 'ACCESSORIES',
        description: 'Elegant leather handbag perfect for any occasion',
        price: 'Rs 449.99',
        image: '/products/handbag.jpg'
      },
      {
        id: 3,
        name: 'Smart Watch Pro',
        category: 'ELECTRONICS',
        description: 'Advanced smartwatch with health tracking features',
        price: 'Rs 399.99',
        image: '/products/watch.jpg'
      }
    ];

    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/products/");
        products.value = response.data;
      } catch (err) {
        console.error("Failed to fetch products:", err);
      }
    };

    const filteredProducts = computed(() => {
      let filtered = products.value;
      
      if (selectedCategory.value !== 'all') {
        filtered = filtered.filter(product =>
          product.category.toLowerCase() === selectedCategory.value.toLowerCase()
        );
      }
      
      if (searchQuery.value) {
        filtered = filtered.filter(product =>
          product.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        );
      }
      
      return filtered;
    });

    const toggleCategories = () => {
      showCategories.value = !showCategories.value;
    };

    const filterCategory = (category) => {
      selectedCategory.value = category;
      showCategories.value = false;
    };

    const scrollCategories = (direction) => {
      const container = categoryGrid.value;
      if (!container) return;
      
      const scrollAmount = 300;
      
      if (direction === 'left') {
        container.scrollLeft -= scrollAmount;
      } else {
        container.scrollLeft += scrollAmount;
      }
      
      updateScrollButtons();  // Update button visibility on scroll
    };

    const updateScrollButtons = () => {
      const container = categoryGrid.value;
      if (!container) return;
      
      canScrollLeft.value = container.scrollLeft > 10;
      canScrollRight.value = 
        container.scrollLeft < (container.scrollWidth - container.clientWidth - 10);
    };

    onMounted(async () => {
      await fetchProducts();
      await nextTick();
      updateScrollButtons();
    });

    const goHome = () => router.push('/');
    const goToSignIn = () => router.push('/signin');
    const goToSignUp = () => router.push('/signup');

    return { 
      searchQuery,
      showCategories,
      categories,
      displayCategories,
      featuredProducts,  // Include featured products in return
      filteredProducts,
      categoryGrid,
      canScrollLeft,
      canScrollRight,
      toggleCategories,
      filterCategory,
      scrollCategories,
      updateScrollButtons,
      goHome,
      goToSignIn,
      goToSignUp
    };
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Navbar */
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
}

.nav-left, .nav-right {
  display: flex;
  align-items: center;
  gap: 24px;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  cursor: pointer;
  color: #1a1a1a;
  letter-spacing: 1px;
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

.search-bar {
  flex: 1;
  max-width: 500px;
  padding: 12px 20px;
  border: 2px solid #e5e5e5;
  border-radius: 24px;
  font-size: 0.95rem;
  outline: none;
  transition: all 0.3s ease;
}

.search-bar:focus {
  border-color: #1a1a1a;
  box-shadow: 0 0 0 3px rgba(26, 26, 26, 0.1);
}

.btn-outline, .btn-solid {
  padding: 10px 24px;
  border-radius: 24px;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid #1a1a1a;
}

.btn-outline {
  background: transparent;
  color: #1a1a1a;
}

.btn-outline:hover {
  background: #f5f5f5;
}

.btn-solid {
  background: #1a1a1a;
  color: #fff;
}

.btn-solid:hover {
  background: #333;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Categories Dropdown */
.categories-dropdown {
  position: fixed;
  top: 70px;
  left: 40px;
  background: #fff;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  padding: 8px;
  border-radius: 12px;
  min-width: 200px;
  z-index: 1100;
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

.dropdown-enter-active, .dropdown-leave-active {
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

/* Banner */
.banner {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 100px 0px 20px;
  background: #fff;
  margin-top: 70px;
  gap: 70px;
}

.banner-content {
  flex: 1;
  max-width: 550px;
}

.banner h1 {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 20px;
  color: #1a1a1a;
  line-height: 1.2;
}

.banner p {
  font-size: 1.1rem;
  margin-bottom: 24px;
  color: #666;
  line-height: 1.7;
}

.banner-features {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 32px;
}

.feature {
  font-size: 0.95rem;
  color: #555;
  font-weight: 500;
}

.shop-btn {
  padding: 16px 48px;
  background-color: #1a1a1a;
  color: #fff;
  border: none;
  border-radius: 30px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.shop-btn:hover {
  background-color: #333;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

.banner-images {
  flex: 1;
  display: flex;
  gap: 16px;
  max-width: 600px;
}

.main-image {
  flex: 1;
}

.main-image img {
  width: 100%;
  height: 480px;
  object-fit: cover;
  border-radius: 16px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

.side-images {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 180px;
}

.side-images img {
  width: 100%;
  height: 232px;
  object-fit: cover;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

/* Category Section */
.category-section {
  padding: 80px 40px;
  background-color: #fff;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 50px;
  color: #1a1a1a;
  text-align: center;
}

.category-container {
  position: relative;
  max-width: 1400px;
  margin: 0 auto;
}

.category-grid {
  display: flex;
  gap: 24px;
  overflow-x: auto;
  scroll-behavior: smooth;
  padding: 0 50px;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.category-grid::-webkit-scrollbar {
  display: none;
}

.nav-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: #fff;
  border: 1px solid #e0e0e0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  font-size: 2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: all 0.3s ease;
  color: #333;
}

.nav-arrow:hover {
  background: #f5f5f5;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

.left-arrow {
  left: 0;
}

.right-arrow {
  right: 0;
}

.category-card {
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  min-width: 250px;
  flex-shrink: 0;
}

.category-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.category-icon {
  width: 100%;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f9f9f9;
  overflow: hidden;
}

.category-icon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.category-card span {
  padding: 16px 20px;
  font-size: 1rem;
  font-weight: 600;
  color: #333;
  text-align: left;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    flex-wrap: wrap;
    padding: 12px 20px;
  }

  .search-bar {
    order: 3;
    width: 100%;
    margin-top: 12px;
  }

  .banner {
    flex-direction: column;
    padding: 100px 30px 60px;
    text-align: center;
  }

  .banner h1 {
    font-size: 2.5rem;
  }

  .banner-features {
    font-size: 0.85rem;
  }

  .category-grid {
    padding: 0 60px;
  }

  .nav-arrow {
    width: 40px;
    height: 40px;
    font-size: 1.5rem;
  }
  
  .category-card {
    min-width: 200px;
  }
}

/* Featured Products Section */
.featured-section {
  padding: 60px 40px;
  background-color: white;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 32px;
  max-width: 1400px;
  margin: 0 auto;
}

.product-card {
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  width: 350px;
  height: 550px;
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
}

.product-image {
  width: 100%;
  overflow: hidden;
  background: #f5f5f5;
}

.product-image img {
  width: 100%;
  object-fit: contain;
  transition: transform 0.4s ease;
}

.product-card:hover .product-image img {
  transform: scale(1.05);
}

.product-info {
  padding: 24px;
}

.product-category {
  font-size: 0.75rem;
  font-weight: 600;
  color: #888;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.product-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a1a1a;
  margin: 8px 0;
}

.product-description {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
}

.product-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.product-price {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
}

.add-to-cart-btn {
  padding: 12px 28px;
  background-color: #1a1a1a;
  color: #fff;
  border: none;
  border-radius: 24px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.add-to-cart-btn:hover {
  background-color: #333;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* Footer */
.footer {
  background-color: white;
  color: black;
  padding: 80px 24px 32px;
  border-top: 1px solid #e5e5e5;
}

.footer-content {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 60px;
  max-width: 1400px;
  margin: 0 auto 40px;
}

.footer-section h3,
.footer-section h4 {
  margin-bottom: 20px;
  font-size: 1.25rem;
}

.footer-logo {
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: 1px;
}

.footer-desc {
  color: gray;
  line-height: 1.7;
  margin-bottom: 24px;
  max-width: 350px;
}

.social-icons {
  display: flex;
  gap: 16px;
}

.social-icon {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  text-decoration: none;
  font-size: 1.2rem;
  transition: all 0.3s ease;
}

.social-icon:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

.footer-links {
  list-style: none;
  padding: 0;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: #aaa;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: #fff;
}

.footer-bottom {
  text-align: center;
  padding-top: 32px;
  border-top: 1px solid #e5e5e5;
  color: #999;
  font-size: 0.9rem;
}

</style>