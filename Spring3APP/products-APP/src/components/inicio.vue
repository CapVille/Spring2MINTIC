<template>
    <div id="inicio">
        <div class="title">
            <h2>Inicio</h2>
        </div>

        <div class="buttons">
            <button v-if="consulta" v-on:click="procesarConsulta">Consultar Producto</button>
            <button v-if="venta" v-on:click="procesarVenta">Venta</button>
            <button v-if="!inicio" v-on:click="procesarInicio">Inicio</button>
            <br>
        </div>
    </div>

    

</template>

<script>
    export default {
        name: "inicio",
        data: function(){
            return{
                inicio: true,
                product: false,
                consulta: true,
                venta: true
            }
        },
        methods: {
            procesarConsulta: function(){
                this.$router.push({name: "consultProduct"})
            },
            procesarVenta: function(){
                this.$router.push({name: "venta"})
            }
        },
    }
</script>

<style>
.title{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
}
.buttons{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
}
</style>