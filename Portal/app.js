const express = require('express')
const compression = require('compression')
const routes = require('./routes')

const app = express()

app.use(compression())
app.use(routes)

const port = process.env.NODE_PORT || 3000

app.listen(port, () => {
  console.log(`[worker] Application is running on port ${port}...`)
})