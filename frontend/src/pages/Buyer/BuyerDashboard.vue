<template>
  <div class="dashboard">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-content">
        <h1>Discover Amazing Products</h1>
        <p>Shop the latest trends with exclusive deals</p>
      </div>
    </section>

    <!-- Products Section -->
    <section class="products-section">
      <div class="section-header">
        <h2 class="section-title">Featured Products</h2>
        <div class="filter-chips">
          <button
            :class="['chip', { active: selectedCategory === 'all' }]"
            @click="filterCategory('all')"
          >
            All
          </button>
          <button
            v-for="category in categories"
            :key="category"
            :class="['chip', { active: selectedCategory === category }]"
            @click="filterCategory(category)"
          >
            {{ category }}
          </button>
        </div>
      </div>

      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Loading products...</p>
      </div>

      <div v-else-if="error" class="error">{{ error }}</div>

      <div class="product-grid" v-else>
        <div class="product-card" v-for="product in filteredProducts" :key="product.id">
          <div class="image-zone" @click="getProduct(product)">
            <img :src="product.image" :alt="product.name" class="product-img" />
            <button
              class="wishlist-btn"
              @click.stop="addToWishlist(product)"
              :class="{ active: product.saved }"
            >
              <svg viewBox="0 0 24 24">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </button>
            <span class="category-tag">{{ product.category }}</span>
          </div>

          <div class="card-body">
            <div class="product-brand">{{ product.brand }}</div>
            <h3 class="product-name" @click="getProduct(product)">{{ product.name }}</h3>

            <div class="divider"></div>

            <div class="price-row">
              <span class="price">₹{{ product.price }}</span>
              <span class="stock-badge" :class="{ low: product.quantity < 10 }">
                {{ product.quantity }} in stock
              </span>
            </div>

            <div class="qty-row">
              <span class="qty-label">Qty</span>
              <div class="qty-control">
                <button class="qty-btn" @click.stop="changeQty(product, -1)">−</button>
                <span class="qty-num">{{ product.userQuantity }}</span>
                <button class="qty-btn" @click.stop="changeQty(product, 1)">+</button>
              </div>
            </div>

            <button
              class="add-btn"
              @click.stop="addToCart(product)"
              :disabled="product.added"
            >
              <svg v-if="!product.added" viewBox="0 0 24 24">
                <circle cx="9" cy="21" r="1"></circle>
                <circle cx="20" cy="21" r="1"></circle>
                <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
              </svg>
              <svg v-else viewBox="0 0 24 24">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
              <span>{{ product.added ? 'Added to Cart' : 'Add to Cart' }}</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Categories Section -->
    <section class="categories-showcase">
      <h2 class="categories-title">Shop by Category</h2>
      <div class="categories-grid">
        <div
          v-for="category in displayCategories"
          :key="category.name"
          @click="filterCategory(category.name)"
          class="category-showcase-card"
        >
          <div class="category-image-wrapper">
            <img :src="category.image" :alt="category.name" class="category-showcase-img" />
          </div>
          <h3 class="category-showcase-name">{{ category.name }}</h3>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features-section">
      <div class="feature">
        <div class="feature-icon">📦</div>
        <h3>Free Shipping</h3>
        <p>On orders over ₹999</p>
      </div>
      <div class="feature">
        <div class="feature-icon">🔒</div>
        <h3>Secure Payment</h3>
        <p>100% protected payments</p>
      </div>
      <div class="feature">
        <div class="feature-icon">↩</div>
        <h3>Easy Returns</h3>
        <p>30-day return policy</p>
      </div>
      <div class="feature">
        <div class="feature-icon">💬</div>
        <h3>24/7 Support</h3>
        <p>Dedicated customer service</p>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-section">
          <h3 class="footer-logo">PARS</h3>
          <p>Your one-stop destination for premium products and exceptional shopping experience.</p>
          <div class="social-links">
            <a href="#" class="social-icon"><i class="fa fa-instagram"></i></a>
            <a href="#" class="social-icon"><i class="fa fa-twitter"></i></a>
            <a href="#" class="social-icon"><i class="fa fa-facebook-f"></i></a>
            <a href="#" class="social-icon"><i class="fa fa-telegram"></i></a>
          </div>
        </div>
        <div class="footer-section">
          <h4>Shop</h4>
          <ul>
            <li><a href="#">Electronics</a></li>
            <li><a href="#">Fashion</a></li>
            <li><a href="#">Home & Living</a></li>
            <li><a href="#">Beauty</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h4>Support</h4>
          <ul>
            <li><a href="#">Contact Us</a></li>
            <li><a href="#">FAQs</a></li>
            <li><a href="#">Shipping Info</a></li>
            <li><a href="#">Returns</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h4>Company</h4>
          <ul>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2025 PARS. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script>
import { ref, computed, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  setup() {
    const router = useRouter();
    const products = ref([]);
    const searchQuery = ref("");
    const loading = ref(true);
    const error = ref(null);
    const cartTotal = ref(0);
    const wishlistTotal = ref(0);
    const selectedCategory = ref("all");
    const categories = ref([]);

    const displayCategories = [
      { name: "Electronics", image: "/categories/electronics.jpg" },
      { name: "Make-up", image: "/categories/makeup.jpg" },
      { name: "Clothes", image: "/categories/clothes.jpg" },
      { name: "Shoes", image: "/categories/shoes.jpg" },
      { name: "Accessories", image: "/categories/accessories.jpg" },
      { name: "Books", image: "/categories/books.jpg" },
      { name: "Home Appliances", image: "/categories/home-appliances.jpg" }
    ];

    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/products/");
        products.value = response.data.map(p => ({
          ...p,
          userQuantity: 1,
          added: false,
          saved: false
        }));
        categories.value = [...new Set(products.value.map(p => p.category))];
      } catch {
        error.value = "Failed to fetch products";
      } finally {
        loading.value = false;
      }
    };

    const changeQty = (product, delta) => {
      if (product.added) return;
      product.userQuantity = Math.max(1, Math.min(product.quantity, product.userQuantity + delta));
    };

    const addToCart = async (product) => {
      
      try {
        await axios.post("http://127.0.0.1:8000/api/cart/add/", {
          product_id: product.id,
          quantity: product.userQuantity || 1
        },
      {
        withCredentials: true
      });
        product.added = true;
        cartTotal.value += 1;
      } catch (err) {
        console.error("Failed to add to cart:", err);
      }
    };

    const addToWishlist = async (product) => {
      try {
        await axios.post("http://127.0.0.1:8000/api/wishlist/add/", {
          product_id: product.id
        });
        product.saved = true;
        wishlistTotal.value += 1;
      } catch (err) {
        console.error("Failed to add to wishlist:", err);
      }
    };

    const fetchCartItems = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/cart/");
        cartTotal.value = res.data.items?.length || 0;
      } catch (err) {
        console.error("Failed to fetch cart:", err);
      }
    };

    const fetchWishlistItems = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/wishlist/");
        wishlistTotal.value = res.data.items?.length || 0;
      } catch (err) {
        console.error("Failed to fetch wishlist:", err);
      }
    };

    const getProduct = (product) => {
      router.push(`/product/${encodeURIComponent(product.name)}/${encodeURIComponent(product.brand)}/`);
    };

    const filterCategory = (category) => {
      selectedCategory.value = category;
    };

    const filteredProducts = computed(() => {
      return products.value.filter(p => {
        const matchName = p.name.toLowerCase().includes(searchQuery.value.toLowerCase());
        const matchCategory = selectedCategory.value === "all" || p.category === selectedCategory.value;
        return matchName && matchCategory;
      });
    });

    onMounted(() => {
      fetchProducts();
      fetchCartItems();
      fetchWishlistItems();
    });

    return {
      searchQuery, loading, error, filteredProducts, displayCategories,
      wishlistTotal, cartTotal, selectedCategory, categories,
      filterCategory, getProduct, addToCart, addToWishlist, changeQty
    };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Jost:wght@300;400;500&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');

/* ── Palette ── */
:root {
  --cream:      #F5F0E8;
  --parchment:  #EDE4D3;
  --sand:       #D4C4A8;
  --caramel:    #B8996E;
  --mocha:      #8B6B45;
  --espresso:   #5C3D2E;
  --dark:       #2C1A0E;
  --warm-white: #FAF7F2;
  --blush:      #E8DDD0;
}

/* ── Base ── */
.dashboard {
  min-height: 100vh;
  background: var(--warm-white);
  padding-top: 70px;
  font-family: 'Jost', sans-serif;
}

/* ── Hero ── */
.hero-section {
  background: linear-gradient(135deg, #8B6B45 0%, #5C3D2E 100%);
  color: var(--parchment);
  padding: 80px 24px;
  text-align: center;
  margin-bottom: 48px;
}

.hero-content h1 {
  font-family: 'Playfair Display', serif;
  font-size: 3rem;
  font-weight: 600;
  margin-bottom: 16px;
  color: var(--warm-white);
}

.hero-content p {
  font-size: 1.2rem;
  opacity: 0.85;
  font-weight: 300;
}

/* ── Products Section ── */
.products-section {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px 60px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
  flex-wrap: wrap;
  gap: 16px;
}

.section-title {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  font-weight: 600;
  color: var(--dark);
}

/* Filter Chips */
.filter-chips {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.chip {
  padding: 7px 18px;
  border: 1.5px solid var(--sand);
  background: var(--cream);
  border-radius: 24px;
  cursor: pointer;
  transition: all 0.25s ease;
  font-size: 0.9rem;
  font-weight: 400;
  color: var(--mocha);
  font-family: 'Jost', sans-serif;
}

.chip:hover {
  border-color: var(--caramel);
  color: var(--espresso);
}

.chip.active {
  background: var(--espresso);
  color: var(--parchment);
  border-color: var(--espresso);
}

/* Loading / Error */
.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 0;
  gap: 16px;
  color: var(--mocha);
}

.spinner {
  width: 44px;
  height: 44px;
  border: 3px solid var(--sand);
  border-top-color: var(--espresso);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

.error {
  text-align: center;
  padding: 60px 20px;
  color: var(--espresso);
  font-size: 1.1rem;
}

/* ── Product Grid ── */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 28px;
}

/* ── Product Card ── */
.product-card {
  background: var(--cream);
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid var(--sand);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(92, 61, 46, 0.12);
}

/* Image Zone */
.image-zone {
  position: relative;
  width: 100%;
  height: 280px;
  overflow: hidden;
  background: var(--parchment);
  cursor: pointer;
}

.product-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.image-zone:hover .product-img {
  transform: scale(1.05);
}

.wishlist-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(250, 247, 242, 0.92);
  border: 1px solid var(--sand);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
}

.wishlist-btn:hover {
  border-color: var(--caramel);
  transform: scale(1.1);
}

.wishlist-btn svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: var(--mocha);
  stroke-width: 1.8;
  transition: all 0.25s ease;
}

.wishlist-btn.active svg {
  fill: var(--mocha);
  stroke: var(--mocha);
}

.category-tag {
  position: absolute;
  bottom: 12px;
  left: 12px;
  background: rgba(92, 61, 46, 0.82);
  color: var(--parchment);
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 5px 12px;
  border-radius: 20px;
  font-family: 'Jost', sans-serif;
}

/* Card Body */
.card-body {
  padding: 20px 20px 22px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.product-brand {
  font-size: 10px;
  font-weight: 400;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--mocha);
  opacity: 0.75;
  margin-bottom: 5px;
}

.product-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--dark);
  line-height: 1.35;
  cursor: pointer;
  transition: color 0.2s;
  margin-bottom: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.product-name:hover {
  color: var(--espresso);
}

.divider {
  height: 1px;
  background: var(--blush);
  margin: 14px 0;
}

.price-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 14px;
}

.price {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--espresso);
}

.stock-badge {
  font-size: 11px;
  font-weight: 400;
  color: var(--mocha);
  background: var(--parchment);
  border: 1px solid var(--sand);
  padding: 3px 10px;
  border-radius: 20px;
}

.stock-badge.low {
  color: #8B5E3C;
  background: #F5EBD9;
  border-color: #D4A574;
}

/* Qty Control */
.qty-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

.qty-label {
  font-size: 10px;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--mocha);
  opacity: 0.7;
  flex-shrink: 0;
}

.qty-control {
  display: flex;
  align-items: center;
  background: var(--parchment);
  border: 1px solid var(--sand);
  border-radius: 8px;
  overflow: hidden;
}

.qty-btn {
  width: 32px;
  height: 32px;
  background: none;
  border: none;
  cursor: pointer;
  color: var(--espresso);
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
  font-family: 'Jost', sans-serif;
}

.qty-btn:hover {
  background: var(--sand);
}

.qty-num {
  width: 36px;
  text-align: center;
  font-size: 14px;
  font-weight: 500;
  color: var(--dark);
  border-left: 1px solid var(--sand);
  border-right: 1px solid var(--sand);
  line-height: 32px;
}

/* Add to Cart Button */
.add-btn {
  width: 100%;
  padding: 12px;
  background: var(--espresso);
  color: var(--parchment);
  border: none;
  border-radius: 10px;
  font-family: 'Jost', sans-serif;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 1px;
  text-transform: uppercase;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  transition: all 0.3s ease;
  margin-top: auto;
}

.add-btn:hover:not(:disabled) {
  background: var(--dark);
  transform: translateY(-1px);
}

.add-btn:disabled {
  background: var(--caramel);
  cursor: not-allowed;
  opacity: 0.95;
  transform: none;
}

.add-btn svg {
  width: 15px;
  height: 15px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  flex-shrink: 0;
}

/* ── Categories Showcase ── */
.categories-showcase {
  max-width: 1400px;
  margin: 0 auto 80px;
  padding: 60px 24px;
}

.categories-title {
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
  font-weight: 600;
  color: var(--dark);
  text-align: center;
  margin-bottom: 48px;
}

.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px;
}

.category-showcase-card {
  background: var(--cream);
  border-radius: 20px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid var(--sand);
}

.category-showcase-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 36px rgba(92, 61, 46, 0.12);
}

.category-image-wrapper {
  width: 100%;
  height: 280px;
  overflow: hidden;
  background: var(--parchment);
}

.category-showcase-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.category-showcase-card:hover .category-showcase-img {
  transform: scale(1.06);
}

.category-showcase-name {
  padding: 18px 20px;
  font-family: 'Playfair Display', serif;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--dark);
  text-align: center;
  background: var(--cream);
}

/* ── Features ── */
.features-section {
  max-width: 1200px;
  margin: 40px auto 80px;
  padding: 0 24px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 24px;
}

.feature {
  text-align: center;
  padding: 32px 24px;
  background: var(--cream);
  border-radius: 16px;
  border: 1px solid var(--sand);
  transition: all 0.3s ease;
}

.feature:hover {
  background: var(--parchment);
  box-shadow: 0 6px 20px rgba(92, 61, 46, 0.08);
}

.feature-icon {
  font-size: 2rem;
  margin-bottom: 14px;
}

.feature h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  font-weight: 600;
  color: var(--dark);
  margin-bottom: 6px;
}

.feature p {
  color: var(--mocha);
  font-size: 0.875rem;
  font-weight: 300;
}

/* ── Footer ── */
.footer {
  background: var(--espresso);
  color: var(--parchment);
  padding: 72px 24px 32px;
  margin-top: 40px;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto 48px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 48px;
}

.footer-logo {
  font-family: 'Playfair Display', serif;
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--warm-white);
  margin-bottom: 14px;
  letter-spacing: 1px;
}

.footer-section p {
  color: var(--sand);
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 0.9rem;
  font-weight: 300;
}

.social-links {
  display: flex;
  gap: 10px;
}

.social-icon {
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(212,196,168,0.25);
  border-radius: 50%;
  text-decoration: none;
  color: var(--sand);
  font-size: 1rem;
  transition: all 0.3s ease;
}

.social-icon:hover {
  background: var(--caramel);
  color: var(--warm-white);
  border-color: var(--caramel);
  transform: translateY(-2px);
}

.footer-section h4 {
  font-family: 'Playfair Display', serif;
  margin-bottom: 18px;
  font-size: 1rem;
  font-weight: 600;
  color: var(--warm-white);
}

.footer-section ul { list-style: none; }

.footer-section ul li { margin-bottom: 10px; }

.footer-section ul li a {
  color: var(--sand);
  text-decoration: none;
  transition: color 0.2s;
  font-size: 0.9rem;
  font-weight: 300;
}

.footer-section ul li a:hover { color: var(--warm-white); }

.footer-bottom {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
  padding-top: 28px;
  border-top: 1px solid rgba(212, 196, 168, 0.2);
  color: var(--caramel);
  font-size: 0.875rem;
  font-weight: 300;
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .hero-content h1 { font-size: 2rem; }
  .hero-content p { font-size: 1rem; }
  .section-title { font-size: 1.5rem; }
  .product-grid { grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 18px; }
  .section-header { flex-direction: column; align-items: flex-start; }
  .categories-title { font-size: 1.75rem; }
}
</style>