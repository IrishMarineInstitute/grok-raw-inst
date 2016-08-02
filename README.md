# grok-raw-inst
Parsing raw text from instrument outputs using [grok](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html) patterns

The developed Grok patterns can be found in the [/patterns](https://github.com/IrishMarineInstitute/grok-raw-inst/tree/master/patterns) directory of this repository

A simple example of using the patterns in Python is included in the [root](https://github.com/IrishMarineInstitute/grok-raw-inst) directory

## Example output
```javascript
{
  "wavelength_turbidity": "700", 
  "timestamp": "2016-08-02T08:42:56.179Z", 
  "instrument": "WL-ECO-FLNTU-3137", 
  "wavelength_fluorescence": "695", 
  "chlorophyll_counts": "66", 
  "thermistor": "540", 
  "turbidity_counts": "134"
}
```

The output from the Grok match can be piped to [jq](https://stedolan.github.io/jq/) (a command line JSON processor) in order to generate standardised output e.g.

```bash
jq . | {id:"foo","phenomenonTime":{"Instant": .timestamp},"member":[{"type":"measurement","id": "CHLCount", "observedProperty": {"href": "http://vocab.nerc.ac.uk/collection/P01/current/FCNTRW01/"}, "procedure": {"href": "http://vocab.nerc.ac.uk/collection/L22/current/TOOL0215/"}, "result": {"uom": "http://vocab.nerc.ac.uk/collection/P06/current/UUUU/","value": .chlorophyll_counts|tonumber}, "resultTime": .timestamp},{"type":"measurement","id": "TurbCount", "observedProperty": {"href": "http://vocab.nerc.ac.uk/collection/P01/current/NVLTOBS1/"}, "procedure": {"href": "http://vocab.nerc.ac.uk/collection/L22/current/TOOL0215/"}, "result": {"uom": "http://vocab.nerc.ac.uk/collection/P06/current/UUUU/","value": .turbidity_counts|tonumber}, "resultTime": .timestamp}]}
```

yields

```javascript
{
  "id": "foo",
  "phenomenonTime": {
    "Instant": "2016-08-02T08:42:56.179Z"
  },
  "member": [
    {
      "type": "measurement",
      "id": "CHLCount",
      "observedProperty": {
        "href": "http://vocab.nerc.ac.uk/collection/P01/current/FCNTRW01/"
      },
      "procedure": {
        "href": "http://vocab.nerc.ac.uk/collection/L22/current/TOOL0215/"
      },
      "result": {
        "uom": "http://vocab.nerc.ac.uk/collection/P06/current/UUUU/",
        "value": 66
      },
      "resultTime": "2016-08-02T08:42:56.179Z"
    },
    {
      "type": "measurement",
      "id": "TurbCount",
      "observedProperty": {
        "href": "http://vocab.nerc.ac.uk/collection/P01/current/NVLTOBS1/"
      },
      "procedure": {
        "href": "http://vocab.nerc.ac.uk/collection/L22/current/TOOL0215/"
      },
      "result": {
        "uom": "http://vocab.nerc.ac.uk/collection/P06/current/UUUU/",
        "value": 134
      },
      "resultTime": "2016-08-02T08:42:56.179Z"
    }
  ]
}
```
