<template>
  <div class="hello" style="float: left">
    <h1>BookInfo</h1>
    <div style="width: 80%;float: left;height: 80px;text-align: left;padding: 60px;">
      <a>Profile</a><br>
      <div style="width: 120px;float: left;height: 80px;text-align: left;">
        name: <br>
        category: <br>
        release_date: <br>
        author: <br>
        type: <br>
      </div>
      <div style="width: 100px;float: left;height: 80px;text-align: left;">
        {{ info.name }}<br>
        {{ info.category }}<br>
        {{ info.date }}<br>
        {{ info.author }}<br>
        {{ info.type }}<br>
      </div>
    </div>
    <div style="width: 30%;float: left;height: 500px;text-align: left;padding: 60px;">
      <a>Rating</a><br>
      <div style="text-align: left" v-for = "(item,index) in info.rating" :key="index">
        <div style="width: 40%;float: left;height: 16px;text-align: left;">
          {{ index }}<br>
        </div>
        <div style="width: 60%;float: left;height: 16px;text-align: left;">
          {{ item }}<br>
        </div>
      </div>
    </div>
    <div style="width: 30%;float: left;height: 500px;text-align: left;padding: 60px;">
      <a>Comments</a><br>
      <div style="text-align: left" v-for = "(item,index) in info.comments" :key="index">
        <div style="width: 40%;float: left;height: 16px;text-align: left;">
          {{ index }}<br>
        </div>
        <div style="width: 60%;float: left;height: 16px;text-align: left;">
          {{ item }}<br>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require('axios')
export default {
  name: 'BookInfo',
  data () {
    return {
      info: {}
    }
  },
  mounted () {
    axios
      .get('/details/0')
      .then(response => {
        this.info = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.a1 {
  margin: 5px auto;
}
.blueColor{
  font-size: 1.3em;
  color: blue;
  padding-left: .3em;
}
.a1 li{
  border: 1px solid #444444;
  margin: 5px;
  padding: 10px;
}

div-a {
  width: 40%;
  float: left;
  height: 500px;
  text-align: left;
  padding: 60px;
}
</style>
