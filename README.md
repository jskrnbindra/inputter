# inputter
Answer to my code design interview question when I was a fresher.

## Question
We need to accept input from the user (say through command line) and output the following JSON.

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
| AttributeType  | int, long, double, string           |
| AttributeIndex | NONE, NORMAL                        |
| Notification   | NOTIFICATION_ALL, NOTIFICATION_NONE |
| SampleGran     | SECOND, MINUTE, HOUR                |


## Usage
`python3 main.py`