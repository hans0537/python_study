<template>
<section id="trend" class="pt-4 mt-5">
  <div class="container">
    <div class="row trend_1" style="display:flex; justify-content: space-between;">
      <div class="hr-line"></div>
      <div class="col-md-6 col-6">
        <h4 class="trend_1l" style="text-align:left;">UpComing <span class="col_red">Movies</span></h4>
      </div>
      <div class="col-md-6 col-6 text-end">
        <h6 class="mb-0">
          <router-link to="/movie/upcoming" class="btn btn-primary" style="text-decoration: none;">View All</router-link>
        </h6>
      </div>
    </div>

    <div class="row trend_2 mt-4">
      <div id="carouselExampleCaptions2" class="carousel slide" data-bs-ride="carousel" >
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleCaptions2" data-bs-slide-to="0" class="active bg-success" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions2" data-bs-slide-to="1" class="bg-success" aria-label="Slide 2" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions2" data-bs-slide-to="2" class="bg-success" aria-label="Slide 3" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions2" data-bs-slide-to="3" class="bg-success" aria-label="Slide 4" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions2" data-bs-slide-to="4" class="bg-success" aria-label="Slide 5" aria-current="true"></button>
        </div>
        
        <div class="carousel-inner"> 
          <div class="carousel-item" v-for="(movies, index) in upcomingList" :key="index" :class="index===0 ? 'active' : ''">
            <div class="trend_2i row">
              <UpComingListItem 
              v-for="movie in movies" :key="movie?.id" :movie="movie"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import UpComingListItem from '@/components/HomeMovieComponents/UpComingListItem'

export default {
  name: 'UpComingList',
  components: {
    UpComingListItem
  },
  computed: {
    upcomingList() {
      const tmp = this.$store.state.upcomingList
      let res = []
      let temp = []
      for (let i = 1; i <= 20; i++) {
        temp.push(tmp[i - 1])
        if(i % 4 == 0) {
          res.push(temp)
          temp = []
        }
      }
      return res
    }
  },
}
</script>

<style>

</style>