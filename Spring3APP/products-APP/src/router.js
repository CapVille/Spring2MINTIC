import vueRouter from 'vue-router'

import App from './App'

import consultProduct from './components/consultProduct'
import inicio from './components/inicio'
import venta from './components/venta'

const router = new vueRouter({
        mode: 'history',
        base: __dirname,
        routes:[
            {
                path: '/',
                name: 'root',
                component: App
            },
            {
                path: '/inicio',
                name: 'inicio',
                component: inicio
            },
            {
                path: '/consultProduct',
                name: 'consultProduct',
                component: consultProduct
            },
            {
                path: '/venta',
                name: 'venta',
                component: venta
            },
        ]
    }
)

export default router