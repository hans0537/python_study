<template>
  <div id="order-board">
    <div class="d-flex selected cart-btn justify-content-center align-items-center"
    @click="addOrder">
      <div>장바구니 담기</div>
    </div>
    <div>
      <h1 style="margin-botton: 20px">주문 내역</h1>
      <h4>총 {{ totalOrderCount }}건: {{ totalOrderPrice }}원</h4>
      <hr>
      
      <OrderListItem v-for="(order, idx) in orderList" :key="idx" :order="order"/>
      <hr>
    </div>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList: function () {
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },
  methods: {
    addOrder() {
      return this.$store.dispatch('addOrder')
    }
  }
}
</script>

<style>
#order-board {
  margin-top: 30px;
  padding: 10px;
  background-color: lightgray;
}

.cart-btn {
  width: 90%;
  margin: 10px auto;
  height: 50px;
  border-radius: 10px;
}

.cart-btn:hover {
  cursor: pointer;
}
</style>