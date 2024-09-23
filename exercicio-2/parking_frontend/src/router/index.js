import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import VehicleView from '@/views/VehicleView.vue';
// import CustomerView from '@/views/CustomerView.vue';
// import PlanView from '@/views/PlanView.vue';
// import ContractView from '@/views/ContractView.vue';

const routes = [
    { path: '/', name: 'Home', component: HomeView },
    { path: '/vehicles', name: 'Vehicle', component: VehicleView },
    // { path: '/customers', name: 'Customer', component: CustomerView },
    // { path: '/plans', name: 'Plan', component: PlanView },
    // { path: '/contracts', name: 'Contract', component: ContractView },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;