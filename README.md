## sleep

**Author:** pangbo
**Version:** 0.0.1
**Type:** tool

### Description


# sleep 插件文档

## 概述

sleep 插件是一个让工作流暂停指定时间的工具。它支持多种时间单位（年、月、日、小时、分钟、秒），可以灵活地配置睡眠时间。

## 作者
pangbo

## 版本
0.0.1

## 类型
Tool

## 功能特性

- 支持多种时间单位：年、月、日、小时、分钟、秒
- 可以组合使用多个时间单位进行精确控制
- 提供友好的错误提示
- 精确的时间计算，考虑了闰年等因素

## 参数说明

| 参数名 | 类型   | 必填 | 描述         |
|--------|--------|------|--------------|
| year   | number | 否   | 年数         |
| month  | number | 否   | 月数         |
| day    | number | 否   | 天数         |
| hour   | number | 否   | 小时数       |
| minute | number | 否   | 分钟数       |
| second | number | 否   | 秒数         |


## 注意事项

1. 所有参数都是可选的，默认值为0
2. 参数可以是浮点数，如`{"second": 0.5}`表示半秒
3. 不允许使用负数作为参数，否则会返回错误
4. 时间计算考虑了每月平均30.44天，每年365.25天（考虑闰年）

## 错误处理

- 如果提供非数字参数，会返回"Error: All time parameters must be numbers."
- 如果提供负数参数，会返回"Error: Time parameters cannot be negative."
- 如果出现异常，会返回"Error during sleep operation: [error message]"

## 应用场景

1. 工作流中需要延迟执行某些操作
2. 需要控制API调用频率，防止超过速率限制
3. 在自动化测试中模拟耗时操作
4. 控制任务执行节奏，避免系统过载

## 开发者指南

插件遵循Dify插件框架的最佳实践，代码结构清晰，包含详细的文档字符串和错误处理机制。开发者可以根据需要扩展功能，例如添加更多时间单位或实现更复杂的时间调度逻辑。


# sleep Plugin Documentation

## Overview

The sleep plugin is a tool that allows workflows to pause for a specified amount of time. It supports multiple time units (years, months, days, hours, minutes, seconds) and provides flexible control over the sleep duration.

## Author
pangbo

## Version
0.0.1

## Type
Tool

## Features

- Supports multiple time units: years, months, days, hours, minutes, seconds
- Can combine multiple time units for precise control
- Provides friendly error messages
- Accurate time calculation considering leap years

## Parameters

| Parameter | Type   | Required | Description        |
|----------|--------|----------|--------------------|
| year     | number | No       | Number of years    |
| month    | number | No       | Number of months   |
| day      | number | No       | Number of days     |
| hour     | number | No       | Number of hours    |
| minute   | number | No       | Number of minutes  |
| second   | number | No       | Number of seconds  |


## Notes

1. All parameters are optional with a default value of 0
2. Parameters can be floating-point numbers, e.g., `{"second": 0.5}` for half a second
3. Negative numbers are not allowed as parameters, an error will be returned if used
4. Time calculation considers monthly average of 30.44 days and yearly average of 365.25 days (considering leap years)

## Error Handling

- If non-numeric parameters are provided, it returns "Error: All time parameters must be numbers."
- If negative parameters are provided, it returns "Error: Time parameters cannot be negative."
- If an exception occurs, it returns "Error during sleep operation: [error message]"

## Use Cases

1. Delaying execution of certain operations in a workflow
2. Controlling API call frequency to prevent rate limiting
3. Simulating time-consuming operations in automated testing
4. Controlling task execution rhythm to avoid system overload

## Developer Guide

The plugin follows best practices of the Dify plugin framework, with clear code structure, detailed docstrings, and error handling mechanisms. Developers can extend functionality as needed, such as adding more time units or implementing more complex time scheduling logic.