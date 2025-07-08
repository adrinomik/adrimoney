<template>
    <div style="max-width: 1200px; margin: 0 auto;">
        <h1>Playground</h1>
        <p>Счетчик: {{ count }}</p>

        <button @click="increment" :disabled="count >= 10">Увеличить</button>
        <button @click="decrement" :disabled="count <= -5">Уменьшить</button>
        <button @click="reset">Сбросить</button>


        <hr />

        <h2>Мини корзина</h2>
        <button @click="addToCart">Добавить в корзину</button>
        <div>В корзине: {{ cart.count }} товаров</div>
        <ul>
            <li v-for="(item, idx) in cart.items" :key="idx">
                {{ item }}
                <button @click="cart.removeItem(idx)">Удалить</button>
            </li>
        </ul>



        <div>
            <div v-for="(elem, index) in names">
                <p>{{ elem }}</p>
                <button>Посмотреть {{ elem }} ({{ index }})</button>

            </div>
        </div>

        <hr />

        <input v-model="myName" placeholder="Введите My Name">
        <button @click="getMyName">ADD</button>
        <button @click="removeThirdName">Remove Third Name</button>

        <ul>
            <li v-for="(name, idx) in myNames">
                {{ name }}
            </li>
        </ul>

    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCartStore } from '@/stores/cart'

const count = ref(0);

const myName = ref('');

const myNames = ref([]);

onMounted(() => {
    const savedMyNames = localStorage.getItem('myNames');
    if (savedMyNames) {
        myNames.value = JSON.parse(savedMyNames);
    } else {
        myNames.value = ['Еблан', 'Гандон', 'Pidr'];
    }
})


const names = ref(['Антон', 'Мария', 'Иван', 'Елена', 'Дмитрий'])

function reset() {
    count.value = -2
}

function increment() {
    if (count.value < 10) {
        count.value++
    }
}

function decrement() {
    if (count.value > -5) {
        count.value--
    }
}

const cart = useCartStore()

function addToCart() {
    cart.addItem('Товар 1')
}

function getMyName() {
    if (myName.value.trim()) {
        myNames.value.push(myName.value.trim());
        myName.value = '';
        console.log(myNames);

        localStorage.setItem('myNames', JSON.stringify(myNames.value));
    }

}


function removeThirdName() {
    if (myNames.value.length > 2) {
        myNames.value.splice(2, 1);
        localStorage.setItem('myNames', JSON.stringify(myNames.value));
    }
}

</script>
