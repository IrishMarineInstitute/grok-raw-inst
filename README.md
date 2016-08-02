# grok-raw-inst
Parsing raw text from instrument outputs using grok patterns

The developed Grok patterns can be found in the /patterns directory of this repository

A simple example of using the patterns in Python is included in the root directory

## Example output
```javascript
{
  'wavelength_turbidity': '700', 
  'timestamp': '2016-08-02T08:42:56.179Z', 
  'instrument': 'WL-ECO-FLNTU-3137', 
  'wavelength_fluorescence': '695', 
  'chlorophyll_counts': '66', 
  'thermistor': '540', 
  'turbidity_counts': '134'
}
```
