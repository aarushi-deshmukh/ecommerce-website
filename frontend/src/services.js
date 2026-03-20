import api from "@/api";

export const fetchCart = async () => {
  try {
    const res = await api.get("cart/");
    return res.data.items || [];
  } catch (err) {
    console.error("Fetch cart error:", err.response?.data || err);
    throw err;
  }
};

export const removeCartItem = async (productId) => {
  try {
    await api.delete(`cart/remove/${productId}/`);
    return true;
  } catch (err) {
    console.error("Remove cart error:", err.response?.data || err);
    throw err;
  }
};

export const addToCart = async (productId, quantity = 1) => {
  try {
    const res = await api.post("cart/add/", {
      product_id: productId,
      quantity
    });
    return res.data;
  } catch (err) {
    console.error("Add to cart error:", err.response?.data || err);
    throw err;
  }
};

export const checkoutCart = async (items) => {
  try {
    const res = await api.post("place-order/", { items });
    return res.data;
  } catch (err) {
    console.error("Checkout error:", err.response?.data || err);
    throw err;
  }
};

export const fetchWishlist = async () => {
  try {
    const res = await api.get("wishlist/");
    return res.data.items || [];
  } catch (err) {
    console.error("Fetch wishlist error:", err.response?.data || err);
    throw err;
  }
};

export const addWishlistItem = async (productId) => {
  try {
    const res = await api.post("wishlist/add/", {
      product_id: productId,
    });
    return res.data;
  } catch (err) {
    console.error("Add wishlist error:", err.response?.data || err);
    throw err;
  }
};

export const removeWishlistItem = async (productId) => {
  try {
    await api.delete(`wishlist/remove/${productId}/`);
    return true;
  } catch (err) {
    console.error("Remove wishlist error:", err.response?.data || err);
    throw err;
  }
};

export const fetchProducts = async () => {
  try {
    const res = await api.get("products/");
    return res.data;
  } catch (err) {
    console.error("Fetch products error:", err.response?.data || err);
    throw err;
  }
};