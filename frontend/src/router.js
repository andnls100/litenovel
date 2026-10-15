import {createRouter,createWebHistory}
from "vue-router"


import Home from "./views/Home.vue"
import Book from "./views/Book.vue"
import Reader from "./views/Reader.vue"

import Chapter from "./views/Chapter.vue"

const router=createRouter({

    history:createWebHistory(),

    routes:[

        {
            path:"/",
            component:Home
        },

        {
			path: '/chapter/:book',
			name: 'Chapter',
			component: Chapter
		},

		{
            path:"/book/:id",
            component:Book
        },
        {
            path:"/read/:book/:chapter/:page",
            component:Reader
        }

    ]

})


export default router