<template>
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
</template>

<style scoped>
/* ── Footer ── */
.footer {
  background: white;
  color: var(--parchment);
  padding: 72px 0px 32px;
  margin-top: 40px;
  border-top: 1px solid #e5e5e5;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto 40px;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 20px;
}

.footer-logo {
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
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(212, 196, 168, 0.25);
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
  margin-bottom: 18px;
  font-size: 1.3rem;
  color: var(--warm-white);
}

.footer-section ul {
  list-style: none;
}

.footer-section ul li {
  margin-bottom: 18px;
}

.footer-section ul li a {
  color: #aaa;
  text-decoration: none;
  transition: color 0.2s;
  font-size: 1rem;
}

.footer-section ul li a:hover {
  color: var(--warm-white);
}

.footer-bottom {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
  padding-top: 28px;
  border-top: 1px solid #e5e5e5;
  color: #999;
  font-size: 0.9rem;
  font-weight: 300;
}
</style>