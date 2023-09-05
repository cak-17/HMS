import axios from 'axios'

export default axios.create({
    baseUrl: "http://0.0.0.0:8000/api/"
})