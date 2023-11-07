# HomeAssistant_chinese_workday
## Chinese have chinese workday

#### step1. use "Custom deps deployment" install these python lib to HA-env.
  - workalendar
  - convertdate
  - pymeeus
  - lunardate
  - pyluach

#### step2. insert this config to */config/configuration.yaml*
```yaml
  sensor:
  - platform: chinese_workday
```

#### step3. restart HomeAssistant
#### step4. you will find an entity "sensor.chinese_workday_sensor". Enjoy it !

## Suggestion:
 Use a conditional-card show diffrent color and icon at weekend or workday in you lovelace
[example yaml](custom_components/chinese_workday/example_lovelace_config.yaml)
