#dyscover

This api provides the list of restaurants in the given location.  
The location is provided via a query parameter in the url.  
The result is returned as a Json response.  
The sample url is:

/api/search/?q=connaught%20place

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
