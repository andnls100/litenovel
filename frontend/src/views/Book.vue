<script setup>

import {ref,onMounted} from "vue"

import {useRoute,useRouter} from "vue-router"

import axios from "axios"


const route = useRoute()

const router = useRouter()


const chapters = ref([])

const bookName = ref("")



async function load(){

    let res = await axios.get(

        "http://127.0.0.1:8000/api/book/"
        +
        route.params.id
        +
        "/catalog"

    )


    chapters.value = res.data

}



function read(chapter){

    router.push(

        "/read/"
        +
        route.params.id
        +
        "/"
        +
        chapter.id
        +
        "/1"

    )

}



onMounted(load)


</script>



<template>

<div class="book">


<h1>
小说目录
</h1>


<div

v-for="c in chapters"

:key="c.id"

class="chapter"

@click="read(c)"

>

{{c.title}}

</div>


</div>


</template>



<style scoped>


.book{

width:800px;

margin:auto;

padding:30px;

}



.chapter{

padding:15px;

border-bottom:1px solid #ddd;

cursor:pointer;

}



.chapter:hover{

background:#f5f5f5;

}


</style>