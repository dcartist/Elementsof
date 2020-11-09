## What is Elements Of?

Language, by definition, is the method of human communication, either spoken or written, consisting of words in a structured and conventional way. There is beauty in the fact that humans have more than 600 forms of communicating with machines.  This Flask API captures some of those programming languages and gives you information on them based on Wikipedia data via python. 

`*The dataset is still being working on and adjusted.`



### Technologies used:

- **Flask API** *(Python)*

- **Wikipedia** *(Python Library)*

- **WPtools** *(Python Library)*

- **Vercel** *(deployment)*

  

## Website:

 https://elementsof.vercel.app/api/

------

#### Routes

##### Get All Languages:

`GET https://elementsof.vercel.app/api/`

##### Get Language by ID:

`GET https://elementsof.vercel.app/api/id/<id>`

##### Get Language by Name:

`GET https://elementsof.vercel.app/api/name/name`



#### Response

```javascript
{
	"id": Number,
	"infobox": { 
		"age": String,
		"developer": String,
		"implementations": String,
		"influenced_by": String,
		"logo": String,
		"name": String,
		"paradigm": [Array],
		"typing": [Array],
		"year": String
			},
	"name": String,
	"summary": String,
	"summary_html": String
}
```

