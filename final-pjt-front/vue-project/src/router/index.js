import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import LogOutView from '@/views/LogOutView.vue'

// profileview
import Profile from '@/components/Profile.vue'
import MyPageView from '@/views/MyPageView.vue'
import SearchPageView from '@/views/SearchPageView.vue'

// likesview
import DepositsLikeDetailView from '@/views/DepositsLikeDetailView.vue'
import SavingLikeDetailView from '@/views/SavingLikeDetailView.vue'

//recommendview
import RecommendView from '@/views/RecommendView.vue'
import StockRecommendView from '@/views/StockRecommendView.vue'
import StockPlusRecommendView from '@/views/StockPlusRecommendView.vue'
import FundRecommendView from '@/views/FundRecommendView.vue'
import SaveRecommendView from '@/views/SaveRecommendView.vue'
import DepositsRecommendView from '@/views/DepositsRecommendView.vue'
import FinLifeView from '@/views/FinLifeView.vue'

// deposits-save view
import SaveProductView from '@/views/SaveProductView.vue'
import DepositsProductView from '@/views/DepositsProductView.vue'
import DepositsProductDetailView from '@/views/DepositsProductDetailView.vue'
import SaveProductDetailView from '@/views/SaveProductDetailView.vue'

// gameview
import GameView from '@/views/GameView.vue'
import CheckResultView from '@/views/CheckResultView.vue'
import Lv1 from '@/components/LevelPage.vue/Lv1.vue'
import Lv2 from '@/components/LevelPage.vue/Lv2.vue'
import Lv3 from '@/components/LevelPage.vue/Lv3.vue'
import Lv4 from '@/components/LevelPage.vue/Lv4.vue'
import Lv5 from '@/components/LevelPage.vue/Lv5.vue'

// exchangerateview
import ExchangeRateView from '@/views/ExchangeRateView.vue'

// mapview
import MapView from '@/views/MapView.vue'

// articleview 
import ArticleView from '@/views/Article/ArticleView.vue'
import ProfitDataView from '@/views/Article/ProfitDataView.vue'
import AssetDataView from '@/views/Article/AssetDataView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signupview',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'loginview',
      component: LogInView
    },
    {
      path: '/logout',
      name: 'logoutview',
      component: LogOutView
    },
    {
      path: '/finlife',
      name: 'finlifeview',
      component: FinLifeView,
      children: [
        {
          path: '/finlife/save-product',
          name: 'saveproductview',
          component: SaveProductView
        },
        {
          path: '/finlife/deposits-product',
          name: 'depositsproductview',
          component: DepositsProductView
        },
      ]
    },
    {
      path: '/recommend',
      name: 'recommendview',
      component: RecommendView,
      children: [
        {
          path: '/recommend/stock-recommend',
          name: 'stockrecommendview',
          component: StockRecommendView
        },
        {
          path: '/recommend/stock-plus-recommend',
          name: 'stockplusrecommendview',
          component: StockPlusRecommendView
        },
        {
          path: '/recommend/fund-recommend',
          name: 'fundrecommendview',
          component: FundRecommendView
        },
        {
          path: '/recommend/save-recommend',
          name: 'saverecommendview',
          component: SaveRecommendView
        },
        {
          path: '/recommend/deposits-recommend',
          name: 'depositsrecommendview',
          component: DepositsRecommendView
        },
      ]
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/mypage',
      name: 'mypageview',
      component: MyPageView
    },
    {
      path: '/searchpage',
      name: 'searchpageview',
      component: SearchPageView
    },
    {
      path: '/game',
      name: 'gameview',
      component: GameView
    },
    {
      path: '/checkresult/:username',
      name: 'checkresultview',
      component: CheckResultView
    },
    {
      path: '/checkresult/lv1',
      name: 'lv1',
      component: Lv1
    },
    {
      path: '/checkresult/lv2',
      name: 'lv2',
      component: Lv2
    },
    {
      path: '/checkresult/lv3',
      name: 'lv3',
      component: Lv3
    },
    {
      path: '/checkresult/lv4',
      name: 'lv4',
      component: Lv4
    },
    {
      path: '/checkresult/lv5',
      name: 'lv5',
      component: Lv5
    },
    {
      path: '/exchange_rate',
      name: 'exchangerateview',
      component: ExchangeRateView

    },
    {
      path: '/map',
      name: 'mapview',
      component: MapView

    },
    {
      path: '/finlife/deposits-product/:id', 
      name: 'depositsdetailview',
      component: DepositsProductDetailView
    },
    {
      path: '/finlife/save-product/:id', 
      name: 'savedetailview',
      component: SaveProductDetailView
    },
    {
      path:'/article',
      name: 'articleview',
      component: ArticleView,
      children:[
        {
          path:'/article/ranking/profit',
          name:'profitdataview',
          component: ProfitDataView
        },
        {
          path:'/article/ranking/asset',
          name:'assetdataview',
          component: AssetDataView
        },
      ]
    },
    {
      path: '/mypage/saving-product/:id', 
      name: 'mysavingdetailview',
      component: SavingLikeDetailView
    },
    {
      path: '/mypage/deposits-product/:id', 
      name: 'mydepositsdetailView',
      component: DepositsLikeDetailView
    },
  ]
})

export default router
