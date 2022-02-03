const express = require('express');
const morgan = require("morgan");
const { createProxyMiddleware,responseInterceptor } = require('http-proxy-middleware');
const axios = require('axios');
const qs = require('qs');

// Create Express Server
const app = express();

// Configuration
const PORT = 3000;
const HOST = "localhost";
const API_SERVICE_URL = "https://jsonplaceholder.typicode.com";
//"https://api-dev.cat.com/iotgateway/messageParser/v1/parseMessage/json_placeholder"
const dealerLocatorURL = "22";
const ClientID = "nn";
const Secret = "xx";

app.use(morgan('dev'));
const config = {method: 'post', 
                url:'11', 
                headers:{'Content-Type':'application/x-www-form-urlencoded',
                            'Authorization':'Basic '+Buffer.from(ClientID+":"+Secret).toString('base64')},
                data:qs.stringify({'grant_type':'client_credentials'})};

const httpRequestToDecideSomething = function(path){
                console.log("-------");
                axios(config).then((response) => {
                        console.log(response.data.access_token);
                        const DLCconfig = {method: 'get', 
                        url:dealerLocatorURL, 
                        headers:{'Content-Type':'application/json',
                                    'Authorization':'Bearer '+response.data.access_token}
                        };
                        axios(DLCconfig).then((dlrResp) => {
                            console.log("HAHAHA");
                            console.log(dlrResp.data);
                            console.log("HAHAHA");
                        });
            });
            console.log("-------");
            return path;
        };
// Info GET endpoint
app.get('/info', (req, res, next) => {
    res.send('This is a proxy service which proxies to Billing and Account APIs.');
 });

 const myProxyMiddleware =createProxyMiddleware({
    target: API_SERVICE_URL,
    changeOrigin: true,
    logLevel: 'debug',
    pathRewrite: async function (path, req) {
        console.log(req.baseUrl)
        const should_add_something = await httpRequestToDecideSomething(path);
        if (should_add_something) path = should_add_something;
        return path.replace('/json_placeholder', '/');
      }
 });
 // Proxy endpoints
app.use('/json_placeholder', myProxyMiddleware);

 // Start the Proxy
app.listen(PORT, HOST, () => {
    console.log(`Starting Proxy at ${HOST}:${PORT}`);
 });
