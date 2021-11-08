<template>
  <h1>test</h1>
  <input type="file" id="target">
  <button @click="doit">do</button>
  <p>{{ result.number }}</p>
  <textarea :value='result.text' rows="10" cols="100" id="text"/>
  <br>
  <textarea id="code"/>
  <br>
  <button @click="commit">commit</button>
</template>

<script>
import XLSX from 'xlsx'
import {reactive} from 'vue'
import axios from 'axios'

export default {
  name: 'HelloWorld',
  setup() {
    let wb;

    let result = reactive({
      number: '',
      text: '',
      code: '',
    })
    const commit = () => {
      //console.log(document.getElementById('text'))
      result.text = document.getElementById('text').value
      result.code = document.getElementById('code').value
      send()
    }
    const doit = () => {
      let x = document.getElementById('target').files[0]
      let reader = new FileReader()
      reader.onload = (e) => {
        let data = e.target.result
        wb = XLSX.read(data, {type: "binary"})
        let test = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
        console.log(typeof (test))
        for (let i = 0; i < test.length; i++) {
          result.number = result.number + test[i]['tele'] + ','
        }
        //console.log(result)
      }
      reader.readAsBinaryString(x)
    }
    const send = () => {
      let params = new URLSearchParams()
      params.append('number', result.number)
      params.append('text', result.text)
      params.append('code', result.code)
      axios.post('http://127.0.0.1:8000/portfolio_comfirm/diy_send/', params).then((res) => {
        console.log(res.data)
      })
    }
    return {doit, result, commit, send}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
