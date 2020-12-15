<template>
    <div id="venta">
        <div class="title">
            <h2>Venta</h2>
        </div>

        <div class="buttons">
        <button v-on:click="procesarInicio">Inicio</button>
        </div>

        <div class="forms">
            <br>
            <h2>Codigo de barras</h2>
            <input v-model="name" type="text" placeholder="">
            <h2>Cantidad</h2>
            <input v-model="name" type="text" placeholder="">
        </div>
    </div>
    
    

</template>

<script>
    export default {
        name: "venta",
        data: function(){
            return{
                inicio: true,
                product: false,
                consulta: true,
                venta: true
            }
        },
        methods: {
            procesarInicio: function(){
                this.$router.push({name: "inicio"})
            }
        }
    }
</script>

<style>
.buttons{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
  }
.title{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
  }
.forms{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: small;
  }
</style>