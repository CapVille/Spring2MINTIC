<template>
  <div id="app">
    <div class="header">
      <h2>INVENTARIO</h2>
    </div>


    <div class="main">
      <router-view v-on:select-product="procesarConsulta" v-on:select-venta="procesarVenta"></router-view>
    </div>

    <div class="footer">
      <h2>G2M3-6</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {},

  data: function(){
    return{
      inicio: true,
      title: "Inicio",
      product: false,
      consulta: true,
      venta: true
    }
  },

  methods: {
  },
  created: function(){
    this.$router.push({name: "inicio"})
  }
}
</script>

<style>
  .header{
    background-color: #dcdcdc;
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: x-large;
  }
  
  
  .footer{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
  }
</style>
