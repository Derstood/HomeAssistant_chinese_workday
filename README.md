# HomeAssistant_chinese_workday
## Chinese have chinese workday

Need this python lib:
  - workalendar
  - convertdate
  - pymeeus
  - lunardate
  - pyluach

step1. use "Custom deps deployment" install them.

step2. insert this config to */config/configuration.yaml*
```yaml
  sensor:
  - platform: chinese_workday
```

step3. restart HomeAssistant
step4. you will find entity"sensor.chinese_workday_sensor". enjoy it !

## Suggestion:
 Use a conditional-card show diffrent color and icon at weekend or workday in you lovelace
```yaml
- type: conditional
    conditions:
      - condition: state
        entity: sensor.chinese_workday_sensor
        state: 'False'
    card:
      type: tile
      entity: sensor.chinese_workday_sensor
      color: green
      show_entity_picture: false
      vertical: false
      hide_state: false
      icon_tap_action:
        action: call-service
        service: homeassistant.update_entity
        target:
          entity_id: sensor.chinese_workday_sensor
      icon: mdi:gamepad-variant-outline
      state_content:
        - state
        - last-changed
  - type: conditional
    conditions:
      - condition: state
        entity: sensor.chinese_workday_sensor
        state_not: 'False'
    card:
      type: tile
      entity: sensor.chinese_workday_sensor
      color: red
      show_entity_picture: false
      vertical: false
      hide_state: false
      icon_tap_action:
        action: call-service
        service: homeassistant.update_entity
        target:
          entity_id: sensor.chinese_workday_sensor
      icon: mdi:briefcase
      state_content:
        - state
        - last-changed
```
