<template>
    <div id="consultProduct">
        <div class="title">
            <h2>Consultar Producto</h2>
        </div>

        <div class="buttons">
        <button v-on:click="procesarInicio">Inicio</button>
        </div>

        <div class="forms">
            <br>
            <h2>Codigo de barras</h2>
            <input v-model="code" type="text" placeholder="">
        </div>

        <div class="result">
            <br>
            <p v-if="hay_datos" >Producto: {{product.name}}</p>
            <p v-if="hay_datos" >Producto: {{product.price}}</p>
            <p v-if="hay_datos" >Producto: {{product.stock}}</p>
        </div>

        <div class="consulta">
            <button v-on:click="procesarConsulta">Consultar</button>
        </div>

    </div>
    
    

</template>

<script>
import axios from 'axios';
    export default {
        name: "consultProduct",
        data: function(){
            return{
                code:"",
                hay_datos: false,
                product: {
                    name: "",
                    price: "",
                    stock: ""

                }
            }
        },
        methods: {
            procesarInicio: function(){
                this.$router.push({name: "inicio"})
            },
            procesarConsulta: function(){
                let self = this
                axios.get("http://127.0.0.1:8000/product/"+self.code)
                    .then((result)=>{
                        self.product.name = result.data.name
                        self.product.price = result.data.price
                        self.product.stock = result.data.stock
                        self.hay_datos = true 
                    })
                    .catch((error)=>{
                        self.hay_datos = false
                        alert("ERROR: " + error.response.status)
                    })

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
.consulta{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
    }
.title{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
  }
  .result{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: medium;
  }
.forms{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: small;
  }
</style>