import { defineStore } from 'pinia'
import { ref, computed } from 'vue'


// cart - уникальное имя хранилища
export const useCartStore = defineStore('cart', () => {

    const items = ref<string[]>([])

    function addItem(item: string) {
        items.value.push(item)
    }

    function removeItem(index: number) {
        items.value.splice(index, 1)
    }

    const count = computed(() => items.value.length)

    return {
        items,
        addItem,
        removeItem,
        count
    }

});




