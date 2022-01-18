var axios = require('axios');
var qs = require('qs');
var access_token1;
var data = qs.stringify({
  'grant_type': 'client_credentials',
  'access_token_manager_id': 'BasicIdentityATMClientCreds',
  'scope': 'manage:all' 
});
var config = {
  method: 'post',
  url: 'https://fedloginqa.cat.com/as/token.oauth2',
  headers: { 
    'Content-Type': 'application/x-www-form-urlencoded', 
    'Authorization': 'Basic '+Buffer.from("").toString('base64')
  },
  data : data
};

axios(config)
.then( function (response) {
  console.log(JSON.stringify(response.data));
  access_token1 = JSON.stringify(response.data)
  print_token(access_token1)
})
.catch(function (error) {
  console.log(error);
});

function print_token(access_token){
    console.log("*****")
    console.log(access_token1)
    console.log("*****")
};
