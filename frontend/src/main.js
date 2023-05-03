import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from 'vue'
import axios from 'axios';

import App from './App.vue'
import router from './router'

// createApp(App).use(router).mount('#app')

const app = createApp(App);

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://localhost:5000';

app.use(router);
app.mount("#app");
