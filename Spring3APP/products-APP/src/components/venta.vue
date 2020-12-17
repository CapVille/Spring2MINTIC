<template>
    <div id="venta">
        
        <div class="title">
            <h2>Venta</h2>
        </div>

        <div class="buttons">
        <button v-on:click="procesarInicio">Inicio</button>
        </div>

        <div class="forms">
            
            <form v-on:submit.prevent="procesarVenta" >
                <h2>Codigo de barras</h2>
                <input v-model="product.bar_code" type="text" placeholder="">
                <h2>Cantidad</h2>
                <input v-model="product.stock" type="text" placeholder="">
                <br>
                <button type="submit">Vender</button>
            </form>
        </div>


    </div>
    
    

</template>

<script>
import axios from 'axios';
    export default {
        name: "venta",
        data: function(){
            return{
                product: {
                    bar_code: "",
                    stock: ""

                }
            }
        },
        methods: {
            procesarInicio: function(){
                this.$router.push({name: "inicio"})
            },
            procesarVenta: function(){
                let self = this
                
                /*axios.get("http://127.0.0.1:8000/product/"+self.product.bar_code)
                    .then((result)=>{
                        alert(result.data.stock)
                    })
                    .catch((error)=>{
                        self.hay_datos = false
                        alert("ERROR: " + error.response.status)
                    })
*/
                axios.put("http://127.0.0.1:8000/product/", self.product, {headers: {}})
                    .then((result)=>{
                        alert("Se actualizo correctamente") 
                    })
                    .catch((error)=>{
                        self.hay_datos = false
                        alert("ERROR: " + error.response.data.detail)
                    })
                

            },
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

  .venta{
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: small;
  }
</style>