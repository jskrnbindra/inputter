# inputter
Answer to a simple code design interview question I faced when I was a fresher.
Saving it here because I like how I did it back then.

## Question
We need to generate the following JSON by accepting input from the user for field values.

```javascript
{
   "displayName":"someName",
   "query":"STATIC",
   "attributes":[
      {
         "code":"someCode",
         "name":"Some name",
         "attrType":"double",
         "Index":"NONE",
         "key-size":0
      },
      {
         "code":"SomeCode",
         "name":"SOmeNAme",
         "attrType":"string",
         "Index":"NORMAL",
         "key-size":64
      }
   ],
   "notification":"NOTIFICATION_NONE",
   "desc":"Some descriptin here",
   "archive-ttlsec":"5000",
   "sample-gran":"SECOND",
   "id":164411900999514687498612240976476000374,
   "stream-name":"Jezzy_164411900999514687498612240976476000374",
   "appId":"4f0e4695-6d02-40fa-a968-449c135a9e69"
}
```
**Judgement criteria**: Make it as flexible as possible but don't overdo it.
<br></br>
#### Validations

| field          | Accepted values                     |
|----------------|-------------------------------------|
| query          | GROUPBY, STATIC, RAW, TOPK          |
| attrType       | int, long, double, string           |
| Index          | NONE, NORMAL                        |
| Notification   | NOTIFICATION_ALL, NOTIFICATION_NONE |
| SampleGran     | SECOND, MINUTE, HOUR                |
| key-size       | 64 if attrType is 'string'          |
| id             | a random id                         |
| stream-name    | displayName + '_' + id              |
| appId          | a random uuid                       |

`attributes` can be of any number.

## Usage
`python3 main.py`
