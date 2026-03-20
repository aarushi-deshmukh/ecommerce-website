import { createRouter, createWebHistory } from "vue-router"

import MainLayout from "@/layouts/MainLayout.vue"
import AuthLayout from "@/layouts/AuthLayout.vue"

import SignIn from "@/pages/Auth/SignIn.vue"
import SignUp from "@/pages/Auth/SignUp.vue"

import Home from "@/pages/Dashboard.vue"
import Shopping from "@/pages/Shopping.vue"
import Profile from '@/pages/Profile.vue'
import ProductDetails from '@/pages/ProductDetails.vue'

import Cart from '@/pages/Buyer/Cart.vue'
import Wishlist from '@/pages/Buyer/Wishlist.vue'
import History from '@/pages/Buyer/History.vue' 

import MyProducts from '@/pages/Seller/MyProducts.vue'
import AddProducts from '@/pages/Seller/AddProducts.vue'
import Analysis from '@/pages/Seller/Analysis.vue'

const routes = [

  {
    path: "/",
    component: MainLayout,
    children: [
      // Shared urls
      { path: '', component: Home },
      { path: 'shopping', component: Shopping },
      { path: 'details/:id', component: ProductDetails },
      { path: 'profile', component: Profile },

      // Buyer
      { path: 'cart', component: Cart },
      { path: 'history', component: History },
      { path: 'wishlist', component: Wishlist },

      // Seller
      { path: 'add-product', component: AddProducts },
      { path: 'my-products', component: MyProducts },
      { path: 'analysis', component: Analysis },
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