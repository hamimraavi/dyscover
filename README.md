# dyscover

This API provides the list of restaurants in the given location. The location is provided via a query parameter in the URL. The result is returned as a JSON response.  

# API Documentation

## Getting list of restaurants

Fetch nearby restaurants

` GET search/?q=connaught%20place `

### Output

```
{
  Restaurants: [
    {
      Url: "https://www.zomato.com/ncr/archi-connaught-place-new-delhi?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
      Name: "Archi"
    },
    {
      Url: "https://www.zomato.com/food-cloud?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
      Name: "Food Cloud"
    },
    {
      Url: "https://www.zomato.com/mygreens?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
      Name: "MyGreens"
    },
    {
      Url: "https://www.zomato.com/tlc-kitchen?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
      Name: "TLC Kitchen"
    },
    {
      Url: "https://www.zomato.com/ncr/tpot-cafe-1-connaught-place-new-delhi?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
      Name: "Tpot Cafe"
    }
  ]
}
```

**Request method:** GET

**URL Parameters:** 
- (Required):   
 q=[string]  
 example: q=connaught place

**Success Response:** 
- 200 : Ok

**Error Response:**
- 400 : Bad Request
- 404 : Not found
- 503 : Service unavailable
