// import { createRouter, createWebHistory } from 'vue-router'
// import SignUp from '@/pages/Auth/SignUp.vue'
// import SignIn from '@/pages/Auth/SignIn.vue'
// import SProfile from '@/pages/Seller/SProfile.vue'
// import BProfile from '@/pages/Buyer/BuyerProfile.vue'
// import Cart from '@/pages/Buyer/Cart.vue'
// import Product from '@/pages/Product.vue'
// import BuyerDashboard from '@/pages/Buyer/BuyerDashboard.vue'
// import SellerDashboard from '@/pages/Seller/SellerDashboard.vue'
// import AddProducts from '@/pages/Seller/AddProducts.vue'
// import History from '@/pages/Buyer/History.vue' 
// import MyProducts from '@/pages/Seller/MyProducts.vue'
// import Wishlist from '@/pages/Buyer/Wishlist.vue'
// import HomeView from '@/pages/Dashboard.vue'

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'homeview',
//       component: HomeView,
//     },
//     {
//       path: '/signup',
//       name: 'signup',
//       component: SignUp,
//     },
//     {
//       path: '/signin',
//       name: 'signin',
//       component: SignIn,
//     },
//     {
//       path: '/buyer-profile',
//       name: 'buyer-profile',
//       component: BProfile,
//     },
//     {
//       path: '/seller-profile',
//       name: 'seller-profile',
//       component: SProfile,
//     },
//     {
//       path: '/cart',
//       name: 'cart',
//       component: Cart,
//     },
//     {
//       path: '/get-product/:name/:brand',
//       name: 'ProductDetail',
//       component: Product,
//     },
//     {
//       path: '/buyer-dashboard',
//       name: 'buyer-dashboard',
//       component: BuyerDashboard,
//     },
//     {
//       path: '/seller-dashboard',
//       name: 'seller-dashboard',
//       component: SellerDashboard,
//     },
//     {
//       path: '/add-products',
//       name: 'add-products',
//       component: AddProducts,
//     },
//     {
//       path: '/my-products',
//       name: 'my-products',
//       component: MyProducts,
//     },
//     {
//       path: '/history',
//       name: 'history',
//       component: History,
//     },
//     {
//       path: '/wishlist',
//       name: 'wishlist',
//       component: Wishlist,
//     },
//   ],
// })

// export default router

import { createRouter, createWebHistory } from "vue-router"

import MainLayout from "@/layouts/MainLayout.vue"
import AuthLayout from "@/layouts/AuthLayout.vue"

import Home from "@/pages/Dashboard.vue"
import SignIn from "@/pages/Auth/SignIn.vue"
import SignUp from "@/pages/Auth/SignUp.vue"
import BuyerDashboard from "@/pages/Buyer/BuyerDashboard.vue"
import SellerDashboard from '@/pages/Seller/SellerDashboard.vue'
import SProfile from '@/pages/Seller/SProfile.vue'
import BProfile from '@/pages/Buyer/BuyerProfile.vue'
import Cart from '@/pages/Buyer/Cart.vue'
import Product from '@/pages/Product.vue'
import MyProducts from '@/pages/Seller/MyProducts.vue'
import Wishlist from '@/pages/Buyer/Wishlist.vue'
import History from '@/pages/Buyer/History.vue' 

const routes = [

  {
    path: "/",
    component: MainLayout,
    children: [
      { path: "", component: Home },
      { path: "buyer-dashboard", component: BuyerDashboard },
      { path: 'buyer-profile', component: BProfile },
      { path: 'seller-profile', component: SProfile },
      { path: 'cart', component: Cart },
      { path: 'seller-dashboard', component: SellerDashboard },
      { path: '/history', component: History },
      { path: 'wishlist', component: Wishlist },
    ]
  },

  {
    path: "/",
    component: AuthLayout,
    children: [
      { path: "signin", component: SignIn },
      { path: "signup", component: SignUp }
    ]
  }

]

export default createRouter({
  history: createWebHistory(),
  routes
})